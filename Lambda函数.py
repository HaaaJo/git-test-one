##lambda x,y=3:x*y
##
##

##def fun_A(x):
##	if x % 2:
##		return x
##	else:
##		return None



##for i in range(1,101):
##    if i%3==0:
##        print(i)

##list(filter(lambda x:not(x%3),range(101)))



##list(map(lambda x,y:[x,y],[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))


def make_repeat(n):
        return lambda s : s * n

double = make_repeat(2)
##make_repeat(2) 返回的是 lambda s: s * 2
##double 就指向这个函数

##lambda s: s * 2也可写为：
##def double(s):
##    return s * 2

##所以double(8)的8就是传给 double 函数的参数s
print(double(8))
print(double('FishC'))
