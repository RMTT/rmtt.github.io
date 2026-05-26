---
categories:
- Distributed System
date: "2021-06-19"
tags:
- Distributed System
title: MIT 6.824 Lec1 分布式：MapReduce
---



# Introduction

> paper url: http://nil.csail.mit.edu/6.824/2020/papers/mapreduce.pdf

## Why need distributed
+ parallelism
+ fault tolerance
+ physical
+ security or isolated
## Basic challenges
+ concurrency
+ partial failture
+ performence
## Map Reduce
### 个人理解
MapReduce是一个比较直观而且可以分布式的编程框架，主要过程就是将数据（输入）分发到不同的task（map过程），然后将所有task的输出收集起来shuffle一下，然后分发给另外的task（reduce过程）。从目前（2021年）来看，这个编程模型的瓶颈应该是中间的shuffle过程，因为数据量非常大的时候，shuffle过程的网络IO量也非常大。
### 关键点
MapReduce的编程模型很简单，但Google的论文中最有价值的部分是应该是关于容错和任务备份。
#### 容错
##### Worker容错
每个Task可以分为三个状态，`idle`/`in-progress`/`completed`，当task被分配给worker后，会由`idle`变为`in-progress`状态，当worker正常完成task时，会由`in-progress`变为`completed`。
当worker因意外或其他原因变得`inavaible`时，Task将会变成`idle`状态，然后master就可以将其重新分配给其他worker去完成。
##### Master容错
Master的错误比较暴力，直接做几个`mirror`就行了，如果没有`mirror`，那么当master出错时，整个系统就会宕机。
#### 任务备份
个人觉得是论文里一个不错的点，任务备份是当一个MapReduce操作（个人理解就是map和reduce)完成时，将当前`in-progress`的Task备份，然后当有空闲的worker时再将备份中的task分配过去执行。这样的好处是可以明显减少因为`straggler`的存在而导致的性能下降。
> straggler指因为磁盘、网络等原因而造成性能下降的Worker

### personal idea
因为在实际情况中，每个Worker都会因为各种因素而产生性能上的差距。同时，Master中也记录了每个task的完成时间，感觉可以用完成时间的平均值（或者之类的）来将worker放到一颗平衡树里面，然后优先用效率高的worker去完成task。
