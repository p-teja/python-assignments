# 1. Most repeated word in a string
# text = "apple orange apple banana apple orange banana"
# words = text.split()
# most = None
# count = 0

# for w in words:
#     c = 0
#     for x in words:
#         if w == x:
#             c += 1
#     if c > count:
#         count = c
#         most = w

# print("Most repeated word:", most)

# 2. Fibonacci series up to n terms
# n = 10
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# 3. Prime check
# num = 29
# prime = True
# for i in range(2, num):
#     if num % i == 0:
#         prime = False
#         break
# print("Prime" if prime and num > 1 else "Not Prime")

# 4. Armstrong numbers from 1 to 1000
# for num in range(1, 1001):
#     s = 0
#     n = num
#     k = len(str(num))
#     while n > 0:
#         d = n % 10
#         s += d ** k
#         n //= 10
#     if s == num:
#         print(num, end=" ")

# 5. Armstrong check
# num = 153
# s = 0
# n = num
# k = len(str(num))
# while n > 0:
#     d = n % 10
#     s += d ** k
#     n //= 10
# print("Armstrong" if s == num else "Not Armstrong")

# 6. Extract numbers from string and sum
# text = "ab12cd3e4"
# s = 0
# num = ""
# for ch in text:
#     if ch.isdigit():
#         num += ch
#     else:
#         if num != "":
#             s += int(num)
#             num = ""
# if num != "":
#     s += int(num)
# print("Sum:", s)

# 7. Series 2,22,222…
# n = 10
# num = ""
# for i in range(n):
#     num += "2"
#     print(num, end=" ")

# 8. Odd numbers at even index
# lst = [10, 11, 13, 20, 25, 30, 35]
# for i in range(0, len(lst), 2):
#     if lst[i] % 2 != 0:
#         print(lst[i], end=" ")

# 9. Remove duplicates in-place
# lst = [1, 2, 2, 3, 4, 4, 5]
# i = 0
# while i < len(lst):
#     j = i + 1
#     while j < len(lst):
#         if lst[i] == lst[j]:
#             lst.pop(j)
#         else:
#             j += 1
#     i += 1
# print(lst)

# 10. Separate positive & negative
# lst = [10, -2, 30, -45, 50, -7]
# pos, neg = [], []
# for x in lst:
#     if x >= 0:
#         pos.append(x)
#     else:
#         neg.append(x)
# print("Positive:", pos, "Negative:", neg)

# 11. Palindrome list
# lst = [1, 2, 3, 2, 1]
# print("Palindrome" if lst == lst[::-1] else "Not Palindrome")

# 12. Common elements of two sets (without &)
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# common = set()
# for i in a:
#     if i in b:
#         common.add(i)
# print("Common:", common)

# 13. Simulate set methods
# A = {1, 2, 3}
# B = {3, 4, 5}

# print("Union:", A | B)
# print("Difference:", A - B)
# print("Intersection:", A & B)
# print("Symmetric Difference:", A ^ B)

# A1, B1 = A.copy(), B.copy()
# A1 &= B1
# print("Intersection update:", A1)

# A2, B2 = A.copy(), B.copy()
# A2 -= B2
# print("Difference update:", A2)

# A3, B3 = A.copy(), B.copy()
# A3 ^= B3
# print("Symmetric Difference update:", A3)

# 14. Max & Min of tuple (without built-in)
# t = (5, 2, 9, 1, 7)
# mx = mn = t[0]
# for x in t:
#     if x > mx: mx = x
#     if x < mn: mn = x
# print("Max:", mx, "Min:", mn)

# 15. Length of collection without len()
# lst = [10, 20, 30, 40]
# count = 0
# for _ in lst:
#     count += 1
# print("Length:", count)

# 16. Spy number check (sum of digits = product of digits)
# num = 1124
# s, p, n = 0, 1, num
# while n > 0:
#     d = n % 10
#     s += d
#     p *= d
#     n //= 10
# print("Spy" if s == p else "Not Spy")

# 17. All spy numbers 1–1000
# for num in range(1, 1001):
#     s, p, n = 0, 1, num
#     while n > 0:
#         d = n % 10
#         s += d
#         p *= d
#         n //= 10
#     if s == p:
#         print(num, end=" ")

# 18. Neon number check (sum of digits of square = number)
# num = 9
# sq = num * num
# s = 0
# while sq > 0:
#     s += sq % 10
#     sq //= 10
# print("Neon" if s == num else "Not Neon")

# 19. Neon numbers 1–1000
# for num in range(1, 1001):
#     sq, s = num * num, 0
#     while sq > 0:
#         s += sq % 10
#         sq //= 10
#     if s == num:
#         print(num, end=" ")

# 20. Xylem number (sum of extreme digits = sum of mean digits)
# num = 12321
# s_mean = 0
# s_ext = 0
# n = str(num)
# s_ext = int(n[0]) + int(n[-1])
# for d in n[1:-1]:
#     s_mean += int(d)
# print("Xylem" if s_mean == s_ext else "Phloem")

# 21. Phloem check (opposite of Xylem)
# num = 1234
# s_mean = 0
# s_ext = 0
# n = str(num)
# s_ext = int(n[0]) + int(n[-1])
# for d in n[1:-1]:
#     s_mean += int(d)
# print("Phloem" if s_mean != s_ext else "Xylem")

# 22. Automorphic check (last digits of square = number)
# num = 25
# sq = num * num
# print("Automorphic" if str(sq).endswith(str(num)) else "Not Automorphic")

# 23. Happy numbers from 1–1000 (short for loop version)
# def is_happy(n):
#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         s = 0
#         while n > 0:
#             d = n % 10
#             s += d * d
#             n //= 10
#         n = s
#     return n == 1

# for i in range(1, 1001):
#     if is_happy(i):
#         print(i, end=" ")


# #For loop
# '''It is a looping statement which will exeute the statements repeatedly 
# In the case of for loop no need of initialization variables nor incremental both happens internally'''
# #Range
# # It is a function which will generates sequence of number between the specified numbers
# print(list(range(1,11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(1,100,10))) #[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]

# #write a program to print each and evry character present in the string using for
# s="samba siva"
# for i in s:
#     print(i)

# ##write a program to print all the key names in a given dictionary using for
# # Program to print all key names in a dictionary

# # Sample dictionary
# my_dict = {
#     "name": "siva",
#     "age": 22,
#     "city": "Hyderabad",
#     "profession": "Engineer"
# }
# for key in my_dict:
#     print(key)


# # Program to print all key names in a dictionary using while loop

# # Sample dictionary
# my_dict = {
#     "name": "siva",
#     "age": 22,
#     "city": "Hyderabad",
#     "profession": "Engineer"
# }

# # Convert keys into a list
# keys_list = list(my_dict.keys())
# i = 0

# while i < len(keys_list):
#     print(keys_list[i])
#     i += 1


# for i in range(2,100,2):
#     print(i)


# # Program to print the length of a collection using for loop

# my_list = [10, 20, 30, 40, 50]
# print(len(my_list))

# # Program to print the length of a collection using for loop

# my_list = [10, 20, 30, 40, 50]

# for _ in range(1):   # simple for loop, runs once
#     print("Length of the collection:", len(my_list))


# name = "Samba Siva"

# for i in range(5):   # loop runs 5 times (0 to 4)
#     print(name)


# #2. Print n natural numbers
# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print(i)

# #3. Multiplication table of a given number
# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")

# #4. Numbers divisible by 5 in range 1 to 100
# for i in range(1, 101):
#     if i % 5 == 0:
#         print(i)

# #5. Sum of n natural numbers
# n = int(input("Enter a number: "))
# total = 0

# for i in range(1, n+1):
#     total += i
# print(total)

# #6. Factorial of a number
# n = int(input("Enter a number: "))
# fact = 1

# for i in range(1, n+1):
#     fact *= i
# print(fact)

# #7. Extract all lowercase characters from a string
# s = input("Enter a string: ")
# result = ""

# for ch in s:
#     if ch.islower():
#         result += ch
# print(result)

# #8. Extract all special characters from a string
# s = input("Enter a string: ")
# result = ""

# for ch in s:
#     if not ch.isalnum():
#         result += ch
# print(result)

# #9. Sum of integers in a heterogeneous list
# l = [10, 2.5, 40, "hello", True, "sagar", 420, 84.0, 20+6j, -10]
# total = 0

# for item in l:
#     if type(item) == int:
#         total += item
# print(total)

# #10. Print tuple elements at even indexes
# t = (10, 2.5, 40, "hello", True, "sagar", 420, 84.0, 20+6j, -10)

# for i in range(0, len(t), 2):   # step = 2 for even indexes
#     print(t[i])

# #11. Extract characters from a string at odd indexes
# s = input("Enter a string: ")
# result = ""

# for i in range(1, len(s), 2):   # step = 2 for odd indexes
#     result += s[i]
# print("Characters at odd indexes:", result)

#to temove the duplicate elements from the list using for
# my_list = [10, 20, 30, 20, 40, 10, 50, 30]
# list = []
# for x in my_list: 
#     if x not in list: 
#         list.append(x)
# print(list)

#Without using for loop
# a = [10, 20, 30, 20, 40, 10, 50, 30]
# b = list(set(a))
# print(b)

#to reverse a string without using indexing or slicing using for
# s = "samba"
# str  = ""
# for i in s:        
#     str = i + str  
# print(str)


# data = {"a": 10, "b": 2.4, "c": 100, "d": 1.9, "e": 20.43}
# sum = 0
# for i in data.values():
#     if isinstance(i, float):
#         sum += i
# print(sum)
# l = [10, 22, 32, 43, 54, 65, 76, 87]
# sum = 0
# for i in range(len(l)):          
#     if i % 2 == 1:
#         if l[i] % 2 == 0 :
#             sum += l[i]
# print(sum)


# text = "hi hello tommorrow is mock so be prepared"
# words = text.split()  

# for i in words:
#     print(f"{i}:{len(i)}", end=", ")

# text = "hi hello tommorrow is mock so be prepared"
# for i  in text.split():
#     print(i, ":", len(i))


# text = "hi hello tommorrow is mock so be prepared"
# d = {}

# for i in text.split():
#     d[i] = len(i)

# print(d)

#Program to print index and element from a list
a = ["bike", "car", "jeep", "xl","bike","car"]
for i in range(len(a)):  
    print(i,a[i])

# # Program to print index and element without using len() or enumerate()
# a = ["bike", "car", "jeep", "xl","bike","car"]
# index=0
# for element in a:   
#     print(index,element)
#     index+=1
#write a program finding factorial of a number using for 
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
     fact *= i
print(fact)
#to merge of two list without using addition using for
# Program to merge two lists in a single for loop (without + operator)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
list = []
for i in (l1,l2):   
    for item in i:
        list.append(item)
print(list)

#arrange elements in a ascending order without using sort method using for

# Short program to arrange elements in ascending order without sort()
numbers = [5, 2, 9, 1, 7, 3]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("Ascending order:", numbers)
