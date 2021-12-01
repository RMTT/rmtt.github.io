---
title: Procedures and Stacks
date: 2021-12-01
categories:
  - MIT 6.004
  - Computation Structure
tags:
  - MIT Course
---

# Procedures and Stacks

> 课程地址：https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c12/c12s1/

本章的主要内容是讲解了为什么需要Procedures和Stacks, 应该是第一次这么清晰的理解栈（

## Procedures

Procedures就是一组指令的集合，目的是为了重用指令，节约空间。当然，在高级变成语言里面都叫函数或者方法。

这里从汇编的角度来考虑如何实现Procedure, 一个最简单的办法是将Procedure在编译的时候展开，这样虽然重用了指令，但是并没有节省空间，而且无法递归调用！

另一个比较好的做法是记录Procedure的开始位置，在需要调用的时候只需要把PC设置成Procedure的地址就可以了，这样即能重用指令，也能节省空间，还能递归调用！不过问题也随之而来，当Procedure运行完后，如何知道应该返回到哪里继续执行呢？Procedure所需要的参数该如何传递呢？

![](/posts/computation-structure/implementing-procedures.png)

首先，在执行分支指令的时候，会自动计算$PC + 4$并存在指定的寄存器，所以我们可以在Procedure里面拿到要返回的地址。其次，我们可以固定几个寄存器来传递参数，比如R3 ~ R6。这样做的话，似乎可以正确执行procedure, 但是，一旦有递归调用，那这些指定的寄存器都会被覆盖，当递归最后一层结束后返回上一层时，整个调用链就“断掉”了！

![](/posts/computation-structure/procedure-calling-concention.png)

![](/posts/computation-structure/procedure-linkage-first-try.png)

而且，当procedure的参数变多时，寄存器根本不够用！

## Stacks

有了上述的问题之后，让我们再来思考一下procedure的调用需要那些工作来完成。

![](/posts/computation-structure/procedure-storage-needs.png)

首先我们需要知道Procedure的参数、返回值以及结束后PC的值，其次是procedure里面的局部变量应该存在哪里，因为在procedure执行完后，这些局部变量应该要被完全清除。我们的目标是在procedure执行过程中不会影响caller的数据，在执行完成后回到caller的时候，各个寄存器除了存放返回值的那个外，都应该是调用procedure前的状态！我们把这些在每次procedure调用时都需要记录的东西称为Activation Record。

下图演示了在递归调用时，Activation Record应该是如何变化的。

![](/posts/computation-structure/activation-record.png)

这不就是先进后出的Stack嘛！然后就是一系列的有关于Stack的定义了。

![](/posts/computation-structure/we-need-a-stack.png)

![](/posts/computation-structure/stack-implementation.png)

![](/posts/computation-structure/stack-management-macros.png)

## Stack frame

现在我们用Stack来解决之前的问题了！

![](/posts/computation-structure/solving-procedure-linkage-problems.png)

我们可以把procedure的参数，局部变量，以及procedure要使用的寄存器的内容都存到stack了！除此之外，我们还需要一些特殊的记录，比如procedure执行完后该返回的地址以及一个可以随时在栈中寻址的指针。然后，约定一个顺序来存这些数据就可以了！

![](/posts/computation-structure/stack-frame-as-activation-record.png)

栈中一个procedure的相关数据都在连续的区块中，我们称这个区块为stack frame.

![](/posts/computation-structure/stack-frame-details.png)

![](/posts/computation-structure/arguments-order-and-bp-usage.png)

然后约定好caller和callee的职责，就可以开心地使用procedure啦！

![](/posts/computation-structure/procedure-linkage-contract.png)

![](/posts/computation-structure/procedure-linkage-template.png)

## Compile procedure

如下是将C的一个递归调用编译成汇编的例子。

![](/posts/computation-structure/procedure-factorial.png)

![](/posts/computation-structure/recursion.png)

![](/posts/computation-structure/stack-detective.png)

## Summary

![](/posts/computation-structure/procedure-stack-summary.png)