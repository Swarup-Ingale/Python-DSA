
# a = 10
# print(a)

# print(type(a))


# # Floating Point

# x = 10.09
# print(x)
# print(type(x))

# b = 2e3 # Also Float = 2 X 10**3
# print(b)
# print(type(b))

# # Complex Numbers

# c = 3 + 4j
# print(c)
# print(type(c))
# print(type(c.real))
# print(type(c.imag))
# print(c.conjugate)

# # String -> Immutable

# d = "Hello Everyone"
# print(type(d))
# print(d)

# e = 'a'
# print(type(e))
# print(e)

# f = 'hello'
# print(f)
# print(id(f))
# f = f + "everyone"
# print(f)
# print(id(f))

# # List

# g = [1, 2, 4, 5]
# print(g)
# print(type(g))

# # Tuple
# h = (1, 2, 3, 4)
# print(h)
# print(type(h))

# # Range
# i = range(1,5)
# print(i)
# print(type(i))

# # Nesting
# j = list(range(1,5))
# print(j)
# print(type(j))

# # Set

# k = {}
# print(type(k))

# l = {1,2,4,4}
# print(l)
# print(type(l))

# m = set()

# # Frozen Set - > Immutable version of Set
# n = frozenset({1,2,3,4,4,5})
# print(n)
# print(type(n))

# # Boolean
# o = False
# p = "True"

# print(f"{o} {p}")
# print(type(o))
# print(type(p))

# # Binary
# q = b"hello"
# print(q)
# print(type(q))

# data = bytes([65, 66, 67, 68])
# print(data)
# print(type(data))

# data1 = bytearray([65, 66, 67, 68])
# print(data1)
# print(data1[0])
# print(type(data1))

# # NONE
# r = None
# print(r)
# print(type(r))

# # Keywords

# import keyword

# print(keyword.kwlist)
# print(len(keyword.kwlist))

# # Code Maxing

# t = 10
# u = 20
# print(t, u)
# print(t, end=">>")
# print(u)

# v = 10, 20, 30j
# print(v)

# #w, x = 10, 20, 30
# #print(w)
# #print(x)

# w = (10, 20, 30)
# x, y, z = w
# print(w)
# print(x)
# print(y)
# print(z)

# # Input
# ab = input("enter a: ")
# ac = input("enter b: ")
# ad = ab + ac
# print(ad)

# ae = int(input("enter a: "))
# af = int(input("enter b: "))
# ag = ae + af
# print(ag)
# print("output: " + str(ag))

# # Narrowing Conversion

# ah = 10.5
# ai = int(ah)
# print(ah)
# print(ai)

# # Widening Conversion

# aj = 10.5
# ak = int(ah)
# print(aj)
# print(ak)

# Double Input Function
# a, b = int(input("enter a: ")), int(input("enter b: "))
# print(a)
# print(b)
# c = a + b
# print(c)

# Single Input Function
# a, b = input("enter a and b : ").split(";")
# c = int(a) + int(b)
# print(a)
# print(b)
# print(c)

# F-String
# a = 10
# print(f"{a}")
