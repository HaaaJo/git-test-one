#编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值
#def power(x,y):
#    return x**y
#print(power(3,2))


#编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，
#例如gcd(x, y)返回值为参数x和参数y的最大公约数,计算公式gcd(a,b) = gcd(b,a mod b)
##def gcd(x,y):
##    while True:
##        a=x%y
##        if a==0:
##            break
##        else:
##            x=y
##            y=a
##            continue
##    return x
##print(gcd(56,21))


#编写一个将十进制转换为二进制的函数，
#要求采用“除2取余”（脑补链接）的方式，结果与调用bin()一样返回字符串形式
#除2取余，逆序排序后的结果就是要得到的二进制
def dbs(x):
    list1=[]
    result=''
    while x:
        a=x%2
        x=x//2
        list1.append(a)
    
    while list1:
        result+=str(list1.pop())
        
    return result
print(dbs(125))

