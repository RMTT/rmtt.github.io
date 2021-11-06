---
title: Combinational Logic
date: 2021-10-31
categories:
  - Computation Structure
  - MIT 6.004
tags:
  - MIT Course
---

# Combinational Logic

## 如何描述电子元件的功能

+ 真值表
+ 逻辑表达式

在输入变量比较多的时候，真值表就很难读/写了，所以逻辑表达式更加通用。

## 设计数字电路的步骤

1. 写出真值表
2. 写出逻辑表达式
3. 用AND/OR/NOT三种基本逻辑门实现，或者用NAND/NOR/NOT三种逻辑门实现

因为CMOS本身就是Inverting的，所以实际中NAND/NOR更加通用。

## Sum of products

将真值表中为1的项用*OR*连接起来就得到了相应的逻辑表达式。

在功能不变的情况下，为了减少逻辑门的数量，也就是减小$t_{pd}$和$t_{cd}$，就需要将逻辑表达式中的项数最小化。

![](/posts/computation-structure/sum-of-products-implementation.png)

![](/posts/computation-structure/boolean-identities.png)

![](/posts/computation-structure/boolean-minimization.png)

###  卡诺图

![Karnaugh-map](/posts/computation-structure/karnaugh-map.png)

#### 卡诺图化简步骤

1. 找出Implicants

   ![](/posts/computation-structure/finding-implicants.png)

   ![](/posts/computation-structure/finding-prime-implicants.png)

2. 合并

   ![](/posts/computation-structure/writing-down-equation.png)

3. 处理lenient

   ![](/posts/computation-structure/lenient.png)

## Mux

![](/posts/computation-structure/mux.png)

## Decoder

![](/posts/computation-structure/decoder.png)

## ROM

![](/posts/computation-structure/ROM1.png)

![](/posts/computation-structure/ROM2.png)

## Summary

![](/posts/computation-structure/summary.png)