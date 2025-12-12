##def outside():
##    var = 5
##    def inside():
##        print(var)
##        var = 3
##        
##    inside()
##outside()

##def outer():
##    x = 10
##    def inner():
##        print(x)
##    return inner
##print(outer())
##f = outer()
##print(f)


def funX():
    x = 5
    def funY():
        nonlocal x
        x += 1
        return x
    return funY

a = funX()
print(a())
print(a())
print(a())
