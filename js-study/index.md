# JavaScript学习总结


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

