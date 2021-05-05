import sys as s
c = 0
def even(num):
    global c
    newnum =(num/2)
    if num != 1.0:
        print(newnum)
        func(newnum)

def odd(num):
    global c
    newnum = ((3*num)+1)
    if num != 1.0:
        print(newnum)
        func(newnum)

def func(num):
    global c
    if num == 1.0:
        print(c)
        s.exit()
    if (num % 2) == 0:
        c+=1
        even(num)
        print(num)
    else:
        c+=1
        odd(num)
        print(num)
    

func(90762340743965878844423561778755479903)
