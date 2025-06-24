---
title: Designing an instruction set
date: 2021-11-24
categories:
  - MIT 6.004 
  - Computation Strcuture
tags:
  - MIT Course
---

# Designing an instruction set

> 课程地址: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c9/c9s1/

本章用前8章所学的知识设计了一个简单的通用计算机，采用冯诺伊曼结构，即*main memory* + *CPU*，而CPU则主要由*datapath*(即以ALU为主的计算电路)和*control logic*(即用ROM和Register实现的FSM控制电路)。整体内容很简单，但是很好玩！

## Datapaths and FSMs

Let’s start by designing the logic that implements the desired computations — we call this part of the logic the “*datapath*”.

![](/posts/computation-structure/datapath-for-factorial.png)

上图虽然实现了a和b的计算，但还不能控制其状态，即不能在b为0时结束循环，所以需要一个FSM来控制整个计算电路即datapath的状态。

![](/posts/computation-structure/control-fsm-for-factorial.png)

![](/posts/computation-structure/control-fsm-hardware.png)

## Programmable Datapath

第一节中设计了一个可以计算介乘的datapath, 然后配上一个简单的FSM, 就可以完成计算任务。但实际中的计算任务有成千上万种，我们不能为每种任务都设计一个单独的datapath。

首先每种计算都可以分解为ALU的几个基本计算类型(Arithmetic, Bool, Comparable, Shift)，所以就计算来说，一个ALU就差不多够用了。但有的任务可能需要更多的寄存器来保存中间结果，所以增加寄存器数量是必须的。如下是一个简单的可以进行通用计算的datapath.

![](/posts/computation-structure/a-simple-programmable-datapath.png)

![](/posts/computation-structure/a-control-fsm-for-factorial.png)

## The von Neumann Model

在上一节的模型的基础上，冯诺伊曼引入了主存和输入/输出设备，从而执行数据量更大的计算任务，而且也可以有各种各样的输入输出设备，如下图所示。

![](/posts/computation-structure/the-von-neumann-model.png)

## Storage

冯诺伊曼模型的要点是用主存来存储指令和数据，主存相对于寄存器来说，最主要的优点就是容量大，所以能存储很多条指令。假如一条指令是32位也就是4bytes的话，那么1KB就能存256条指令，1M就能存256000条！

![](/posts/computation-structure/stored-program-computer.png)

在冯诺伊曼结构中，有一个专门的*PC*寄存器，用来存储*下一条*指令在主存中的地址。

![](/posts/computation-structure/anatomy-of-von-neumann-computer.png)

## 指令和指令集

指令就是用来告诉*control logic*该干什么，指令集就是按同一标准设计的一大堆指令，可以控制*control logic*干各种各样的事。指令集相关内容感觉没有太多需要记录的，所以就不记录啦。

## Summary

![](/posts/computation-structure/beta-isa-summary.png)