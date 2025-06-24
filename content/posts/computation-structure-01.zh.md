---
title: Basic of information
categories:
  - MIT 6.004
  - Computation Structure
date: 2021-09-19
tags:	
  - MIT Course
---

# Basic of Information

## 信息是什么

信息是我们接收到的关于确实某个特定事件或者情况的数据。

## 量化信息

对于随机变量$X_i$，其发生的概率为$p_i$，则其传达的信息量为:

$$I(x_i) = \log_2(\frac{1}{p_i})$$

## 数据中的信息

假设收到data的概率$p_{data}$，则

$$I(data) = \log_2(\frac{1}{p_{data}})$$

## Entropy

信息论中的entropy：

$$H(X) = \sum_{i=1}^{N}p_i\log_2(\frac{1}{p_i})$$

其中$X$为随机变量。

物理中的entropy：

$$ S = k\ln\Omega $$

其中，$k$为玻尔兹曼常数

## Meaning of Entropy

为了描述某一个随机变量$X$，需要传输一系列的数据，Entropy就是确定$X_i$发生与否的平均位数，即传输量。

## 编码

编码就是把一个数据集合映射为一系列二进制字符串。常见的编码是把英文字母用二进制来表示，比如如下表格：

|  A   |  B   |  C   |  D   |     ABBC的编码      |
| :--: | :--: | :--: | :--: | :-----------------: |
|  00  |  01  |  10  |  11  |     00 01 01 00     |
|  01  |  1   | 000  | 001  |      01 1 1 01      |
|  0   |  1   |  10  |  11  | 0 1 1 0（无法确定） |

> 编码不能有二义性

### 二叉树编码

用二叉树的边当作0和1,叶子节点当作编码的值，可以去除二义性。

### 定长编码

所有值的编码长度都相等。

### 2的补码

即将二进制最高位的全值定为$-2^{N-1}$

> 负数的补码，按位取反再加1,因为$-A = -1 - A + 1$

### 变长编码

+ 哈夫曼编码

## 错误检测

### Hamming distance

Hamming distance H等于两个二进制编码中，不同的位数。

假设数据传输中，合法的数据集合为$S$，且$S$中元素的Hamming distance为E, 则该编码系统能检测$\lfloor{\frac{E}{2}}\rfloor$Bits的错误，能纠正$\lfloor\frac{E - 1}{2}\rfloor$Bits的错误。

## Summary

![img](/posts/computation-structure/Slide28.png)
