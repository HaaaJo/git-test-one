#写一个用户登录程序（这次尝试将功能封装成函数）
def login():
    usercode = {}
    while True:
        print("---新建用户：N/n---")
        print("---登录账号：E/e---")
        print("---退出程序：Q/q---")
        code = input("请输入指令代码：")
        if code == 'N' or code == 'n':
            name = input("请输入用户名：")
            if name in usercode:
                name = input("此用户名已经被使用，请重新输入：")
                usercode[name]=input("请输入密码：")
                print("注册成功，赶紧试试登录吧。")
                continue
            else:
                usercode[name]=input("请输入密码：")
                print("注册成功，赶紧试试登录吧。")
                continue
        elif code == 'E' or code == 'e':
            name = input("请输入用户名：")
            if name not in usercode:
                name = input("您输入的用户名不存在，请重新输入：")
                if name in usercode:
                    pwd = input("请输入密码：")
                    if pwd == usercode[name]:
                        print("欢迎进入系统。")
                        break
        elif code == 'Q' or code == 'q':
            break

login()
        
#要把每个功能都写成一个单独的函数。上面都写在一个函数里去了
