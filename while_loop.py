#while loop
#while loop is a looping statement which is used to execute same set of instructions repeatedly
#again and again until the condition is false.
#in while loop initialisation of looping variable is mandatory. and updation of looping variable is also mandatory
#if we don't looping a variable then the controller through an error to avoid that we can use boolean True or a keyword
#upadation of a looping variable is mandatory if not it is going to fall inside a infinite loop.
#infinite loop it works on cpu until RAM get full.it destroy ram and motherboard 
#(if a proragm falls inside a infinite loop it must be stop break using cntlr+c if not RAM or harddisk will be correpted)


#SYNTAX:
#initialisation:
#while condition:
#<tab> statement block(code to execute)
#      updation of a looping variable

#flow diagram
#initilation
#true
#true->while condition       ->false out of loop (means final o/p)
#true-> 
# execute the code
#true->
# update the code
# true-> go to while condition

#WAPP to print your name five times
# name="sreedeep"
# i=1  #intialzer
# while i<=5:  #condition 
#     print(name) #print statement
#     i+=1  #increase i by 1

# i=1  #intialzer
# while i<=5:  #condition 
#     print("sree") #print statement
#     i+=1  #increase i by 1
#1<=5 true sree
#2<=5 true sree
#3<=5 true sree
#4<=5 true sree
#5<=5 true sree
#6<=5 False


#WAPP to print n natural numbers
# WAPP to print n natural numbers using while loop

# n = int(input("Enter a number: "))
# i = 1   # starting number
# while i <= n:   # loop runs till n
#     print(i)    #print
#     i += 1      # increment i
# #1<=5 true 1
#2<=5 true 2
#3<=5 true 3
#4<=5 true 4
#5<=5 true 5
#6<=5 False


#WAPP to print first 50 even numbers

# i=0
# while i<=10:
#     print(i)
#     i+=2
#0<=10 true 0
#2<=10 true 2
#4<=10 true 4
#6<=10 true 6
#8<=10 true 8
#10<=10 true 10
#12<=10  false
#or
# i=0
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1
#incrementation
#0<=10 true 0
#2<=10 true 2
#4<=10 true 41
#6<=10 true 6
#8<=10 true 8
#10<=10 true 10
#12<=10  false

#while i<=100: upto #0<=100 true 0 o/p

#22/8



# write a programe to print the multiplication of a givenn number 
# n=int(input("enter number"))
# i=1
# while i<=10:
#     print(f"{n}*{i}={n*i}")
#     i+=1



# ## write a programe to print all the values which are divisible by 5 within the range of 100 
# i=1
# while i<=100:
#     if i %5==0:
#         print(i)
#     i+=1
    

## write a programe to print the sum of n natural numbers
# n=int(input("enter natural num"))
# i=1
# result=0
# while i<=n:
#     result+=i
#     i+=1
# print(result)



# factorial of a number

# n=int(input("enter natural num"))
# i=1
# result=1
# while i<=n:
#     result*=i
#     i+=1
# print(result)




# write a prog to extract all the lowercase char from a goiven string and store it in a string format

# s="we are best friENds "
# i=0
# l=[]
# while i<=len(s)-1:
#     if 97<=ord(s[i])<=122:
#         l.append(s[i])
#     i+=1
# print("".join(l))


# s="we are best friENds "
# i=0
# l=[]
# while i<=len(s)-1:
#     if s[i].islower():
#         l.append(s[i])
#     i+=1
# print("".join(l))


# write a prog to extract all the special char from a goiven string and store it in a string format

# s="we are best friENds @!##%"
# i=0
# l=[]
# while i<=len(s)-1:
#     if not s[i].isalnum():
#         l.append(s[i])
#     i+=1
# print("".join(l))


# s="we are best friENds @!##%"
# i=0
# l=[]
# while i<=len(s)-1:
#     if not (65<=ord(s[i])<=90 or 97<=ord(s[i])<=122 or ord(s[i])==32):
#         l.append(s[i])
#     i+=1
# print("".join(l))


# write a prog to  sum of all the integers present in a heterogeniouns list


# l=[10,2.5,40,"hello",True,"rahul",420,84.0,20+6j,-10]

# i=0
# s=0
# while i<len(l):
#     if type(l[i])==int:
#         s+=l[i]
#     i+=1
# print(s)

#WAPT extract all the values present in the tuple which are in the even position and print it

# t = (10, 2.5, 40, "hello", True, "sree", 420, 84.0, 20+6j, -10)
# i = 0
# while i < len(t):
#     if i % 2 == 0:   # check if index is even
#         print(t[i])
#     i += 1
#10
# 40
# True
# 420
# (20+6j) 

#WAPP to extract characters from a given string at there odd index without slicing

# t = "raviteja"
# i = 0
# while i < len(t):
#     if i % 2 == 0:   # check if index is even
#         print(t[i])
#     i += 2


# s=input("enter password")
# uc=0
# lc=0
# sp=0
# num=0
# space=0

# i=0
# while i<len(s):
#     if s[i].isupper():
#         uc+=1
#     elif s[i].islower():
#         lc+=1
#     elif s[i].isdigit():
#         num+=0
#     elif s[i].isspace():
#         space+=1
#     else:
#         sp+=1
#     i+=1
# if 7<=len(s)<=15:
#     if uc>=1:
#         if lc>=1:
#             if num>=1:
#                 if space ==0:
#                     if sp>=0:
#                         print("password is valid")

#                     else:
#                         print("pass must contain specuial char")
#                 else:
#                     print("pass should not contain space ")
#             else:
#                 print("pass must contain atleast 1 number")
#         else:
#             print("pass must contain 1 lower char")
#     else:
#         print("pass must contain atleast 1 upper char")
# else:
#     print("pass must contain 7 char")

# s=input("enter the password")
# uc=0
# lc=0
# sp=0
# num=0
# space=0

# i=0
# while i<len(s):
#     if s[i].isupper():
#         uc+=1
#     elif s[i].islower():
#         lc+=1
#     elif s[i].isdigit():
#         num+=1
#     elif s[i].isspace():
#         space+=1
#     else:
#         sp+=1
#     i+=1
# #print(uc,lc,num,space,sp)
# if 7<=len(s)<=15:
#     if uc>=1:
#         if lc>=1:
#             if num>=1:
#                 if space==0:
#                     if sp>=1:
#                         print("pass is valid")
#                     else:
#                         print("pass must contaion atleast one special char")
#                 else:
#                     print("pass should not contain space")
#             else:
#                 print("pass must contain atleast one number")
#         else:
#             print("pass must contain atleast one lower case")
#     else:
#         print("pass must contain atleast one upper case")
# else:
#     print("pass must contain atleast 7 characters")

#WAPP to convert userinput to uppercase characters without using upper builtin method


# s=input("enter string")
# i=0
# l=[]
# while i<len(s):
#     if 97<=ord(s[i])<=122:
#         l.append(chr(ord(s[i])+32))
#     else:
#         l.append(s[i])
#     i+=1
# print("".join(l))

# s=input("enter string")
# a=input("enter the char")
# i=0
# count=0
# while i<len(s):
#     if s[i]==a:
#         count+=1
#     i+=1
# print(count)


# /reverse the string with out using built in and slicing

# s=input("enter a string")

# def reverse_words(text):
#     words = text.split()
#     reversed_words = [word[::-1] for word in words]
#     return ' '.join(reversed_words)

# # Example usage
# input_text = "My name is Ravi"
# output = reverse_words(input_text)
# print(output)  # Output: yM eman si ivaR


# s="hello world"
# l=s.split()
# i=0
# l1=[]
# while i<len(l):
#     l1.append(l[i][::-1])
#     l1.append(" ")
#     i+=1
# print(''.join(l1))

# to remove duplicates from the list
# l=[1,1,2,2,3,3,4,4]
# a=set(l)
# print(a)

# to remove duplicates from the list without typecasting to set
# l=[12,2,3,2,2,2,3,3,44,4,5,5,5]
# d=[]
# for i in l:
#     if i in d:
#         pass
#     else:
#         d.append(i)
# print(d)

# WAPT reverse a string without using indexing or sclicing

# s="ravi teja "
# res=" "
# for i in s:
#     res=i+res
# print(res)

# WAPT extract all the floating values from dictionary and perform addition on it
# print("to extract the floating values from dictionary and adding them")
# d={'a':12,'b':12.2,'c':12.23}
# a=list(d.values())
# sum=0.0
# for i in a:
#     if type(i)==float:
#        sum+=i
# print(sum)

# WAPT find the sum of all the even numbers present at odd index in the list
# l=[1,2,3,4,5,6,8,9,4,6,2]
# sum=0
# for i in range(len(l)):
#     if i%2==1:
#         if l[i]%2==0:
#           sum+=i
# print(sum)

# WAPT get the below output
# s="hi hello tommorow is mock so be prepared"
# op={'hi':2,'hello':5,'tommorow':8}



# i=0
# l=s.split()
# d={}
# while i<len(l):
#    d[l[i]]=len(l[i])
#    i+=1
# print(d)
   


# l=[1,2,3,4,4,4,5,6]
# index=0
# for i in l:
#    index = l.index(i)
#    print(index,i)
   # index+=1
   

# l=[1,2,3,4,4,4,5,6]
# index=0
# for i in l:
#    # index = l.index(i)
#    print(index,i)
#    index+=1

# # factiorial

# # a=int(input("enter number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i

# print(fact)

# WAP to merg 2 listrs without using addition operator

l1=[2,3,4,5]
l2=[2,34,4,3]
l=[]
for i in l1:
    l.append(i)
for j in l2:
    l.append(j)
print(l)