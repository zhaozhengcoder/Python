## Python 教程 

#### 1. 生成器和迭代器的区别
        
如果要创建一个100w元素的列表，直接创建出来，放在那里很耗费空间。生成器的想法是，到了需要的时候，再取创建。

通过 yield 关键字 可以实现一个生成器的函数 :
```
def myrange_func(end):
    i = 0
    while i <end:
        yield i 
        i+=1

In [11]: myrange_func(10)
Out[11]: <generator object myrange_func at 0x000001E51FA30BA0>

In [12]: f = myrange_func(10)

In [14]: next(f)
Out[14]: 0

In [15]: next(f)
Out[15]: 1

In [16]: next(f)
Out[16]: 2

# for - in 的表达式
In [17]: for i in f:
    ...:     print (i)
    ...:
3
4
5
6
7
8
9
```



#### 2. 可变对象和不可变对象


#### 3. new 和 __init__ 魔法函数


#### 4. Python的缺陷