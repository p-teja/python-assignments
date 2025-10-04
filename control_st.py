'''a=input("enter val")
mid=len(a)//2
if (len(mid))%2==0:
    print("no mid")
else:
    print("mid id ",mid)


a=input("enter val")
if len(a)%2==1:
    print("mid val is:",a[len(a)//2])
else:
    print("no mid")

a=input("enter val")
b=reversed(a)
if a==b:
    print("pal")
else:
    print("not pal")



# if elif else 

a=234
if a==(type(int)):
    print("given char is integer type")
elif a==(type(float)):
    print("given char is float type")
elif a==(type(str)):
    print("given char is str type")
elif a==(type(list)):
    print("given char is list type")
elif a==(type(tuple)):
    print("given char is tuple type")
elif a==(type(set)):
    print("given char is set type")
else:
    print("char is nogthing")



for i in range(128):
    print(i, ":",chr(i))
'''

a=input("enter char")
l=[]
v=['a','e','i','o','u']
if a in  v:
    l.append(a)
    print(l)
else :
    print(ord(a))