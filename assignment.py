# make a decorated function which is going to call the 3 times whenever it called ?
# write a decoratedr which checks all the      if they are + or not if + execute the decorated func else print invalid inputs ?
# type check decorater 
# create a decorater function which checks all the arguments which are passed to func or integers if not print type error ?
# authentication decorater 
# create a decorater that allows a func to run only if thne user      admin otherwise print access denied ?


# def delay(func):
#     def inner(args,*kwrgs):
#         print('processing')
#         time.sleep(15)
#         func(args,*kwrgs)
#         time.sleep(2)
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



# 2nd
# WA decorater func for authentication , validation and for encryption of the password for insta login ??


def repeat(func):
    def inner(*args,**kwrgs):
        for i in range(3):
            print(f"execution{i+1}:")
            func(*args,**kwrgs)
    return inner
@repeat
def name(name):
    print(f"Hello,{name}!")
name("ravitejaaa")

