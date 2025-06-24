---
categories:
- Programming
- JavaScript
date: "2021-01-11"
description: JS study conclude
tags:
- javascript
title: JavaScript学习总结
---

# JavaScript学习总结

## 基础语法

js基础的语法和C/C++等众多语言类似，有8种基本类型：

+ string
+ number
+ boolean
+ null
+ undefined
+ object
+ symbol
+ bigint

以及流程控制和循环语句等：

+ if
+ switch
+ for 
+ for .. in
+ for .. of
+ while
+ do .. while

## JS Object

在js中，除了几个基本类型，其他基本都可以当成是Object。而Object这个对象就是JS中最基本的Object, 除了使用`Object.create(null)`创建的对象，其他对象都会默认使用`Object.prototype`作为自己的`[[Prototype]]`。如下是JS中几种主要Object的导图：

![JS Object](/posts/js-study/object.png)

### Function

JS中的function也是Object, 只不过是可以“执行”的Object。要注意的是，js中的`this`变量的处理与其他语言不太一样，`this`指向的是调用该函数的对象，比如`a.hi()`，调用`hi()`的时候，`this`指向的是a这个object, 而用`b.hi()`时则是指向b这个object。

#### This

在JS中，当调用Object里面的函数时，并不能用变量名直接访问对象的其他property，而是必须通过`this`变量。一般情况下，`this`就是指向调用对象的一个指针。

#### Arrow function

JS的箭头函数`() => xxx`除了是简化的函数外，还有一点比较特殊：没有`this`，所以箭头函数会直接使用调用环境下的`this`。

#### Closure

JS中闭包其实就是上下文或者说Environment的复制（估计解释型语言应该都是这样）再加上JS的垃圾回收机制（一个对象没有任何引用或者一组与Global无关的对象才会被自动回收）。Environment就是执行时的层级，其中记录了当前Block下的各种变量。比如：

```javascript
function a(){
    let count = 0;
    return function(){
        count++;
    }
}

let b = a();
```

当如上代码执行时，会先创建一个`a`的Environment，然后再创建被返回的那个匿名函数的Environment，因为匿名函数被`b`引用，而a的Environment会被匿名函数引用，便形成了一个闭包。

### Prototype

JS中的`prototype`是`Object`的一个特殊的属性，当访问`Object`的属性或者函数时，如果没有找到相应的，则会去`prototype`中寻找，因此我们可以用`prototype`来实现继承关系。因为`prototype`本身也是一个`Object`，所以可以有很多层的继承。实例的`__proto__`属性是真正的`prototype`的一个setter/getter，对于真正的prototype，一般用`[[Prototype]]`表示。

在函数和Class中，有一个`prototype`的属性，注意这个属性并不是上面所讲的`prototype`。函数和Class的`prototype`属性是用来给实例的`__proto__`或者说`[[Prototype]]`赋值的，需要使用`new`操作符。比如：

```javascript
function User(){
    this.name = "John";
}
User.prototype = {
    name: "IIa"
}
let user = new User;
console.log(User.prototype == user.__proto__);
```

### Class

Class是JS为OOP设计的一个结构，跟其他OOP语言一样有成员、方法，可以继承，有静态变量和方法，但是如下特性还只在最近的浏览器版本中部分实现：

+ 静态成员
+ 私有成员或函数(#)

JS的Class本质上也是一个Function, 只不过把`constructor`体现的更明显，其中`super`关键字也可以在普通Object中使用。

## Promise

`Promise`是JS提供的一个Async模型，类似`生产-消费者`模型。`Promise`的基本用法如下：

```javascript
new Promise(function(resolve, error){
    // 生产内容
    ...
    
    // 发给消费者
    resolve(...)  // 生产成功
    // or
    error(new Error(...)) // 生产失败
}
).then(result => ..., error => ...) // 消费者
.catch(error => ..); // 消费者
```

`Promise`中的消费者是按从上到下的顺序放入队列中，队列中上一个消费者返回的内容会被传递给下一个消费者。

### async & await

`async`和`await`个人觉得就是`Promise`的`语法糖`，本质上就是`Promise`，比如如下代码：

```javascript
async function f(){}
let result = await f();
```

其中，`async`相当于把`f`封装在了`Promise`里面：

```javascript
new Promise((resolve, error) => {
    resolve(f());
    ...
});
```

而`await`则类似`then`，只不过会阻塞线程。

## 参考

+ [The Modern JavaScript Tutorial](https://javascript.info/)
