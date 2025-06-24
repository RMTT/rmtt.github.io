---
title: Assembly Language
date: 2021-11-29
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# Assembly Language

> 课程地址: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c10/c10s1/

汇编语言是对指令集的抽象，用一些单词的缩写来替代指令集的opcode, 从而更容易记忆和理解。

![](/posts/computation-structure/assembly-language.png)

本课程中使用的汇编语言叫*USAM*，课程Lab里面有详细的cookbook, 就不再记录了，下面主要记录图灵机相关的内容。

![](/posts/computation-structure/assembly-language-summary.png)

## FSM的局限

FSM是一个很强大的计算模型，前面章节中我们已经用电路实现了通用FSM, 那么FSM是否可以计算所有能用数字设备计算的功能或者说函数呢？

答案是不能，比如简单的括号匹配。因为FSM要靠状态来记住`(`和`)`的个数，当有一个长度无穷大的序列时，FSM便无法构造。

![](/posts/computation-structure/fsm-limitation.png)

为了解决这个问题，Alan turing提出了`图灵机`的模型。

## 图灵机

图灵机的核心还是FSM, 不过现在多了一条无限长的纸带，FSM可以通过存储在纸带上的符号来记录额外的信息，从而避免了状态数过多而无法构造FSM的问题。

![](/posts/computation-structure/turing-machine.png)

因为一段纸带上的符号可以被编码为一个整数，所以图灵机就是一个整数函数$y = TM_I(x)$。

其中$I$是用来标识特定功能即有特定FSM的图灵机，我们可以将FSM的真值表编码成数字来表示$I$。

## Church's Thesis

$f(x) computable <=> for some k, all x f(x) = T_k[x]$

该定理由图灵的老师Church提出，但目前并没有证明，不过已经被普遍接受（可能是还没找到反例吧）。

![](/posts/computation-structure/computability.png)

## 通用图灵机

对于不同的计算任务，其构造的FSM不同，所构造的图灵机便也不同，那么为了各种计算任务，就需要构造各种各样的图灵机（实际上只有FSM不同）。那么存在一种或者一个图灵机，能够计算所有图灵机能计算的函数吗？

从21世纪的结果来看，当然是存在的！

![](/posts/computation-structure/the-universal-function.png)

如上图所示，$U(k, j) = T_k[j]$是一个Universal Function, 实现这个函数的图灵机便是通用图灵机。

实际上，这里的关键在于$k$。

![](/posts/computation-structure/universality.png)

$k$在这里是表示`program`，理论上讲就是对FSM的编码，比如用FSM的真值表来编码，而从上层计算机的角度来讲的话，$k$就是可执行的二进制程序，而PC本身就是一个通用图灵机！通用图灵机的计算便是对$k$的interpret，实际上就是把$k$本身的计算步骤走一遍。

![](/posts/computation-structure/coded-algorithms.png)

现在的各种编码算法，实际上就是把一个FSM编码成整数从而输入给通用图灵机。

不过由于内存的空间是有限的，所以实际中的计算机还是只能计算数据量不超过内存大小的任务。

## Uncomputability

如下是一个不可计算函数的例子，也就是所谓的图灵停机问题。

![](/posts/computation-structure/uncomputability.png)

![](/posts/computation-structure/why-fh-is-uncomputable.png)