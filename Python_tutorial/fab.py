
# 递归版本
def fib_digui(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)

# 循环版本
def fib_xunhuan(max):
    n,a,b = 0,0,1
    while n<max:
        print b
        a,b = b ,a+b
        n+=1

# 生成器的版本
def fib_generate(max):
    n,a,b = 0,0,1
    while n<max:
        yield b 
        a,b = b ,a+b
        n+=1




