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

![](assets/extending-the-memory-hierarchy.png)

![](assets/impact-of-enormous-miss-penalty.png)

## Virtual Memory

![](assets/virtual-memory.png)

![](assets/paging.png)

![](assets/demand-paging.png)

### Page Map

![](assets/simple-page-map-design.png)

![](assets/example-vtop.png)

![](assets/page-fault.png)

![](assets/example-page-fault.png)

### Translation look-aside buffer (TLB)

![](assets/tlb.png)

![](assets/mmu-address-translation.png)

![](assets/mmu-with-tlb.png)

### Context

![](assets/contexts.png)

![](assets/memory-management-and-protection.png)

![](assets/multi-level-maps.png)

![](assets/rapid-context.png)

![](assets/best-of-both-worlds.png)

## Summary

![](assets/virtual-memory-summary.png)