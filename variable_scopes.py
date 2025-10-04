''' 11/9 game 12/9
VARIABLES SCOPES:
================
There are 3 types of variable scopes
1.local variable
2.global variable
3.non-local scopes

local variables: Any variable which is created inside a function and can be accessed inside a function
we cannot access these variables outside a function

Global variables: nay variables which are created outside a function are 
called as global variables,
this can be accessed inside a function as well as outside a function

Non-local scopes:Any variables which are declared in nested functions
and this variables are neither a global nor a local variables 
this can be accessed inside a outer function and inner function but not 
outside the function
to modify these kind of variables we have to use 'nonlocal'
keyword
'''
a=10
a+=3
print(a)

# def demo():
#     a+=2
#     print(a) # cannot access local variable 'a' where it is not associated with a value
# demo()

# note:global variable can be accessed inside a function or outside a function
# but to modity a variable which defined outside a function we need to use global keyword

def demo1():
    global a 
   # b=10
    a+=1
    print(a)#14
demo1()
#print(b)# name 'b' is not defined

name="sree"
def std():
    print(name)
std()#sree

bal=1000
acc_num=987654321
acc_pin=1432
def dept(acc,pin):
    global bal
    if acc==acc_num:
        if pin==acc_pin:
            amt=int(input("enter amt"))
            bal-=amt
            print(f"ur available balance{bal}")
        else:
            print("enter the correct pin")
    else:
        print("invaild acc num")

dept(123435434,1002)#invaild acc num
dept(987654321,1432)
print(bal)
#enter amt100
# ur available balance900
# 900

# local variables 
def add():
    a=10
    b=20
    c=a+b
    print(c)
add()

# non local
# they are like glonal var for nested fun ald localn var for outer fun()

 non LOCAL VARIABLE
# this are the variable which are neither variables 
# they are global variable for nested function and local variable for outer function

# z="tinesipo"
# def food():
#     a="biryani"
#     def fruits():
#         b="apple"
#         print(z)#global varb
#         print(a)#global for fruits and local var for food
#         print(b)#local varb for fruits
#     fruits()
#     print(a)#
# print(z)
# print()

# z="tinesipo"
# def food():
#     a="biryani"
#     def fruits():
#         b="apple"
#         global a 
#         a="bum biryani"
#         print(z)#global varb
#         print(a)#global for fruits and local var for food
#         print(b)#local varb for fruits
#     fruits()
#     print(a)#
# print(z)
# food()
# #tinesipo
# # tinesipo
# # bum biryani
# # apple
# # biryani


# z="tinesipo"
# def food():
#     a="biryani"
#     def fruits():
#         b="apple"
#         # global a 
#         nonlocal a
#         a="bum biryani"
#         global z
#         z="mali ra"
#         print(z)#global varb
#         print(a)#global for fruits and local var for food
#         print(b)#local varb for fruits
#     fruits()
#     print(a)#
# food()
# print(z)
#tinesipo
# tinesipo
# bum biryani
# apple
# biryani

transaction=0
def acc_details(acc,pin):
    acc_num=123456789
    acc_pin=1234
    bal=1000
    def deposit(acc,pin):
        global transaction
        nonlocal bal
        if acc_num== acc:
            if acc_pin== pin:
                amt=int(input("enter amt"))
                bal+=amt
                print("successfully deposited")
                print(bal)
                transaction+=1
    deposit(acc,pin)
    def withdrwl(acc,pin):
        global transaction
        nonlocal bal
        if acc_num== acc:
            if acc_pin== pin:
                amt=int(input("enter amt"))
                bal-=amt
                print("withdral successfully")
                transaction+=1
                print(bal)

    withdrwl(acc,pin)
print(transaction)
acc_details(123456789,1234)
print(transaction)
