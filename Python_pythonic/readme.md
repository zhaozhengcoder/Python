## pythonic 写优雅的python

#### 不要通过for in 的方式修改list
```
In [68]: mylist
Out[68]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [69]: for item in mylist:
    ...:     print (item)
    ...:     item =item *2

# 输出  发现这种方式没有办法修改list
In [70]: mylist
Out[70]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 如果想要修改 ，可以通过访问下标的方式来修改
In [71]: for index in range(len(mylist)):
    ...:     mylist[index]=mylist[index]*2
    ...:

In [72]: mylist
Out[72]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```