def sum(a):
    result=0
    
    for i in a:
        if (type(i) == int) or (type(i) == float):
            result+=i
        else:
            continue

    return result

print(sum([2,6,'测试',8]))
