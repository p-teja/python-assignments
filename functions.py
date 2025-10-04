# # def demo():
# #     print("hy welcome")

# # demo()

# # def intro(name,place,degree):
# #     print(f"myself {name} and lives in {place} had {degree}")
# # intro('ravi','hyd','btech')

# #1. positional arguments
# def sum(a,b,c):
#     print("a is ",a)
#     print("b is ",b)
#     print("c is ",c)
# #     return a+b+c
# # #passing arguments based on there position here a in 1 b in 2 c in 3
# # print(sum(10,20,30))


# # def intro(name,place,age):
# #     return f"my name is {name}, i'm from {place},i'm {age} years old"
# # print(intro("sree","mpl",22))
# # #my name is sree, i'm from mpl,im22 years old

# # print(intro('bnglr',12,'deepu'))
# # #my name is bnglr, i'm from 12,i'm deepu years old

# # #keyword args
# # print(intro(name='ravi',place='hyd',age=19))


# # # combination of positional and keyword arguments

# # print(sum(10,20,c=30))

# # area of triangle

# def area(**kwrgs):
#     d=kwrgs
#     return( 0.5*d['a']*d['b'])
# area(a=10,b=20)


# def right_triangle_area(**kwargs):
#     # kwargs may contain: base, height, hypotenuse
#     b = kwargs.get("base", 0)
#     h = kwargs.get("height", 0)
#     hyp = kwargs.get("hypotenuse", 0)
#     # if height not given, calculate using Pythagoras
#     h = h or (hyp**2 - b**2) ** 0.5
#     # if base not given, calculate using Pythagoras
#     b = b or (hyp**2 - h**2) ** 0.5
#     return 0.5 * b * h
# # Example usage
# print(right_triangle_area(base=6, height=8))       # 24.0
# print(right_triangle_area(base=6, hypotenuse=10))  # 24.0
# print(right_triangle_area(height=8, hypotenuse=10))# 24.0


# def rectangle_diagonal(**kwargs):
#     # Extract length and width from kwargs
#     length = kwargs.get("length", 0)
#     width = kwargs.get("width", 0)
    
#     # Calculate diagonal using Pythagoras theorem
#     diagonal = (length**2 + width**2) ** 0.5
#     return diagonal

# # Example usage
# print("Diagonal:", rectangle_diagonal(length=8, width=6))
# print("Diagonal:", rectangle_diagonal(length=12, width=5))


# def rectangle_diagonal(**kwargs):
#     # Only accept 'length' and 'width'
#     if "length" not in kwargs or "width" not in kwargs:
#         return "Error: Please provide both 'length' and 'width'."
    
#     if len(kwargs) > 2:
#         return "Error: Only 'length' and 'width' are allowed."
    
#     length = kwargs["length"]
#     width = kwargs["width"]

#     # Diagonal formula without math module
#     diagonal = (length**2 + width**2) ** 0.5
#     return diagonal

# # Example usage
# print("Diagonal:", rectangle_diagonal(length=8, width=6))       
# print("Diagonal:", rectangle_diagonal(length=12, width=5))     
# print(rectangle_diagonal(length=10))                           
# print(rectangle_diagonal(length=10, width=4, height=3))        




def temo(**kwargs):
    # Only accept 'celsius', 'fahrenheit', or 'kelvin'
    allowed_keys = {"celsius", "fahrenheit", "kelvin"}
    if not any(key in kwargs for key in allowed_keys):
        return "input in 'celsius', 'fahrenheit', or 'kelvin'."
    if len(kwargs) > 1:
        return "Error: Provide only one temperature value at a time."
    # Determine which unit was given
    if "celsius" in kwargs:
        c = kwargs["celsius"]
        f = (c * 9/5) + 32
        k = c + 273.15
    elif "fahrenheit" in kwargs:
        f = kwargs["fahrenheit"]
        c = (f - 32) * 5/9
        k = c + 273.15
    else:  # kelvin
        k = kwargs["kelvin"]
        c = k - 273.15
        f = (c * 9/5) + 32
    # Fever check (commonly > 37.5°C)
    feve= "Yes" if c > 37.5 else "No"
    return {
        "Celsius": round(c, 2),
        "Fahrenheit": round(f, 2),
        "Kelvin": round(k, 2),
        "Fever": feve
    }
# Example usage
print(temo(celsius=180))
print(temo(fahrenheit=100))
print(temo(kelvin=310))

#areaof tri
def area_tri(**kwrgs):
    d=kwrgs
    dc=d['bc']/2
    h=(d['ac']**2-dc**2)**0.5
    print(h)
    b=d['bc']
    area=0.5*h*b
    print(area)
area_tri(ac=5,bc=6,ab=2)
    

