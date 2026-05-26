---
title: Pipelining the Beta
date: 2021-12-10
categories:	
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# Pipelining the Beta

> 课程地址: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c15/c15s1/

本章主要是讲如何讲前面做的Beta cpu流水线化, 以及如何解决流水线中会遇到的数据冲突/控制逻辑冲突等等.

PS: 这章内容是真多 (

## 流水线化

![](https://blog-img.rmtt.fun/posts/computation-structure-15/pipelined-implementation.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-15/too-long-course.png)

## 冲突

![](https://blog-img.rmtt.fun/posts/computation-structure-15/pipeline-hazards.png)

常见的冲突有两种,即数据冲突和控制逻辑冲突. 数据冲突是指当前指令需要的数据暂时还没有写回寄存器或者内存, 控制逻辑冲突是指当要跳转的指令的地址还没计算出来时, 下一个指令的地址应该是多少.

### 数据冲突

![](https://blog-img.rmtt.fun/posts/computation-structure-15/data-hazards.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-15/resolving-data-hazards.png)

#### Strategy 1 - Stall

Stall就是当指令运行到流水线的某一个阶段时, 如果检测到需要的数据还没有写回寄存器或者内存, 就在这个阶段阻塞住, 而且前面阶段的指令也要同时阻塞住,  阻塞的同时给下一阶段的IR寄存器输出NOP.

![](https://blog-img.rmtt.fun/posts/computation-structure-15/resolving-data-hazard-1.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-15/stall-logic.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-15/resolving-data-hazard-2.png)

#### Strategy 2 - Bypass

虽然每个指令只有在最后的Write Back阶段才会把数据写回寄存器或者内存, 但相关的值在前面的阶段就已经计算出来了, 所以可以直接把这些值bypass到可能需要的地方.

![](https://blog-img.rmtt.fun/posts/computation-structure-15/bypass-logic.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-15/fully-bypassed-pipeline.png)

### 控制逻辑冲突

![](https://blog-img.rmtt.fun/posts/computation-structure-15/control-hazard-1.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-15/control-hazard-2.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-15/resolving-control-hazards.png)

Stratege 1和2跟前面数据冲突的处理一样, 这里只记录一下第三个做法, 也就是分支预测.

#### 分支预测

![](https://blog-img.rmtt.fun/posts/computation-structure-15/resolving-hazards-with-speculation.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-15/branch-prediction.png)

## Exception and Interruption

![](https://blog-img.rmtt.fun/posts/computation-structure-15/exception-and-interrupt-logic.png)