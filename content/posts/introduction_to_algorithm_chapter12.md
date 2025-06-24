---
categories:
- Algorithm
date: "2021-06-27"
tags:
- Algorithm
title: 算法导论 Chapter1&2
---



# 算法

## 什么是算法

### 形式上的定义

Informally, an **algorithm** is any well-defined computational procedure that takes some value, or set of values, as **input** and produces some value, or set of values, as **output**. 

### 个人理解

算法是CS中很多技术的基础，也应该是CS的核心所在。

## 排序问题

### 插入排序

插入排序的过程跟打扑克时起牌的过程差不多，对于位置`i`的元素，在其前面找到应该插入的位置插入即可，复杂度是$\theta(n^2)$。

### 归并排序

归并排序就是将原序列递归分成多个小序列，然后合并的时候发现每个元素只需要$O(1)$的时间就可以确定其位置，比较次数较插入排序少了很多，所以复杂度比插入排序小，为$\theta(nlogn)$。

### 归并+插入

考虑到算法复杂度的常数，在数据规模较小时，插入排序可能会比归并更优，所以在归并排序中，当子序列规模小于`k`时，可采用插入排序来完成。

## 延伸问题

### 逆序对

序列中，数值和位置的大小关系不匹配便可以称为一个逆序。思考一下，可以发现插入排序中，元素的比较次数就是序列中逆序对的个数，而归并排序中同样也能推算出所有的比较次数，故可以在$\theta(nlogn)$的复杂度下解决该问题。