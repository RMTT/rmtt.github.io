---
title: Finite State Machine
date: 2021-11-07
categories:
  - Computation Structure
  - MIT 6.004
tags:
  - MIT Course
---

# Finite State Machine

> 有穷自动机本身是一个比较简单的概念，不过这里的主要难点是考虑将异步信号转换为同步
>
> 课程地址: [Finate State Machine](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c6/c6s1/)

## 本课程中自动机的表示图

![](/posts/computation-structure/valid-state-fsm.png)

## 异步时钟

当电路中的时钟信号和输入变量的时钟信号不一样时，需要将输入的时钟信号转换为与电路时钟同步的信号，从而使得电路能正常工作。

### The bounded-time Synchronizer

![](/posts/computation-structure/the-bounded-time-synchronizer.png)

当`IN`和`CLK`的上升沿到来时间$t_{IN}$和$t_{CLK}$相差大于$t_{E}$时，Synchronizer将输出至少持续$t_{D}$时长的0或1。但如果`IN`和`CLK`的上升时间沿到来时间之差小于$t_E$时，就无法确定Synchronizer的输出。为什么无法确定？个人理解是因为上升沿实际是要一段时间才能完成的，如果两者上升沿到来时间相差太短，当`CLK`达到1时，`IN`可能还在中间。

那么该如何用逻辑电路来实现这个Synchronizer，当然要靠*D-Register*啦！

![](/posts/computation-structure/d-register-synchronizer.png)

上图是用*D-Register*实现的Synchronizer, 用$t_{setup}$和$t_{hold}$来充当$t_{E}$，看起来很美好，但还没有解决`IN`和`CLK`的上升沿同时到来的问题！

当`IN`和`CLK`的上升沿同时到来时，可能会让D-latch进入metastable状态：

![](/posts/computation-structure/synchronizer-metastable-state.png)

![](/posts/computation-structure/metastable-properties.png)

解决办法：加D-Register!

![](/posts/computation-structure/declay-increases-reliability.png)

