---
title: Devices and Interrupts
date: 2021-12-14
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# Devices and Interrupts

> 课程地址: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c18/c18s1/

本章引入外设, 讲解了round-robin调度算法的优缺点.

首先, "IO阻塞"的本质是什么?

当IO请求没有收到回复时, OS在调度到该进程时还是会继续执行等待IO的指令.

![](/posts/computation-structure/readkey-svc-3.png)

虽然每次调度到正在等待IO的进程也花不了多少条指令, 但还是要切换上下文啥的, 为了提高轮询的效率, 我们可以想办法让这些等待IO的进程不会被调度.

![](/posts/computation-structure/readkey-svc-4.png)

我们可以将进程分为不同的状态, 只有状态为0的进程可以被正常调度. 

当进程开始等待IO时, 便用 `sleep(id)` 来改变进程的状态, 其中 `id` 相当于这个IO资源的标识符, 比如可以有多个进程都在等待键盘的输入. 当相应的IO时间响应后, 再根据这个`id`去恢复进程的状态.

加了状态的轮询调度感觉也挺合理的!

那么, 轮询能满足所有的任务吗? 当然是不能!

某些特殊的系统, 例如车载系统, 会有一些特别紧急的中断必须要优先执行, 比如紧急制动啥的. 按我们之前的设计, 中断都是在内核态中执行, 而内核态会禁用中断, 所以当需要紧急制动时, 巧好有一个耗时较长的中断在执行, 可能就会引发悲剧!

像这种每个中断都要及时响应或者在一定时间内执行完成的, 一般称为实时调度.

本章介绍了弱优先级抢占和强优先级抢占两种调度算法. 区别就是当前的中断是否能被高优先级的中断中断 (