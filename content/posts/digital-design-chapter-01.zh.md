---
title: 数电设计和计算机结构：从0到1
date: "2021-01-27"
---

# 数电设计和计算机结构：从0到1（第一章）

## 计算机的抽象结构

+ Application Software: Programs
+ Operating Systems: Device Drivers
+ Architecture: Instructions Registers
+ Microarchitecture: Datapaths Controllers
+ Logic: Adders Memories
+ Digital Circuits: AND Gates/NOT Gates
+ Analog Circuits: Amplifiers Filters
+ Devices: Transistors Diodes
+ Physics: Electrons

## 二进制

### 信息量

N种状态需要$ log_2{N} $个Bit

### 补码

我们一般学习补码都是分正数和负数，正数不变，负数将对应的绝对值按位取反再加1。不过在这本书中学到了一个新的角度：将MSB(二进制最高位)的全值当成$  -2^{N-1}$即可，这样看补码的话也更直观一些。

## 逻辑门

### 基本的一些门电路

+ AND
+ OR
+ NOT
+ NAND
+ XOR
+ NOR
+ Buffer

### Logical level

数字电路处理的是离散量，比如电压只有高电平和低电平（一般用1和0表示），但实际上电路中的电压是连续变化的，那么怎么把连续的量转化为离散的量呢？

#### 逻辑门的输入输出电压

![逻辑门的输入输出](/posts/digital-design-chapter-01/1.png)

逻辑门的输入输出中，所用的高电平和低电平的范围可能会不相同。对于输出，高电平一般是在$V_{OH} - V_{DD}$之间，而低电平是在$GND - V_{OL}$之间。而当门电路读取输入时，低电平一般是在$GND-V_{IL}$之间，高电平是在$V_{IH} - V_{DD}$之间，这样的话，在一套逻辑电路内，必须要有:

$$ V_{OL} \leq V_{IL} $$

$$ V_{OH} \leq V_{IH} $$

而他们的差值就是能容忍的噪声。

#### 如何选择$V_{OL}$、$V_{OH}$等

对于理想的逻辑电路，低电平就是0，高电平就是$V_{DD}$，所以$V_{OL} = V_{IL} = 0$，$V_{OH} = V_{IH} = V_{DD}$。

但在实际中，电压是连续变化的，如下图所示（该图是一个NOT逻辑门的电压变化图，V(A)是输入，V(Y)是输出）：

![NOT的输入电压与输入电压](/posts/digital-design-chapter-01/1.png)

一种选择是将斜率为1和-1的点选为临界点，这些点被成为Unity Gain Points。对于在$V_{IL}$和$V_{IH}$之间的区域，被称为禁止区，如果输入的电压在禁止区内，那门电路的行为是无法判断的。

#### 一些标准

逻辑门的电压临界值原理上是可以由设计者自己决定，但为了方便不同零件的组合，工业上也有一些常用的标准：

+ TTL
+ CMOS
+ LVTTL
+ LVCMOS

上述标准都有自己的$V_{OL}$、$V_{OH}$、$V_{IL}$、$V_{IH}$等等，不一定能兼容。