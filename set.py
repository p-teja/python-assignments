#in set memory allocation changes line to line.
t={0.2,-5.6,6.9}
print(type(t))#<class 'set'>

print(dir(set()))#['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

#default value of set
print(set())#set()

s={}
print(type(s))#<class 'dict'> it give dict value because it dict class aso use {}.

#
s={True,False,0,1}
print(s)#it only gives 0 as false and 1 as true dont give boolen value as output.



#union (method)
s={1,2,3,4,5}
s1={3,4,5,6,7,8}
s2={7,8,9,0}
print(s.union(s1))#{1, 2, 3, 4, 5, 6, 7, 8}
print(s1.union(s2))#{0, 3, 4, 5, 6, 7, 8, 9}
print(s.union(s1.union(s2)))#{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

str="biryani"
print(s.union(str))#{1, 2, 3, 4, 5, 'b', 'i', 'a', 'y', 'r', 'n'} it is unorderd data type and it display unique

# intersection method

print(s.intersection(s1))


# difference

print(s.difference(s1))

'''# symmetric difference

print(s.symmetric_difference(s1))

# intersection update

print(s1.intersection_update(s))
print(s1)'''

#2/8
#symmetric_difference:
#it returns the non common elements from both the sets
str="biryani"
s={1,2,3,4,5}
s1={3,4,5,6,7,8}
s2={7,8,9,0}
print(s.symmetric_difference(s1))#{1, 2, 6, 7, 8} it prints only unique no common elements
#print(s.symmetric_difference(s1,s1))#set.symmetric_difference() takes exactly one argument (2 given)

######### for updation in string
s={1,2,3,4,5}
s1={3,4,5,6,7,8}
s2={7,8,9,0}
s.intersection_update(s1)#it update intersection values into base set 
#like it just update values which are common values into the s from s and s1
print(s)#{3, 4, 5} #now this the base set values it updated from intersection

s.intersection_update(str)
print(s)#set()


#difference_update
# str="biryani"
s={1,2,3,4,5}#{3, 4, 5} from above
s1={3,4,5,6,7,8,0}
s2={7,8,9,0}
print(s)#{1, 2, 3, 4, 5}
s.difference_update(s1)#{1, 2} it acts as subration it display from set1 and it update that value in it
print(s)#{1, 2}
s1.difference_update(s2)
print(s1)#{3, 4, 5, 6}
'''
print(s1.difference_update(s2.union(s))
{3,4,5,6,7,8,0} {7,8,9,0} union{1,2}
{3,4,5,6,7,8,0} {7,8,9,0,1,2}
{3,4,5,6}
'''

s={1,2,3,4,5}
s1={3,4,5,6,7,8,0}
s2={7,7,8,9,0}
#s1.difference_update(s.intersection_update(s1))
#print(s1)#'NoneType' object is not iterable: we can use only one update method in one condition



#s
s.symmetric_difference_update(s1)
print(s)#{0, 1, 2, 6, 7, 8} it update difference values from both sets and updated to base set


#s={0, 1, 2, 6, 7, 8} because it waas updated on top
s2.symmetric_difference_update(s.symmetric_difference(s1))
print(s2)#{0, 1, 2, 3, 4, 5, 7, 8, 9}

'''
{7,7,8,9,0} symmetric_difference_update {0, 1, 2, 6, 7, 8} symmetric_difference {3,4,5,6,7,8,0}
{7,7,8,9,0} symmetric_difference_update  {1,2,3,4,5}
            print(s2) {0,1,2,3,4,5,7,8,9}
'''


