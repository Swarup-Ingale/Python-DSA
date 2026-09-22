# l = []
# print(type(l))

# l1 = list()
# print(type(l1))

# l2 = [1, "hello", 1.3, [1,2], {2,3,4}, True, False, None, (4,5)]
# print(l2)

# l3 = [1, 2, 3]
# l3.append(56)
# print(l3)

# l4 = [10, 20, 30, 40, 50]
# print(l4[3])
# print(l4[:4:])

# l4 = [10, 20, 30, 40, 50, 60, 70, 80]
# print(l4[3])
# print(l4[1:])
# print(l4[::-1])
# print(l4[0:-1:3])
# print(l4[7:0])
# l4 = l4[::-1]
# print(l4)

# l = [1, 2, 3, 4, 5]
# l.append(12)
# l.insert(2, 14)
# print(l)
# l.pop()
# print(l.pop())  # Delete last element
# print(l.remove(4)) # Delete by value
# print(l.pop(1)) # Delete by index
# del l[3]    # Deletes by index

# l1 = [10, 20, 30]
# l2 = [100, 200]

# l1.extend(l2)   # concatenate
# l1 += l2
# print(l1)

# l1.append(l2)   # Append the entire list
# print(l1)

# l = [1, 2, 3, 4, 3, 3, 3, 5, 3]
# print(l.count(3))
# print(l.index(3))
# print(l.index(3, 3))
# print(l.index(3, 3))

# l = [1, 2, 3, 4, 3, 3, 3, 5, 3]
# l.clear()
# print(l)

# l = [1, 10, 45, 25, 15]
# l.sort()
# print(l)
# l.sort(reverse = True)
# print(l)

# l = [1, 10, 45, 25, 15]
# l.reverse()
# print(l)
# print(l[0])

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in l:   # used when value is pointed
#     print(i, end=" ")

# for i in range(len(l) - 1, -1 , -1):  # used when index is pointed
#     print(l[i], end=" ")

# l = [45, 22, 57, 8, 2, 14, 76]
# l.sort()
# print(l)
# print(f"min is : {l[0]} and max is : {l[len(l) - 1]}")

# min max

# l = [45, 22, 57, 8, 2, 14, 76]
# a = len(l)
# max = l[0]
# min = l[0]
# for i in range(a):
#     # max = b
#     if max < l[i]:
#         max = l[i]
# print(max)

# for i in range(a):
#     if min > l[i]:
#         min = l[i]
# print(min)
# l = [1, 2, 5, 4, 7, 6]
# print(sorted(l)) # Temporary sorting
# print(sorted(l, reverse = True))

# TUPLE
# t = (10)    # individual value is considered as int
# print(type(t))
# t = (10,15)
# print(type(t))

# t = (1, 2, 3.44, True, False, {2, 1}, "hello", [1, 2], (1, 20), {3, 4})
# print(t)
# print(type(t)) 

# t = (1, 2, 3, 4, 5, 6)
# print(t[0])

# t = (1, 2, 3, 4, 5, 5, 5, 6, 7, 1, 2)
# print(t)
# print(type(t))

# t = (1, 2, 3)
# print(t)
# print(id(t))
# t += (4, 5)
# print(t)
# print(id(t))

# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(t.index(3))
# print(t.index(3, 4))
# print(t.index(3, 4, 7))

# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(sorted(t)) # Temporary sorting and converted in list for printing

# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(max(t))
# print(min(t))
# print(len(t))

# TUPLE UNPACKING
# x = (10, 20, 30)
# p, q, r = x
# print(p)
# print(q)
# print(r)

# SET

# s ={}
# print(type(s))

# i = set()
# print(type(i))

# s = {3, 4, 4.5 , 4, 4, "hii", (500, 400), True, False}
# print(s)

# s = {1, 2, 3, 4, 5}
# s.clear()
# print(s)

# s = {1, 2, 3, 4, 5}
# s.add(12)
# print(s)
# s.remove(3)
# print(s)
# print(s.pop())

# s = {1,3,2,5,4,7,6}
# print(sorted(s))

# s1 = {1, 2, 3}
# s2 = {2, 3, 4, 5}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))

# s = {1, 2, 3, 4, 5, 6}
# s.discard(2)    # delete data by value without parsing the key error
# print(s)
# s.remove(3)     # deletes data by value with parsing the key error
# print(s)

# Dictionary

# d = {}
# print(type(d))

# m = dict()
# print(type(m))

# student = {
#     "roll" : 1,
#     "name" : "Swarup",
#     "city" : "Mumbai",
#     "age" : 19
# }

# print(student)
# student["subject"] = ["Mathematics", "English", "Marathi"]
# student["gender"] = "M"
# print(student)

# print(student)
# student["subject"] = {"s1" : "Mathematics", "s2" : "English", "s3" : "Marathi"}
# student["gender"] = "M"
# print(student)

# print(student)
# student["roll"] = 9
# student["name"] = "Ingale"
# print(student)

# if "name" in student.keys():
#     print(True)
# else:
#     print(False)

# if "Swarup" in student.values():
#     print(True)
# else:
#     print(False)

# if student["name"] in student:
#     print(True)
# else:
#     print(False)

# if student["name"] in student.values():
#     print(True)
# else:
#     print(False)

# for i in student:
#     print(i)

# for i in student.keys():
#     print(i)

# for i in student.values():
#     print(i)

# for i in student.items():
#     print(i)

# for i,j in student.items():
#     print(i, j)

# for i in student:
#     print(i, student[i])

# x ={"gender": "M", "roll": 34}
# student.update(x)
# print(student)

# student.pop("age")
# print(student)

# x = student.popitem()
# print(student)
# print(x)

# x, y = student.popitem()
# print(student)
# print(x, y)

# student = {
#     "roll" : 1,
#     "name" : "Swarup",
#     "city" : "Mumbai",
#     "age" : 19
# }

# s = student.copy()
# print(s)
# student.clear()
# print(student)

# print(student.get("name"))
# print(student.get("gender"))
# print(student.get("gender", "key not found"))

# List Comprehension

# l = [1, 2, 3, 4]
# ans = []

# for i in l:
#     ans.append(i * i)

# print(ans)

# print(ans:= [i * i for i in l])
# print([i * i for i in l])

# city = ["Nasik", "Mumbai", "Pune", "Nagpur", "Delhi"]
# print([i.strip(i[1:]) for i in city])

# print([ i * i if i % 2 == 0 else i * i * i for i in range(1, 11)])

# Dictionary Comprehension

# print({i : "even" if i % 2 == 0 else "odd" for i in range(1, 11)})

# STRING

# s1 = "hello"
# s2 = "hello"
# print(s1)
# print(type(s1))
# print(s1 == s2)
# print(s1 is s2)

# s1 = "hello"
# s2 = "ABCD"
# s3 = s1 + s2
# print(s3)
# print(id(s1))
# print(id(s2))
# print(id(s3))

# s1 = "hello"
# s2 = "helloabcd"
# s3 = s1 + "abcd"

# print(id(s1))
# print(id(s2))
# print(id(s3))

# s = "hello Students"
# print(s)
# print(len(s))
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())
# print(s.casefold())

# s1 = "Hello"
# s2 = "hello"
# print(s1 == s2)
# print(s1 is s2)
# print(s1.casefold() == s2.casefold())

# s1 = "hello students hi hiih iih hii hhii"
# print(s1.find("h"))
# print(s1.find("h", 4))
# print(s1.count("h"))
# print(s1.index("s"))
# print(s1.index("st"))
# print(s1.find("st"))

# SPLIT STRIP and JOIN
# s1 = "hello"
# s = s1.split()
# print(s)

# s1 = "      ccccccc ajsnbkjabs "
# print(s1.strip())
# print(s1.lstrip())
# print(s1.rstrip())

# l = ["hello", "student", "welcome"]
# print("".join(l))

# l = ["hello", "student", "welcome"]
# print(" ".join(l))

# l = ["hello", "student", "welcome"]
# print("-->".join(l))

# s1 = "hii hiii bimmmmmmmm"
# print(s1.startswith("hi"))
# print(s1.endswith("mmm"))

# s1 = "123"
# print(s1.isalnum())
# print(s1.isalpha())
# print(s1.isnumeric())
# print(s1.isdigit())

# s = "hello"
# print(s[0])
# print(s[:4])
# print(s[:: -1])

# s = "abc jkbas :nanskn , : ; aihioUJj bHHJ"
# s = "".join(i for i in s if i.isalnum())
# print(s)