
# #13/9
# '''DECORATORS
# FIRST CLASS OBJECT:
# 1.first class object are the oen which is treated as an other
#  object in python like,string,list,dicts etc.
# 2.we an pass a function to another function,we can return a function from another function,
#  just like any other function.
# 3. A decorator is a function which takes another function as an argument, adds extra
#  functionality and returns another function without altering the source code of original function.

# DECORATOR OVERVIEW:
# 1. A decorator takes in a function, adds some functionality and returns it.
# this is also called as metaprogramming becausse a part od the program.
# tries to modify another part of thr programs at compile time.
# A single decorator can decorate any number of functions types:
# 1.builin decorator:@class method or static method
# 2.user defined decorator:created by users
# NOTE:
# when a function is decorated with decorator function 
# (@decorator function)
# there will be 2 major changes happening.
# the parameters of outer function(func)will start pointing to main function
# builtin decorator:@class methods or static method 
# user defined decorator:created by users

# General structure of Decorators.

# def sample(func):
#     def demo(*srgs, **kwargs):
#         func(*args, **kwargs).  #modification of main_func
    
#     return demo

# @sample-->
# #main_func=sample(main_func),main_func=demo
# def main_func(parameters):
#     statement
#     return statement

# main_func(arguments)

# '''

# def out_fun(func):
#     def in_fun(*args,**kwrgs):
#         print("saii raamm")
#         func(*args,**kwrgs)
#     return in_fun

# @out_fun
# def uniq_gamer():
#     print(10+20)
#     print("hellooo")

# uniq_gamer()

# #even odd printing by giving range using decoraters
# def outer_fun(func):
#     def inner_fun(*args,**kwrgs):
#         print("*****")
#         func(*args,**kwrgs)
        
        
#     return inner_fun

# @outer_fun
# def  even(n):
#     for i in range(0,n):
#         if i%2==0:
#          print(i)
# even(20)
# @outer_fun
# def  odd(a):
#     for i in range(0,a):
#         if i%2!=0:
#          print(i)
# odd(20)


# # WAP to print a msg before and after execution of the program using decorater
# def outer_fun(func):
#     def inner_fun(*args,**kwrgs):
#         print("program started")
#         func(*args,**kwrgs)
#         print("program ended")
        
        
#     return inner_fun

# @outer_fun
# def  even(n):
#     for i in range(0,n+1):
#         if i%2==0:
#          print(i)
# even(20)

# @outer_fun
# def  odd(a):
#     for i in range(0,a+1):
#         if i%2!=0:
#          print(i)
# odd(20)


# wap to delay the program for 5 sec during transaction 

# def delay(func):
#     def inner(args,*kwrgs):
#         print('processing')
#         time.sleep(5)
#         func(args,*kwrgs)
#         time.sleep(2) #time module
#         print("transaction done")
#         return inner()

# acc_num=123456789
# acc_pin=1234
# acc_bal=1000
# @delay
# def deposit(acc,pin):
#     global acc_bal
#     if acc == acc_num:
#         if pin == acc_pin:
#             amt=int(input("enter amt"))
#             acc_bal+=amt
#             print(f"ur current bal is {acc_bal}")
# deposit(123456789,1234)



# make a decorated function which is going to call the 3 times whenever it called ?
# write a decoratedr which checks all the      if they are + or not if + execute the decorated func else print invalid inputs ?
# type check decorater 
# create a decorater function which checks all the arguments which are passed to func or integers if not print type error ?
# authentication decorater 
# create a decorater that allows a func to run only if thne user      admin otherwise print access denied ?


# WA decorater func to calculate the execution time of a function ?

import time

def time_call(func):
    def inner_func(*args,**kwrgs):
        start = time.time()
        func(*args,**kwrgs)
        end = time.time()
        print(f"time taken to execute the program is {end-start}")
    return inner_func

@time_call
def sum_list(l):
    count=0
    for i in l:
        count+=1
    print(count)
sum_list([1,2,3,4,5,5,3,3,4,3])



def sum(l):
    count=0
    i=0
    while i<len(l):
        count+=l[i]
        i+=1
    print(count)
sum([1,2,3,2,3,2,32,3,4])


# WA decorater func to cslculate the time with the delat of 3 sec only if the arguments passed are even if the arguments passed are odd calculate the delay of the time 15 sec ??