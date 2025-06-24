---
title: Sequential Logic
date: 2021-11-05
categories:
  - MIT 6.004
  - Computation Strcture
tags:
  - MIT Course
---

# Sequential Logic

> 课程地址：https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c5/c5s1/

## Background

用简单的逻辑门与/或/非可以实现很多逻辑函数，但有一种很简单的电路，却没办法用与/或/非直接实现，如下图所示的开关电路。

![](/posts/computation-structure/simple-switch.png)

普通的组合逻辑电路和开关电路最大的区别在于开关电路的输出还于当前的输出(状态)有关。

为了用逻辑电路来实现相同的功能，首先得让电路能*记住*上一次的状态。

## Memory

### Using Capacitors

![](/posts/computation-structure/memory-capacitor.png)

如上图所示，电容是可以存储 ”电压“ 的装置，所以很容易想到用电容来实现存储电路。不过在现实环境中，电容没办法做到完全不漏电，所以用电容实现的存储电路每隔一段时间要充一次电。

DRAM便是类似的原理，需要定时刷新电容上的电压，特点是体积小，便宜。

### Using Feedback

另一个实现存储电路的思路便是正反馈，如下图所示。

![](/posts/computation-structure/memory-feedback.png)

上图中用两个*invertor*实现的正反馈电路可以使输出稳定保持，但除了高低两个状态，还有一个中间的状态，而且该电路也可能会永远保持在中间的状态，所以我们需要避免这种情况。

### Settable Memory

![](/posts/computation-structure/settable-memory-element.png)

我们可以用一个两位的MUX来实现一个可设定的Memory.

这样的元件叫做D-latch, 即D锁存器。

![](/posts/computation-structure/d-latch.png)

要理解D-latch输入输出和时间的关系，如下图。

![](/posts/computation-structure/plea-for-lenience.png)

![](/posts/computation-structure/little-displine-for-d-latch.png)

### Try it out

虽然D-锁存器能够存储状态，但当有一连串的状态输入时，如果要保证每次只有一个状态能通过，然后被其余逻辑电路读取，然后下一个状态才能通过的话，需要对时间做非常严格的限制，但在实际环境中，各种干扰和噪声让这种限制变得几乎不太可能。

![](/posts/computation-structure/try-it-out.png)

## Move to Register

### Flaky Control System

为了解决上面*Try it out*中提到的问题，这里先用一个现实中的例子来解释一下：

![](/posts/computation-structure/flaky-control-system-1.png)

![](/posts/computation-structure/flaky-control-system-2.png)

### D-Register

我们可以按如上的例子用D-latch来实现一个这样的系统。

![](/posts/computation-structure/d-register.png)

### 各种时序图

理解D-Register的时序很重要！！！

![](/posts/computation-structure/D-Register-waveforms.png)

![](/posts/computation-structure/D-Register-hold-time.png)

![](/posts/computation-structure/D-Register-timeing-1.png)

## Summary

![](/posts/computation-structure/sequential-logic-summary.png)
