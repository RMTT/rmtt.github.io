---
title: Performance Measures
date: 2021-11-11
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# Performance Measures

本章主要是讲*pipeline*的原理以及如何将一般的逻辑电路转换为*pipeline*，最后简单提到了一下异步电路和同步电路的区别。

## Latency and Throughput

*Latency*: the delay from when an input is established until the output associated with that input becomes valid.

*Throughput*: The rate at which inputs or outputs are processed.

## Pipelined Circuites

![](/posts/computation-structure/back-to-circuits.png)

如上图所示，在计算$P(X)$时，F和G一直处于空闲状态，那么有没有办法把这段时间利用起来呢？

![](/posts/computation-structure/pipelined-circuits.png)

我们可以用寄存器来保持F和G的输出，从而在$P(X)$的工作时间内，可以让F和G去进行其他计算。

![](/posts/computation-structure/pipelined-diagrams.png)

![](/posts/computation-structure/pipeline-conventions.png)

## Pipelining Methodology

![](/posts/computation-structure/a-pipelining-methodology.png)

如上是将一般逻辑电路pipeline化的一般步骤

## Circuit Interleaving

Pipeline的瓶颈在于$t_{PD}$最大的那个module, 我们可以用如下的方式将两个相同的module组合在一起，提高throughput.

![](/posts/computation-structure/circuit-interleaving.png)

![](/posts/computation-structure/circuit-interleaving-timing.png)

![](/posts/computation-structure/circuit-interleaving-timing-2.png)

![](/posts/computation-structure/combine-techniques.png)

## 异步及同步

同一个module对于不同的输入，所需要的时间可能也不一样。按之前的CLK驱动来设计电路的话，计算CLK的时候需要用module的最长计算时间，才能保证正确性。但对于一些计算较快的输入，这样做肯定是浪费了时间的。

![](/posts/computation-structure/control-structure-alternatives.png)

上图展示了用同步和异步两种方式来实现一个简单的握手协议，对于异步电路来说，不再需要全局的CLK，所以效率非常高，但实际设计非常困难；对于同步电路来说，不再需要靠CLK来在module之间传输数据，效率也提高了，虽然还是在CLK上升沿才会有数据输入输出，但CLK不需要用最长计算时间的输入来计算了。

这个简单的握手协议如下：

+ In phase 1, when the upstream stage has a new output and GOT-X is deasserted, it asserts its HERE-IS-X signal and then waits to see the downstream stage’s reply on the GOT-X signal. 
+ In phase 2, the downstream stage, seeing that HERE-IS-X is asserted, asserts GOT-X when it has consumed the available input. 
+ In phase 3, the downstream stage waits to see the HERE-IS-X go low, indicating that the upstream stage has successfully received the GOT-X signal.
+ In phase 4, once HERE-IS-X is deasserted, the downstream stage deasserts GOT-X and the transfer handshake is ready to begin again. Note that the upstream stage waits until it sees the GOT-X deasserted before starting the next handshake.

![](/posts/computation-structure/selfed-time-example.png)

## Control Structure

![](/posts/computation-structure/control-structure-taxonomy.png)

> 想不到图中 Globally timed + asynchronous 的实例QAQ

## Summary

![](/posts/computation-structure/performance-measures-summary.png)
