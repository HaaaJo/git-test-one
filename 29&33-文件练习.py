##filename = input('请输入文件名：')
##f = open(filename,'w')
##txt = input('请输入内容【按:w退出】：')
##f.write(txt)
##f.close()


##def filew(filename):
##    f = open(filename,'w')
##    txt = input('请输入内容【按:w退出】：')
##    f.write(txt)
##    f.close()
##
##filename = input('请输入文件名：')
##filew(filename)

#输入不是整数时捕获异常
##import random
##
##secret = random.randint(1,10)
##print('------------------我爱鱼C工作室------------------')
##
##while True:
##    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
##    try:
##        guess = int(temp)
##        while guess != secret:     
##            try:
##                temp = input("哎呀，猜错了，请重新输入吧：")
##                guess = int(temp)
##                if guess == secret:
##                    print("我草，你是小甲鱼心里的蛔虫吗？！")
##                    print("哼，猜中了也没有奖励！")
##                else:
##                    if guess > secret:
##                        print("哥，大了大了~~~")
##                    else:
##                        print("嘿，小了，小了~~~")
##            except Exception:
##                print('输入内容不是整数，请重新输入！')
##        print("游戏结束，不玩啦^_^")
##        break
##    except Exception:
##        print('输入内容不是整数，请重新输入！')
##        continue



def int_input(name=''):
    while True:
        try:
            int(input(name))
            break
        except Exception:
            print('出错，输入的不是整数。')

int_input('请输入一个整数：')














