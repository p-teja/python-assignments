t=(1,2,3,4,3,3,3,4)
print(t)
print(type(t))

t=(20,3.5,20+2j,30-3j,9.8,"hi",True)
print(t[4])    #9.8
 
print(t[3])       #(30-3j)

print(t[2:4])
print(t[1:5])

# ARTHAMETIC OPERATIONS

t1=(1,2,3,4,4)
t2=(32,3,4,3,4)
print(t1+t2)  #it merges the tuple

#print(t1-t2)   #TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'

#print(t1*t2)   # not possible

#print(t1/t2)   # not possible

#print(t1//t2)   # not possible

#print(t1%t2)   # not possible

print(dir(tuple))
#  ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


# index 
print(t.index(9.8))

# count

print(t.count(9.8))

print(tuple())

# adding ele to set 
# add()  #update()
s=set()
s.add("ravi teja")
print(s)
s.add(10)
s.add(20+3j)
s.add((1,2,3,4))
print(s)


#removal methods
#set is unordered type
#1:remove it is going to remove specified element at a time it will remove only one element
s={1, 2, 3, (10, 20, 30, 9.6), 39, 9.6, 10, 'r', 's', 50, 20, 'e', 23, 30}
print(s.remove(10))
print(s)#{1, 2, 3, (10, 20, 30, 9.6), 39, 9.6, 'r', 's', 50, 20, 'e', 23, 30} unordered

#print(s.remove(10))
#print(s)#KeyError: 10                      10 is not present in that list

#print(s.remove())
#print(s)#set.remove() takes exactly one argument (0 given)          it not given any element

#print(s.remove(23,30))
#print(s)# set.remove() takes exactly one argument (2 given)     it will take only one element at a time

#discard
#if element not in list it won't give any error compared to remove
s=set()
s.add((10,20,30,40))
print(s)#{(10, 20, 30, 40)}
s.add("hello")
s.update("fruit")
print(s)#{'hello', 'f', (10, 20, 30, 40), 't', 'r', 'i', 'u'}

s.add(10)
s.add(2)
s.add(3)
s.add(40)


#s.discard(10,20,30)#set.discard() takes exactly one argument (3 given)
s.discard((10,20,30,40))
print(s)#{'hello', 2, 3, 40, 10, 'f', 'u', 'r', 't', 'i'} 
print(len(s))#10
s.discard(10)
print(s)# it won't display anything
s.discard('t')
print(s)#{'u', 2, 3, 40, 'hello', 'f', 'i', 'r'}

print(len(s))#8

# pop
s.pop()
print(s)
print(s.pop())