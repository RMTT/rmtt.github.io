---
title: Virtual Memory
date: 2021-12-12
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# Virtual Memory

> 课程地址: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c16/c16s1/

本章主要讲了从硬盘加载数据到主存的策略, 从而引出了虚拟内存和页表.

## Extending the memory hierarchy

![](https://blog-img.rmtt.fun/posts/computation-structure-16/extending-the-memory-hierarchy.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/impact-of-enormous-miss-penalty.png)

## Virtual Memory

![](https://blog-img.rmtt.fun/posts/computation-structure-16/virtual-memory.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/paging.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/demand-paging.png)

### Page Map

![](https://blog-img.rmtt.fun/posts/computation-structure-16/simple-page-map-design.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/example-vtop.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/page-fault.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/example-page-fault.png)

### Translation look-aside buffer (TLB)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/tlb.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/mmu-address-translation.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/mmu-with-tlb.png)

### Context

![](https://blog-img.rmtt.fun/posts/computation-structure-16/contexts.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/memory-management-and-protection.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/multi-level-maps.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/rapid-context.png)

![](https://blog-img.rmtt.fun/posts/computation-structure-16/best-of-both-worlds.png)

## Summary

![](https://blog-img.rmtt.fun/posts/computation-structure-16/virtual-memory-summary.png)