# Function with no argument no return

# def msg():  # definition
#     print("hiii")
#     print("Helloooo")

# msg()   # Calling

# Function with argument and no return

# def add(a, b):
#     c = int(a) + int(b)
#     print("addition is : ", c)

# a, b = input().split()
# add(a, b)

# Function with no args and return

# def add():
#     a, b = input().split()
#     c = int(a) + int(b)
#     return c

# print(add())

# Function with argument and return

# def add(a, b):
#     return a + b

# print(add(92, 2))

# Function with default argument

# def fun(a, b, c):
#     add = a + b + c
#     print(add)

# def fun(a = 10, b = 20, c = 30):      # we have to either fill the default value from right to left .... either only c or c and b or c, b and a .... a and c will throw error ... or only a and only b will also throw error
#     print(a + b + c)

# fun(1, 2, 3)
# fun()

# Function with variable argument
# def fun(a):
#     print(a)

# fun(10)

# def fun(*a):
#     print(a)

# fun(10)
# fun(10, 20)
# fun(10, 20, 30)
# fun(1, "abc", 95.6)

# def fun(*a, b, c):
#     print(a)
#     print(b)
#     print(c)

# fun(10, 20, 30, 40, 50) # Error for b and c due to *a

# def fun(a, b, *c):
#     print(a)
#     print(b)
#     print(c)

# fun(10, 20, 30, 40, 50)

# *a, b, c = 10, 20, 30, 40, 50 # inside function is a tuple is returned and outside the function a list is returned
# print(a)
# print(b)
# print(c)

# a, b, *c = 10, 20, 30, 40, 50 # inside function is a tuple is returned and outside the function a list is returned
# print(a)
# print(b)
# print(c)

# keyword only argument function

# def fun(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# fun(c = 45, a = 23, b = 21)
# fun(c = 45, a = 23, b = 21)

# import sys
# i = sys.stdin.read().split()

# if i:
#     n = int(i[0])
#     s = sum(int(x) for x in i[1: n + 1])
#     print(s)
