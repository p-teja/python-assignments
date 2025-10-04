#logical operators

# int
print(0 and 5)      # 0
print(6 and 0)      # 0

# float
print(0.0 and 5.6)  # 0.0
print(8.9 and 0.0)  # 0.0

# complex
print(0j and (2+3j)) # 0j
print((2+3j) and 0j) # 0j

# string
print("" and "Hi")   # ''
print("Hello" and "")# ''

# list
print([] and [1,2])  # []
print([3,4] and [])  # []

# tuple
print(() and (1,2))  # ()
print((3,4) and ())  # ()

# set
print(set() and {1,2}) # set()
print({3,4} and set()) # set()

# dict
print({} and {"a":1})  # {}
print({"b":2} and {})  # {}

# bool
print(False and True)  # False
print(True and False)  # False



