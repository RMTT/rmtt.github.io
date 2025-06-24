---
title: "GPU 基础知识"
date: 2020-02-11T22:19:39+08:00
draft: false
keywords: ["GPU","GPU基础架构"]
categories:
- GPU
tags:
- GPU
- 基础知识
---

> 因为最近要写一篇GPU方面的论文，所以找了一些资料慢慢看
>
> 参考：[GPU Technology Trends and Future Requirements](https://ieeexplore.ieee.org/abstract/document/5424433/)
>
> 虽然是多年前的文章，不过讲得很细～



## GPU的发展

GPU的基本功能是处理图形，从最初单一的pipeline发展到现在，已经能够完成很多通用的计算任务，而且拥有远超CPU的并行计算能力。

## GPU基本知识

GPU接受的数据应该是一系列的Vertex(保存坐标信息)和Attributes(保存颜色、亮度等信息)，Vertex由专门的vertex shader处理，Attribute由pixel shader处理，shader就是GPU中的一个子程序。经过一系列的shaer处理后，最初的几何数据便会成功最终的像素合并到Frame Buffer中。

## GPU基础架构

![GPU基础架构](/posts/GPU-basic-architeture/architecture.jpg)

从架构图可以比较容易看出，基本的工作方式就是通过BUS传输数据，然后GPU中一些shader讲计算任务分发给各个TPC。至于其中各个组件的作用，见下面的MindMap。

![MindMap](/posts/GPU-basic-architeture/mindmap.png)
