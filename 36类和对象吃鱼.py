##游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
##假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
##游戏生成1只乌龟和10条鱼
##它们的移动方向均随机
##乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
##当移动到场景边缘，自动向反方向移动
##乌龟初始化体力为100（上限）
##乌龟每移动一次，体力消耗1
##当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
##鱼暂不计算体力
##当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
import random
class Turtle:    
    def __init__(self):
        self.x = random.randint(0,10)
        self.y = random.randint(0,10)
        self.energy = 100
        
    def move(self):
        #下面两行改过，把x和y分别要移动的步长给分开了，原来是共用一个，会导致一直呈
        #对角线轨迹移动
        movex = random.choice([-2,-1,1,2])
        movey = random.choice([-2,-1,1,2])
        new_x = self.x + movex
        new_y = self.y + movey
        #移动到场景边缘时，就反向移动
        #下面的判断逻辑改过
        if new_x <= 0:
            new_x += random.choice([1,2])
        elif new_x >= 10:
            new_x += random.choice([-2,-1])
        if new_y <= 0:
            new_y += random.choice([1,2])
        elif new_y >= 10:
            new_y += random.choice([-2,-1])

        self.energy -=1
        self.x = new_x
        self.y = new_y
        #返回移动后的新位置
        return (self.x,self.y)

    def eat(self):
        if 0 <= self.energy < 100:
            self.energy += 20
        elif self.energy == 100:
            self.energy = 100
            
                
class Fish:
    def __init__(self):
        self.fx = random.randint(0,10)
        self.fy = random.randint(0,10)

    def move(self):
        #下面两行改过，把x和y分别要移动的步长给分开了，原来是共用一个，会导致一直呈
        #对角线轨迹移动
        fmovex = random.choice([-1,1])
        fmovey = random.choice([-1,1])
        new_fx = self.fx + fmovex
        new_fy = self.fy + fmovey
        #移动到场景边缘时，就反向移动
        if new_fx <= 0:
            new_fx += random.choice([1])#可以简化只写成1
        elif new_fx >= 10:
            new_fx += random.choice([-1])
        if new_fy <= 0:
            new_fy += random.choice([1])
        elif new_fy >= 10:
            new_fy += random.choice([-1])
            
        self.fx = new_fx
        self.fy = new_fy

        return (self.fx,self.fy)


turtle = Turtle()#实例化Turtle类，并同时调用初始方法生成一只乌龟的坐标
fish = []
#遍历10次生成10条鱼
for i in range(10):
    #每遍历一次，就实例化一次Fish类，并同时调用初始方法生成1个坐标,1个坐标就是1条鱼
    eachfish = Fish()
##    print(eachfish.fx,eachfish.fy)
    #把生成的坐标放到fish列表里去,重复10次，就会有十个不同的坐标，也就是生成10条鱼
    fish.append(eachfish)

while True:
    newturtle = turtle.move()
    for eachf in fish[:]:#遍历鱼的浅拷贝列表，保证在遍历的时候列表元素不会有变动
        if (eachf.fx,eachf.fy) == newturtle:
            turtle.eat()
            fish.remove(eachf)  #在原列表里移除被吃掉的鱼          
            print("有一条鱼儿被吃掉了...")
    
    for f in fish:#遍历剩下的每条鱼，然后移动
        f.move()

    if not len(fish):
        print("鱼儿都吃完了，游戏结束！")
        break
    if not turtle.energy:
        print("乌龟体力耗尽，挂掉了！")
        break

        

