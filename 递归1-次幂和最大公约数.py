#用递归编写一个 power() 函数模拟内建函数 pow()，
#即 power(x, y) 为计算并返回 x 的 y 次幂的值
##def power(x,y):
    



##用递归编写一个函数，利用欧几里得算法求最大公约数，
##例如 gcd(x, y) 返回值为参数 x 和参数 y 的最大公约数
def gcd(x,y):
    print(f"调用 gcd(x={x}, y={y})")
    a=x%y
    if a==0:
        print(f"返回 {y}")
        return y
    else:
        print(f"递归: gcd(x={y}, y={a})")
        return gcd(x=y,y=a)

print(gcd(1997,615))
