---
title: "Windows10 + Linux开发环境探索"
date: 2020-03-07T01:39:24+08:00
draft: false
categories:
- Windows
- Linux
---

## 为什么要Windows + Linux

其实主要是因为N卡和CUDA，不然直接macOS就行了 (x)

## 探索经历

### Arch + i3wm + kvm

众所周知，Arch是最好的发行版(x)，配上i3wm的便捷操作，效率确实能提高不少，但是最终还是放弃了这个方案。放弃的原因并不是因为软件的问题，主要还是因为硬件的问题，一是主板不支持vt-d，不能直通显卡给KVM，而windows和macOS都是比较吃显卡的，二是新换的Intel AX200在Linux固件上还有点问题，不过这个问题是personally。

### Windows10 + Hyper-v

最终还是选择了这个方案，主要是因为Linux可以不吃显卡，有图形化的需求可以直接在Windows上跑一个X Server。

#### Hyper-v安装Arch

安装过程都是傻瓜式的，因为我笔记本上刚好有两块SSD，索性就直接把Arch装在256G的PM961上了，然后Switch用的就是默认的Switch。

#### Arch安装Hyper-v Integration Service

微软提供了一套服务来让宿主机和Hyper-v VM交互，包括文件传输、状态监控、获取IP等等，只需要安装`hyperv`这个包就行了，然后开启如下三个daemon:

+ hv_kvp_daemon
+ hv_vss_daemon
+ hv_fcopy_daemon

不过启动这3个service后再重启VM，马上就会发现问题：这3个Service启动时有很大的可能会失败。然后看了一下Service的内容:

```shell
[Unit]
xxx
ConditionPathExists=/dev/vmbus/hv_xxx
```

失败的原因是ConditionPathExists不满足，但是奇怪的是重启登录后这个设备是存在的，手动启动是可以成功的，于是开始Google(期间因为网络问题错过了标准答案，还好后来archlinuxcn群里有人帮忙找到了答案)。在Redhat的论坛里有一篇15年的[帖子](https://bugzilla.redhat.com/show_bug.cgi?id=1195029)讨论 了这个问题，然后我看了一下日志发现现在2020年了，hyper-v的这个设计还是一样毫无变化。主要的原因就是hyper-v的这个vmbus是通过netlink挂载上去的，而网络传输是存在延迟的，所以就会导致在Integration Service启动的时候vmbus还没有挂载上，不过解决的办法也很简单，就是自己添加一个udev的rule，在vmbus成功挂载时再次启动相应的service：

```shell
SUBSYSTEM=="misc",KERNEL=="vmbus/hv_kvp",TAG+="systemd",ENV{SYSTEMD_WANTS}+="hv_kvp_daemon.service"
```

那么Integration Service启动失败的问题就差不多解决了(期间因为把`==`写成了`=`，找了好几个小时 TwT)。

#### Windows Terminal的配置

Windows Terminal是微软官方发布的一款terminator，目前还在preview，不过已经0.9了，估计可能20H1就要发布正式版了。

第一步当然是要先换字体和配色，字体很简单，用`fontFace`配置就行了，然后配色，刚好自带了[Solarized](https://ethanschoonover.com/solarized/)(目前最喜欢的配色)，不过如果是Powershell最好换用其他颜色，因为PS的语法亮尚会和Solarized冲突。(感谢这些愿意无私奉献的艺术家们)

![Solarized](/posts/windows-environment/solarized-yinyang.png)

接下来就是配置ssh登录Arch，因为Default Switch的IP range是dynamic的(为什么不用Static IP?因为之前试过几次都不稳定，不是突然变了就是突然连不了Internet了)，所以需要动态获取Arch的IP，好在Powershell提供了很多操作命令，实现起来很简单：

```powershell
function arch_addr {
    $addr = (Get-VMNetworkAdapter Arch).ipaddresses[0]
    return $addr
}
```

同时为了支持转发X，需要配置端口转发，因为Windows Terminal中直连貌似不行，完整的代码如下：

```powershell
$arch_switch="Default Switch"

function arch_addr {
    $addr = (Get-VMNetworkAdapter Arch).ipaddresses[0]
    return $addr
}

function arch_switch_addr {
    return (Get-NetIPAddress | Where-Object {$_.InterfaceAlias -like "*($arch_switch)*" -and $_.AddressFamily -eq "IPv4"}).ipaddress    
}
function    arch {
    $addr = arch_addr
    $switch_addr = arch_switch_addr
    $x_port = 6000
    ssh -R $switch_addr`:$x_port`:localhost`:$x_port  mt@$addr -i C:\Users\RMT\.ssh\arch
}
```

同时需要手动在Arch中设置`DISPLAY`，然后就可以转发X了，Windows10用的是VCXSRV。

![配置完成的windows terminal](/posts/windows-environment/wt.png)

#### 共享文件夹

共享文件夹直接使用CIFS就行了，首先安装`cifs-utils`，然后在Windows10中配置一个共享文件夹，然后直接[挂载](https://wiki.archlinux.org/index.php/Hyper-V#Shared_directories)即可，不过要注意在Arch中登录Windows10时，使用的是你微软账户的密码而不是本地的PIN。

```shell
mount -t cifs //PC/share /mnt/Hyper-V -o credentials=~/.credentials,ip=xxx
```

#### 在hosts中自动更新Arch的IP

因为Arch的IP是动态的，如果想在CLION等工具是使用Arch上的toolchain，那每次都要更改一次设置还是挺麻烦的，索性就用脚本在每次开机的时候自动更新hosts，把Arch的ip加进去：

```powershell
$arch_switch="Default Switch"

function arch_addr {
    $addr = (Get-VMNetworkAdapter Arch).ipaddresses[0]
    return $addr
}

$path_hosts = "C:\\Windows\\System32\\drivers\\etc\\hosts"
$host_content = Get-Content -Path $path_hosts

$arch_host_name = "Arch"

$arch_addr = arch_addr
$flag = 0
$line = 0
foreach($msg in $host_content){
    if ($msg -like "*$arch_host_name*"){
        $flag = 1
        break
    }
    $line++
}

if($flag -eq 1){
    $host_content[$line] = "$arch_addr Arch"
    Out-File -FilePath $path_hosts -Encoding ASCII -InputObject $host_content
}else {
    Out-File -FilePath $path_hosts -Append -Encoding ASCII -InputObject "$arch_addr Arch"
}

ipconfig.exe /flushdns
```

之后就可以在任何地方直接用Arch来代替ip 了。

![CLION的remote配置](/posts/windows-environment/clion.png)

#### 在Arch中获取Windows的IP

因为Default Switch用的是NAT，所以可以直接用`ip n`查看Default Switch的ip，通过这个ip便可以访问Windows宿主机，比如使用宿主机中的代理：

```shell
win_addr=$(ip n | awk '{print $1}')
export http_proxy="http://$win_addr:port"
```





## 总结

看了下Hyper-v的交互性其实挺强的，还有很多可以扩展的空间，感觉完全可以手动实现一个WSL?比如如果想在Windows10上直接启动Arch里面的App，可以自己写一个powershell脚本:

```shell
ssh -X -R xxx:xxx:xx:xx xx@xx "code"
```

然后新建一个快捷方式，执行命令`powershell xx.ps1`

然后就是在Arch中调用Windows10的程序，之前看了一下X410这个东西，Hyper-v可以和Windows宿主机建立一个VSOCK，那么两边分别运行一个监听程序，来处理相互的调用感觉是可行，等有时间了可以试试。

