---
title: Caches and the Memory Hierarchy
date: 2021-12-07
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course

---

# Caches and the Memory Hierarchy

>  课程地址：https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c14/c14s1/

本章主要讲了*SRAM*、*DRAM*、Flash、HDD的原理和现代CPU的缓存架构。

## 存储设备

PS: 片上的存储设备一般都有bitline和wordline, wordline用来激活指定的存储单元，bitline用来读/写数据。

### SRAM

SRAM跟寄存器比较像，都是用正反馈是保持电压。

![](/posts/computation-structure/static-ram.png)

![](/posts/computation-structure/sram-cell.png)

![](/posts/computation-structure/sram-read.png)

![sram-write](/posts/computation-structure/sram-write.png)

### DRAM

DRAM是使用电容来保持电压，体积更小，所以容量更大，但访问速度比SRAM慢，而且需要定时刷新存储的数据。

![](/posts/computation-structure/dram-cell.png)

![](/posts/computation-structure/dram-write-and-read.png)

### Flash

Flash是使用MOSFET来存储数据，在栅极下加了一层绝缘体，讲电子导入绝缘体，然后根据绝缘体的带电大小来决定数据。

![](/posts/computation-structure/flash.png)

### Hard Disk

硬盘（这里指机械硬盘）是用磁化来存储数据。

![](/posts/computation-structure/hard-disk.png)

## 内存系统

在现代CPU的架构中，主存一般是速度相对较慢但是体积更小的DRAM组成。不过CPU不会直接跟主存交换数据，在中间可能会有其他几层SRAM来充当缓存，以降低内存的平均访问时间。

![](/posts/computation-structure/the-memory-hierarchy.png)

但从编程的角度看，有这样两种选择。一是完全隐藏缓存的细节，这样写程序时便可以把内存当成一个单独的设备使用；二是公开缓存细节，由programmer去决定哪些数据放在缓存，哪些放在主存。

![](/posts/computation-structure/memory-hierarchy-interface.png)

现在除了超算，基本都是选择隐藏缓存的细节。

## Cache策略

既然要隐藏缓存的细节，那么需要用硬件或者软件来自动控制哪些数据应该放在缓存，当缓存命中时，直接返回给CPU，未命中时，缓存应当自主去主存读数据然后缓存起来并返回给CPU. 下面来讨论一下具体的缓存策略.

### 前提

在模拟测试中, 可以发现这样一个事实:

![](/posts/computation-structure/the-locality-property.png)

![](/posts/computation-structure/memory-reference-patterns.png)

### Direct-Mapped

![](/posts/computation-structure/direct-mapped.png)

![](/posts/computation-structure/block-size.png)

### Full-Associative

![](/posts/computation-structure/full-associative-cache.png)

### Set-Associative

![](/posts/computation-structure/n-way-associative-cache.png)

## Policies

### Replacement Policies

![](/posts/computation-structure/replacement-policies.png)

### Write Policy

![](/posts/computation-structure/write-policy.png)

![](/posts/computation-structure/write-back.png)

## Summary

![](/posts/computation-structure/cache-summary.png)