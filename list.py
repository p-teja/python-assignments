#list 
#list is a collection of elements both homogenous and hetrogenous of data and seperated by , .
#list is an ordered data type it is mutable in nature.
#it supports dupliactes the boundaries are [] square braces and they also called as open boundaries.

#examples for homogenous
[1,2,3,4,5,6]#the list consists of integer values
['hi','hello']#the list consists of string values
[10+3j,2-4j,4+1j]#the list consists of complex values

#examples for hetrogenous
[10,4.6,30-3j,False] # #the list consists of multiple datatype values

l=[1,2,3,4,5,6]
print(type(l))#<class 'list'>




#second way


l=[1,2,3,4,5]
print(type(l)) #<class 'list'>

l1=list((1,2,3,4,4,5))
print(l1) #[1, 2, 3, 4, 4, 5]

print(dir(list))

# indexing in list

l2=[1,2,3,4,5,6]
print(l2[3])
l3=['apple','pineapple','strawberry','kiwi','avacado','cherry']
print(l3[-3])
print(l3[-5] [4:])


l4=[3,[3],23,45,[34],44,54]
print(l4)

l5=[1,2,3,45,[200.43,'pineapple',[1,2,['hello','world'],3,4,5],'cherry'],6,['iphone','samsung','blackberry'],8,1.0]
print(l5[4][2][2][0], end=" ")
print(l5[4][2][2][1])


#METHODS # INDEX
l6=[1,2,3,3,3,34,5]
print(l6.index(3))
print(l6.count(3))

#modification 

a=['ravi','teja']
print(a[1].title())

#2/8
l=[1,2,3,45,[200.43,'pineapple',[1,2,['hello','world'],3,4,5],'cherry'],6,['iphone','samsung','blackberry'],8,1.0]

print(l[4][2][2][0],end=" ")  # hello. end=" "(to come in same line hello world)
print(l[4][2][2][1])  # world print list in list 

print((l[4][::3]))#[200.43, 'cherry']
print(len(l[4][::3]))#2

#methods
#index()

l=[1,2,3,4,5,6]
print(l.index(3))#2

l=['apple','mango','grapes','cherry','banana','orange','banana','orange']
print(l.index('mango'))#1
print(l.index('orange',3))#5 

#print(l.index('hi'))#'hi' is not in list

#print(l.rindex('apple'))
#list' object has no attribute 'rindex'. Did you mean: 'index'?

#count
#to check dulicates
print(l.count('orange'))#2 repeted values


#Modification

l=['google','amazon','microsoft','telsa','spacex','Tata','wipro']
print(l)#['google', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro']
l[0]='hi'#['hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro']
l[-2]='TCS'
print(l[1].title())#Amazon

#adding elements to the list
#it is the method tha can add data in both single and multi value type data the elements will be at the end of list
print(len(l))
#l[8]="oracle"
#print(l)#list assignment index out of range


# for this to add the list we have methods
#SYNTAX: list_var.append(Single value datatype and multi value datatype)
# 1. append
l.append("oracle")
print(l)#['hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle']
l.append(10+2j)
print(l)#['hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle', (10+2j)]
#l.append(1,23,3,4,45)
#print(l)#list.append() takes exactly one argument (5 given)

l.append([1,23,3,4,45])
print(l)#['hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle', (10+2j), [1, 23, 3, 4, 45]]
#l.append()
#print(l)
#list.append() takes exactly one argument (0 given)

#2. extend()
#Syntax: list_var.extend(iterable) #iterable: collection of multiple element
#l.extend(10)
#print(l)#'int' object is not iterable
l.extend("sree")
print(l)#['hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle', (10+2j), 
#[1, 23, 3, 4, 45], 's', 'r', 'e', 'e'] #

#l.extend(10,12,23,32)
#print(l)#list.extend() takes exactly one argument (4 given)

l.extend((10,12,23,32))
print(l)#['hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle', (10+2j),
# [1, 23, 3, 4, 45], 's', 'r', 'e', 'e', 10, 12, 23, 32]# in same list it stores

l.extend("10122332")
print(l)#['hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle', (10+2j), [1, 23, 3, 4, 45], 's', 'r', 'e', 'e', 10, 12, 23, 32,
# '1', '0', '1', '2', '2', '3', '3', '2']

#up and both are same output

l.extend("10 12 23 32")
print(l)#['hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle', (10+2j), [1, 23, 3, 4, 45], 's', 'r', 'e', 'e', 10, 12, 23, 32,
# '1', '0', '1', '2', '2', '3', '3', '2']

l.extend(["sree","deepu"])
print(l)# 'sree', 'deepu']

#3. insert method(addition)
#insert a element to a list at what position we want to add
#it take to arguments 
#SYNTAX: list_var.insert(position value)
l.insert(0,"testyantra")
print(l)#['testyantra', 'hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle', (10+2j), [1, 23, 3, 4, 45], 's', 'r', 'e', 'e', 10, 12, 23, 32, '1', '0', '1', '2', '2', '3', '3', '2', '1', '0', ' ', '1', '2', ' ', '2', '3', ' ', '3', '2', 'sree', 'deepu']

l=[]
l.append("instagram")
l.append("X")
l.append("snap")
l.extend(["facebook","omegle","telegram"])
print(l)#['instagram', 'X', 'snap', 'facebook', 'omegle', 'telegram']

l.insert(10,"linkedin")
print(l)#['instagram', 'X', 'snap', 'facebook', 'omegle', 'telegram', 'linkedin'] it has more but it add at last

l.insert(10,"linkedin")
print(l)

l.insert(-4,"sharechat")
print(l)#['instagram', 'X', 'snap', 'facebook', 'sharechat', 'omegle', 'telegram', 'linkedin', 'linkedin']

#l.insert(10)
#print(l)# insert expected 2 arguments, got 1


#removal methods
 
# 1.pop()
# 2.remove()
# 3.clear()

#removal methods
#1. pop():for specific position
#2. remove()
#3. clear()

l1=['hi', 'amazon', 'microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle', (10+2j), [1, 23, 3, 4, 45], 's', 'r', 'e', 'e', 10, 12, 23, 32,
 '1', '0', '1', '2', '2', '3', '3', '2']
print(l1.pop())#2 if we don't specify any value then it delete the last one

print(l1.pop(10))#s

print(l1.pop(1))#amazon
l1.pop(0)# remove o position value 
print(l1)
#['microsoft', 'telsa', 'spacex', 'TCS', 'wipro', 'oracle', (10+2j), [1, 23, 3, 4, 45],
#  'r', 'e', 'e', 10, 12, 23, 32, '1', '0', '1', '2', '2', '3', '3']




a = [11, 22, 33, 44, 55]                # [11, 22, 33, 44, 55]
a.append(66)                            # [11, 22, 33, 44, 55, 66]
a[2] = 333                              # [11, 22, 333, 44, 55, 66]
print(a.index(44))                      # 3
a.insert(1, 999)                        # [11, 999, 22, 333, 44, 55, 66]
a.remove(11)                            # [999, 22, 333, 44, 55, 66]
print(a.count(22))                      # 1
a.pop()                                 # [999, 22, 333, 44, 55]

b = [0.5, 1.5, -2.5, 3.5, 4.5]          # [0.5, 1.5, -2.5, 3.5, 4.5]
b.extend([5.5, 6.5])                    # [0.5, 1.5, -2.5, 3.5, 4.5, 5.5, 6.5]
b[0] = 7.5                              # [7.5, 1.5, -2.5, 3.5, 4.5, 5.5, 6.5]
print(b.index(4.5))                     # 4
b.append(3.5)                           # [7.5, 1.5, -2.5, 3.5, 4.5, 5.5, 6.5, 3.5]
b.pop(3)                                # [7.5, 1.5, -2.5, 4.5, 5.5, 6.5, 3.5]
b.remove(5.5)                           # [7.5, 1.5, -2.5, 4.5, 6.5, 3.5]
print(b.count(3.5))                     # 1

c = ['Lion', 'Tiger', 'Leopard', 'Panther', 'Cheetah',
     'Jaguar', 'Puma', 'Cougar', 'Lynx', 'Ocelot']  # original list
c.insert(2, 'Caracal')                 # insert at index 2
c.remove('Tiger')                      # remove 'Tiger'
print(c.index('Puma'))                 # 5
c[5] = 'Serval'                        # replace index 5
c.append('Bobcat')                     # append at end
print(c.count('Leopard'))             # 1
c.pop()                                # remove 'Bobcat'

d = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon',
     'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa']         # original list
d.extend(['Lambda', 'Mu'])            # add two more
d.remove('Theta')                     # remove 'Theta'
d[0] = 'Omega'                        # change 'Alpha' to 'Omega'
print(d.count('Gamma'))              # 1
d.append('Nu')                        # append 'Nu'
d.insert(5, 'Xi')                     # insert at index 5
d.pop(3)                              # remove 'Delta'

e = ['rose', 'lily', 'jasmine', 'tulip']  # original
e.append('sunflower')                   # add 'sunflower'
e.remove('lily')                        # remove 'lily'
e[2] = 'daffodil'                       # change 'tulip' to 'daffodil'
e.insert(1, 'marigold')                 # insert 'marigold'
print(e.index('marigold'))             # 1
e.extend(['orchid', 'lavender'])       # add two more
e.pop()                                # remove 'lavender'

f = ['Ant', 'Bee', 'Cat', 'Dog', 'Elephant',
     'Fox', 'Goat', 'Horse', 'Iguana', 'Jackal']     # original
f.remove('Dog')                         # remove 'Dog'
f.append('Kangaroo')                    # append 'Kangaroo'
f.insert(0, 'Aardvark')                 # insert at beginning
print(f.index('Jackal'))               # 10
f[3] = 'Cheetah'                        # change 'Cat' to 'Cheetah'
f.extend(['Llama'])                     # add 'Llama'
print(f.count('Ant'))                  # 1
f.pop(2)                                # remove 'Bee'

g = [9, 'ten', 11.0, True, False]       # original
g.append(None)                         # add None
g[1] = 'eleven'                        # change 'ten' to 'eleven'
g.insert(2, 10.5)                      # insert 10.5
print(g.count(9))                      # 1
g.remove(False)                        # remove False
g.extend(['done'])                    # add 'done'
g.pop()                               # remove 'done'

h = [1+2j, 5, 4.4, 2+0j, -3.3, 7, 0+6j, 6.6, 9, 3.3+0.7j]  # original
h.append(11.11)                        # add 11.11
h.remove(5)                            # remove 5
h[4] = 2+2j                            # change -3.3 to 2+2j
h.insert(1, 13)                        # insert 13
print(h.count(4.4))                    # 1
print(h.index(6.6))                    # 7
h.pop()                                # remove last

i = [150, 140, 130, 120, 110]          # original
i.append(100)                         # add 100
i.insert(0, 160)                      # insert at beginning
i[2] = 135                            # change 140 to 135
print(i.index(110))                  # 5
print(i.count(150))                  # 1
i.extend([90, 80])                   # add two more
i.pop(1)                             # remove 140

j = ['Jan', 'Feb', 'Mar', 'Apr', 'May']    # original
j.append('Jun')                        # add 'Jun'
j.insert(3, 'Jul')                     # insert 'Jul'
j.remove('Jan')                        # remove 'Jan'
j[4] = 'Vacation'                      # change 'May' to 'Vacation'
print(j.index('Jul'))                 # 3
j.extend(['Work'])                    # add 'Work'
j.pop()                               # remove 'Work'
print(j.count('May'))                 # 0


#sort

l=[1,2,3,4,5,56,4,34,]
l.sort()
print(l)


l=['ravi','teja','apple']
l.sort()
print(l)

#key 

l=['ravi','teja','apple']
l.sort(key=len)
print(l)

# reverse=true
l=['ravi','teja','apple']
l.sort( reverse=True)
print(l)

# reverse
l=[1,2,34,2,34,5,4,3,4,5,4]
l.reverse()
print(l)

# this is a list 
