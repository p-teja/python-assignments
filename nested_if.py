'''un=input("enter uname")
ps=input("enter pass")
if (un=="raviteja"):
    if (ps=="ravi123"):
        print("login successful")
    else:
        print("pass is incorrect")

else:
    print("user is incorrect")


# take 6 marks inputs from students and cal avg marks of a student ...check for avg marks obtained from the student and classify them of distinction and test pass and fail.....
sub1=int(input("enter marks"))
sub2=int(input("enter marks"))
sub3=int(input("enter marks"))
sub4=int(input("enter marks"))
sub5=int(input("enter marks"))
sub6=int(input("enter marks"))
avg=(sub1+sub2+sub3+sub4+sub5+sub6)/6
print(avg)

if (avg)<(sub1 or sub2 or sub3 or sub4 or sub5  or sub6):
    print("distinction")
else:
    print("average student")

# WAPT print the middle value from a give heterogenious tuple only if the middle value is a string and has even characters 

#a=(10,20,0j,'hello',True,False,['hi'])
#b=(10,20,0j,'hell',True,False,['hi'])


# write a program to print a middle value from a hetrogenous tuple only if the middle 
# is a string and has even character
a=(10,20,0j,"hello",True,False,['hi'])
#a=(10,20,0j,"hell",True,False,['hi'])
b=len(a)//2
c=a[b]
if isinstance (c,str):
    if len(c)%2==0:
        print(c) #if string length is in even number
    else:
        print("string is odd") # if string length is in odd number
else:
    print("not a str in middle char") # if string is not present in middle of tuple


    #WAPTC the greatest of four numbers

     

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
d = int(input("Enter fourth number"))

if a > b:
    if a > c:
        if a > d:
            print("Greatest number is:", a)
        else:
            print("Greatest number is:",d)
    else:
        if c > d:
            print("Greatest number is:",c)
        else:
            print("Greatest number is:", d)
else:
    if b > c:
        if b > d:
            print("Greatest number is:", b)
        else:
            print("Greatest number is:", d)
    else:
        if c > d:
            print("Greatest number is:", c)
        else:
            print("Greatest number is:", d)


#write a program to check second greatest numner among the four
a1 = int(input("Enter first number"))
b1= int(input("Enter second number"))
c1= int(input("Enter third number"))
d1= int(input("Enter fourth number"))
if (a1>b1 and a1>c1 and a1>d1):
    if (b1>c1 and b1>d1):
        print("b is 2nd greatest")
    elif(c1>d1 and c1>b1):
        print("c is 2nd greater")
    elif(d1>b1 and d1>c1):
        print("d is 2nd greatest")
    else:
        print("2 numbers are equal")

elif(b1>a1 and b1>c1 and b1>d1):
    if (a1>c1 and a1>d1):
        print("b is 2nd greatest")
    elif(c1>d1 and c1>a1):
        print("c is 2nd greater")
    elif(d1>b1 and d1>c1):
        print("d is 2nd greatest")
    else:
        print("2 numbers are equal")

elif(a1>b1 and a1>c1 and a1>d1):
    if (b1>c1 and b1>d1):
        print("b is 2nd greatest")
    elif(c1>d1 and c1>b1):
        print("c is 2nd greater")
    elif(d1>b1 and d1>c1):
        print("d is 2nd greatest")
    else:
        print("2 numbers are equal")

elif(a1>b1 and a1>c1 and a1>d1):
    if (b1>c1 and b1>d1):
        print("b is 2nd greatest")
    elif(c1>d1 and c1>b1):
        print("c is 2nd greater")
    elif(d1>b1 and d1>c1):
        print("d is 2nd greatest")
    else:
        print("2 numbers are equal")




#write a program to check second greatest number among the four
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
# Find the greatest
if a >= b and a >= c and a >= d:
    greatest = a
elif b >= a and b >= c and b >= d:
    greatest = b
elif c >= a and c >= b and c >= d:
    greatest = c
else:
    greatest = d
# Now find the second greatest (among remaining three)
if greatest == a:
    second = max(b, c, d)
elif greatest == b:
    second = max(a, c, d)
elif greatest == c:
    second = max(a, b, d)
else:
    second = max(a, b, c)
print("Greatest number is:", greatest)
print("Second greatest number is:", second)

#2nd
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
# Assume first two as greatest and second
if a > b:
    greatest = a
    second = b
else:
    greatest = b
    second = a
# Check c
if c > greatest:
    second = greatest
    greatest = c
elif c > second:
    second = c
# Check d
if d > greatest:
    second = greatest
    greatest = d
elif d > second:
    second = d

print("Greatest number is:", greatest)
print("Second greatest number is:", second)

#3rd

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# Step 1: Find the greatest
if a >= b and a >= c and a >= d:
    greatest = a
elif b >= a and b >= c and b >= d:
    greatest = b
elif c >= a and c >= b and c >= d:
    greatest = c
else:
    greatest = d
# Step 2: Find the second greatest among remaining 3
if greatest == a:
    if b >= c and b >= d:
        second = b
    elif c >= b and c >= d:
        second = c
    else:
        second = d
elif greatest == b:
    if a >= c and a >= d:
        second = a
    elif c >= a and c >= d:
        second = c
    else:
        second = d
elif greatest == c:
    if a >= b and a >= d:
        second = a
    elif b >= a and b >= d:
        second = b
    else:
        second = d
else:  #greatest == d
    if a >= b and a >= c:
        second = a
    elif b >= a and b >= c:
        second = b
    else:
        second = c
print("Greatest number is:", greatest)
print("Second greatest number is:", second)





l=[]
l.append(a)
l.append(b)
l.append(c)
l.append(d)

print(l.sort(reverse=True))
print(l[1])'''



#write a program to smallest among three numbers with list method and if/else
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a <= b and a <= c:
#     smallest = a
# elif b <= a and b <= c:
#     smallest = b
# else:
#     smallest = c
# print("The smallest number is:", smallest)
# #or
# l=[]
# l.append(a)
# l.append(b)
# l.append(c)
# l.sort()
# print(l[0])


#find the second smallest number among the four numbers 

# Step 1: Find the smallest
a=int(input("enter a value"))
b=int(input("enter a value"))

c=int(input("enter a value"))

d=int(input("enter a value"))

if a <= b and a <= c and a <= d:
    smallest = a
elif b <= a and b <= c and b <= d:
    smallest = b
elif c <= a and c <= b and c <= d:
    smallest = c
else:
    smallest = d

# Step 2: Find the second smallest among remaining 3
if smallest == a:
    if b <= c and b <= d:
        second_smallest = b
    elif c <= b and c <= d:
        second_smallest = c
    else:
        second_smallest = d
elif smallest == b:
    if a <= c and a <= d:
        second_smallest = a
    elif c <= a and c <= d:
        second_smallest = c
    else:
        second_smallest = d
elif smallest == c:
    if a <= b and a <= d:
        second_smallest = a
    elif b <= a and b <= d:
        second_smallest = b
    else:
        second_smallest = d
else:  # smallest == d
    if a <= b and a <= c:
        second_smallest = a
    elif b <= a and b <= c:
        second_smallest = b
    else:
        second_smallest = c

print("Smallest number is:", smallest)
print("Second smallest number is:", second_smallest)
