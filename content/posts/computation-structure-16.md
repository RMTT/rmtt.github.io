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

![](/posts/computation-structure/extending-the-memory-hierarchy.png)

![](/posts/computation-structure/impact-of-enormous-miss-penalty.png)

## Virtual Memory

![](/posts/computation-structure/virtual-memory.png)

![](/posts/computation-structure/paging.png)

![](/posts/computation-structure/demand-paging.png)

### Page Map

![](/posts/computation-structure/simple-page-map-design.png)

![](/posts/computation-structure/example-vtop.png)

![](/posts/computation-structure/page-fault.png)

![](/posts/computation-structure/example-page-fault.png)

### Translation look-aside buffer (TLB)

![](/posts/computation-structure/tlb.png)

![](/posts/computation-structure/mmu-address-translation.png)

![](/posts/computation-structure/mmu-with-tlb.png)

### Context

![](/posts/computation-structure/contexts.png)

![](/posts/computation-structure/memory-management-and-protection.png)

![](/posts/computation-structure/multi-level-maps.png)

![](/posts/computation-structure/rapid-context.png)

![](/posts/computation-structure/best-of-both-worlds.png)

## Summary

![](/posts/computation-structure/virtual-memory-summary.png)