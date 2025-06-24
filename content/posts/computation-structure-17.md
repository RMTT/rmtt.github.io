---
title: Virtualizing the Processor
date: 2021-12-13
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# Virtualizing the Processor

> 课程地址: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c17/c17s1/

本章讲了CPU的"虚拟化", 不过这里的"虚拟化"是指在同一个CPU上执行多个程序, 并且互不干扰, 重点当然就是虚拟内存和MMU啦.

现代CPU都在硬件上实现了内核态和用户态, 所以无法单纯靠软件来实现内核态和用户态的切换, 而是要靠CPU的中断来实现.

![](/posts/computation-structure/timer-interrupts.png)

当Timer发起一个中断时, 我们调用OS的schedule程序来切换用户程序的上下文, 那么具体需要切换哪些内容呢? 常见的就是所有寄存器的内容, MMU的Context和Page Directory/Page Map的base pointer, 还有其他各种外设的状态等等, 比如该用户程序的输入应该在哪个tty.

![](/posts/computation-structure/simple-timesharing-scheduler.png)

这种代码+上下文+所有相关资源的集合便是一个进程(Process).

众所周知, OS提供的底层接口都是在内核态运行, 因为内核态不会受中断的干扰, 所以能够保持调度器一直能正常运行. 但是CPU是禁止程序从用户态直接转移到内核态的, 唯一的办法便是通过中断或者异常. 

现代的CPU都运行设置部分中断和异常的Handler, 当用户态程序有中断或异常产生时, 便会跳转到相应的Handler去执行, 而且会无视用户态/内核态的区别. 所以, OS可以指定自己的异常处理Handler, 对于每一个系统调用, 都分配一个illegal-opcode就可以啦!

![](/posts/computation-structure/illop-handler.png)