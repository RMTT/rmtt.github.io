---
title: Parallel Processing
date: 2021-12-16
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# Parallel Processing

> 课程地址: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c21/c21s1/

本章讲的是各种并行方案.

## 并行

并行大体上有如下3种:

- 指令级并行(ILP)
- 数据级并行(DLP)
- 线程级并行(TLP)

### 指令级并行

指令级并行是让流行线的每个阶段尽可能同时执行多条指令.

![](/posts/computation-structure/superscalar-processor.png)

### 数据级并行

数据级并行主要是指像向量加法这种计算, 天生就能拆开运算的! 只需要提供多个ALU就行了, 目前主要是由GPU来做.

![](/posts/computation-structure/data-level-parallelism.png)

### 线程级并行

首先介绍一下阿姆达尔定律:

![](/posts/computation-structure/amdahl-law.png)

一个线程就是在一个core上执行的计算任务.

> Using multiple independent cores to execute a parallel task is called thread-level parallelism (TLP), where each core executes a separate computation “thread”.

![](/posts/computation-structure/thread-level-parallelism.png)

不同的Core之间是通过同一个main memory来交换数据(还有更高效的MPI), 而且每个core都有自己的cache.

![](/posts/computation-structure/multi-core-caches.png)

为了保证数据的一致性, 在cache和内存之间也有一条bus来监测cache的变化和同步.

> 例如MESI protocal: https://en.wikipedia.org/wiki/MESI_protocol