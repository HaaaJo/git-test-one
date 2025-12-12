for i in range(100,1000):
    bai = i//100
    two = i%100
    shi = two//10
    ge = two%10
    if bai**3+shi**3+ge**3 == i:
        print(i,'是水仙花数')
    else:
        continue

##            
##member=['小甲鱼', 90, '黑夜', '迷途', '怡静', '秋舞斜阳', 88]
##for i in member:
##    print(i)
##    
