---
title: Concurrency and Synchronization
date: 2021-12-15
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# Concurrency and Synchronization

> 课程地址: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c19/c19s1/

本章主要是讲进程间通信(IPC), 不过是从硬件的角度来看.

IPC里面常用的信号量, 其实也只是在共享内存中存入了一个数字, 而所谓的lock, 也只是数量为1的semaphore.

但是如果不同core上的进程同时对同一个内存地址进行写操作的话, 会产生冲突吗? 这个貌似是内存或者总线去解决的, 目前还没找到具体实现, 先mark一下.

![](/posts/computation-structure/hardware-support-semaphore.png)

IPC的一个重要问题是deadlock, 比如进程A和进程B:

```
# 进程A
wait(x)
wait(y)
```

```
# 进程B
wait(y)
wait(x)
```

当进程A执行完`wait(x)`后, 进程B被调度, 而且执行了`wait(y)`, 显然这两个进程永远都无法结束.

一个比较直观而且简单的方案是对IPC中需要用到的信号量进行排序, 在进程`wait`时, 总是先`wait`顺序在前的信号量.