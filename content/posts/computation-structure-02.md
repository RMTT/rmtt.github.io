---
title: The Digital Abstraction
categories:
- MIT6.004
- Computation Structure
date: 2021-09-30
tags:
- MIT Course
---

# The Digital Abstraction

## 信息编码

信息的种类有各种各样，我们需要找到一种方式来表示这些信息。比如，生物的基因信息是通过DNA来记录和表达，在计算机中，所有的数据都是二进制，我们也需要一个物理介质来表达和存储这些二进制信息。

## 电压

目前用来存储和表达二进制信息的物理介质绝大部分都是使用电压，高电平表示1, 低电平表示0。

## VTC和容错

VTC(voltage transfer characteristics)是用来表示一个电子原件的输入和输出电压关系的图，如下是一个*Buffer*的VTC：

![img](/posts/computation-structure/Slide17.png)

其中$V_{IL},V_{IH},V_{OL},V_{OH}$是一个电子元件最重要的参数，解释如下（这里假设最高电压为1）：

+ $V_{IL}$是低电平的输入有效范围，即如果输入电压为$[0,V_{IL}]$，就会被元件当成0处理。
+ $V_{IH}$是高电平的输入有效范围，即如果输入电压为$[V_{IH}, 1]$，就会被元件当成1处理。
+ $V_{OL}$是低电平的输出电压，即如果元件想输出0，则其输出电压应该为$[0, V_{OL}]$。
+ $V_{OH}$是高电平的输出电压，即如果元件想输出1，则其输出电压应该为$[V_{OH},1]$。

其中, $min(|V_{OL} - V_{IL}|, |V_{OH} - V_{IH}|)$即为该元件能容忍的噪声范围。

## Summary

![img](/posts/computation-structure/Slide20.png)