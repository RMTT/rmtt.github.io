---
title: System-level Communication
date: 2021-12-16
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# System-level Communication

> 课程地址: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c20/c20s1/

本章主要讲的是系统间通信, 按现在来讲就是总线(BUS).

前面讲了很多硬核的物理知识, 证明了单一总线因为传输线反射的问题, 无法做到高频.

后面介绍了PCIe, 原来PCIe是受Network的启发, 也搞了一套点对点的通信协议, 跟网络一样分了几层, 数据也是包装成packet发出去.

![](/posts/computation-structure/pcie.png)

跟网络一样, PCIe也可以有多种top, 比如环形, 树形等等.