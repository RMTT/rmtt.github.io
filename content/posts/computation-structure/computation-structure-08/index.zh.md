---
title: Design Tradeoffs
date: 2021-11-18
categories:
  - MIT 6.004
  - Computation Structure
tags:	
  - MIT Course
---

# Design Tradeoffs

> [课程地址](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c8/c8s1/)

本章从CMOS的电能消耗出发，讲如何减少不必要的能量损失，同时也讲了很多时间和空间的tradeoff.

## Power dissipation

### 电路优化的几个metrics

![](assets/optimizing-your-design.png)

### CMOS能耗

![](assets/cmos-static-power-dissipation.png)

![](assets/cmos-dynamic-power-dissipation.png)

![](assets/cmos-dynamic-power-dissipation-2.png)

### 一个减小能耗的简单例子

![](assets/how-can-we-reduce-power.png)

![](assets/fewer-transitions.png)

## Carry-select Adder

设计一个N位的加法器，最直观的设计就是把N个全加器串联。

![](assets/adder-example.png)

但是这样的$t_{PD}$是$\theta(N)$级别的。

现在将一个32位的加法器分成两个16位的部分分别计算再组合，$t_{PD}$就差不多减小了一半。

![](assets/carry-select-adder.png)

按这个思路一直二分下去，$t_{PD}$便能达到$O(\log n)$。

![](assets/32-bits-carry-select-adder.png)

## Carry lookahead Adder(CLA)

![](assets/faster-carry-logic.png)

从$C_{out}$的计算公式中可以看出，一个FA的输入可以转换成3个变量$P$,$G$和$C_{in}$ ，其中只有$C_{in}$需要该位的前一位的$C_{out}$。

如果知道了两个相邻位置的$P$和$G$，那么可以把这两位当作一个整体，计算出这个整体的$P$和$G$，这时$P$和$G$任然还保留着原来的性质，所以，我们可以用倍增来计算整个电路的$P$和$G$。

![](assets/carry-lookahead-adder.png)

下图是一个8-bits的CLA的G&P generate的部分：

![](assets/8-bit-cla-generate-G&P.png)

然后是计算Carry的方法：

![](assets/8-bit-cla-carry-generation.png)

完整版：

![](assets/8-bit-cla-complete.png)

## Multiplier

### binary multiplication

就是普通的竖式乘法，但是要注意如果值是补码，那最高位的全值为$-2^{N-1}$而不是$2^{N-1}$。

![](assets/binary-multiplication.png)

![](assets/combinational-multiplier.png)

如下是值为补码的情况：

![](assets/complement-multiplication.png)

![](assets/complement-multiplier.png)

### pipelined multiplier

![](assets/pipelined-multiplier.png)

虽然pipeline化了，但每个stage的$t_{PD}$还是$O(N)$的，主要问题在于要按行传递carry。

### Carry-save multiplier

![](assets/carry-save-multiplier.png)

讲每行需要传递的carry降到下一行（反正都是加在同一列，所以对结果没影响），这样可以将每个stage的$t_{PD}$优化到$O(1)$，但是需要更多的行，也就是面积增加了。

### 用时序电路减少面积

![](assets/sequential-logic-multiplier.png)

求和->移位->求和。

## Summary

![](assets/design-tradeoff-summary.png)