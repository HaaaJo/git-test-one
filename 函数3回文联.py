##def words(txt):
##    list1 = []
##    for x in txt:
##        list1.append(x)
##    list2 = list(reversed(list1))
##    if list2 == list1:
##        print('是回文联')
##    else:
##        print('不是回文联')
##
##a = input('请输入一句话：')
##words(a)


##def counts(params):
##    english = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
##    
##    number = '0123456789'
##    eng = 0
##    emp = 0
##    num = 0
##    other = 0
##    
####    for x in params:
##    for i in params:
##        if i in english:
##            eng +=1
##        elif i == ' ':
##            emp +=1
##        elif i in number:
##            num +=1
##        else:
##            other +=1
##    print('英文字母:',eng,'数字:',num,'空格;',emp,'其他字符;',other)
##    
####没想好传入多个值的时候要怎么写    
##counts('i love fishc.com.')


def counts(*params):
    english = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    number = '0123456789'
    eng = 0
    emp = 0
    num = 0
    other = 0
    lenth = len(params)
    
##    for x in range(lenth):
    for i in params:
        if i in english:
            eng +=1
        elif i == ' ':
            emp +=1
        elif i in number:
            num +=1
        else:
            other +=1
    print('英文字母:',eng,'数字:',num,'空格;',emp,'其他字符;',other)
    
##没想好传入多个值的时候要怎么写    
counts('i love fishc.com.')
