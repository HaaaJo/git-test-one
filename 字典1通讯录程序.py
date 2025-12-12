##dict1 = {'F': 70, 'C': 67, 'h': 104, 'i': 105, 's': 115}
##print(dict1['C'])

print("---欢迎进入通讯录程序---")
print("---1：查询联系人资料---")
print("---2：插入新的联系人---")
print("---3：删除已有联系人---")
print("---4：退出通讯录程序---")

usernote = {}

while True:
    code = int(input("请输入相关的指令代码："))
    if code == 1:
        name = str(input("请输入联系人姓名："))
        #这里还缺少对name是否在字典里的判断
        print(f"{name}:{usernote[name]}")
            
    elif code == 2:
        name = str(input("请输入联系人姓名："))
        
        if name in usernote:
            print(f"您输入的姓名在通讯录中已存在--->>{name}:{usernote[name]}")
            updatephone = str(input("是否修改用户资料（YES/NO）："))
            if updatephone == 'YES':
                usernote[name] = str(input("请输入用户联系电话："))
                continue
        else:
            usernote[name] = str(input("请输入用户联系电话："))
        
        continue
    elif code == 4:
        print("---感谢使用通讯录程序---")
        break


