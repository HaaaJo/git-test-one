secert = 'abc123'
i = 3

while i >0:
    insec = input('请输入密码：')
    if '*' in insec:
        print('密码中不能含有"*"号！你还有',i,'次机会！')
        continue
    else:
        if insec != secert:
            i -=1
            print('密码错误！你还有',i,'次机会！')
            continue
        else:
            print('密码正确，进入程序...')
            break
    i-=1
