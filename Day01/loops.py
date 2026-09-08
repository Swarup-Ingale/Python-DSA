# FOR LOOPS
# Know Iterations
# Traverse Sequence / List

# ----------------------------------------------------------- #

# WHILE LOOPS
# Until Condition is True
# Dont know how many iterations are needed
# Until a certain condition is met
# Menu Driver Program

# ----------------------------------------------------------- #

# i = 1
# while i <= 5:
#     print("hiii")
#     i += 1
# else:
#     print("hello")

# Patterns

# for i in range(5):
#     print("*", end=""

# for i in range(5):
#     for j in range(3):
#         print("*", end="")
#     print()

# no = 1
# for i in range(5):
#     for j in range(3):
#         print(no, end="")
#     print()
#     no += 1

# no = 1
# for i in range(3):
#     for j in range(3):
#         print(no, end="")
#         no += 1
#     print()

# no = 1
# for i in range(5):
#     for j in range(3):
#         print(no, end="")
#         no += 1
#     print()
#     no = 1

# no = 3
# for i in range(3):
#     for j in range(3):
#         print(no, end="")
#     print()
#     no -= 1

# a = 65
# for i in range(3):
#     for j in range(3):
#         print(chr(a), end="")
#     print()
#     a += 1

# a = 65
# for i in range(3):
#     for j in range(3):
#         print(chr(a), end="")
#         a += 1
#     print()

# a = 67
# for i in range(3):
#     for j in range(3):
#         print(chr(a), end="")
#     print()
#     a -= 1

# a = 67
# for i in range(3):
#     for j in range(3):
#         print(chr(a), end="")
#         a -= 1
#     print()

# a = "A"
# for i in range(3):
#     for j in range(3):
#         print(a, end="")
#         a = chr(ord(a) + 1)
#     print()

# RIght Angle triange
# m = 1
# for i in range(5):
#     for j in range(m):
#         print("*", end="")
#     print()
#     m += 1

# Half Diamond
# m = 1
# for i in range(5):
#     for j in range(m):
#         print("*", end="")
#     print()
#     m += 1

# m = 5
# for i in range(0, 5, -1):
#     for j in range(m):
#         print("*", end="")
#     print()
#     m -= 1

# RIght Sided RIght angle triangle
# m = 1
# s = 4
# for i in range(5):
#     for j in range(s):
#         print(" ", end="")
#     for k in range(m):
#         print("*", end="")
#     print()
#     m += 1
#     s -= 1

# Reverse Right Sided right angle tiangle
# m = 5
# s = 0
# for i in range(5):
#     for j in range(s):
#         print(" ", end="")
#     for k in range(m):
#         print("*", end="")
#     print()
#     m += 1
#     s -= 1

# Equilateral triangle
# for i in range(5):
#     for j in range(s):
#         print(" ", end="")
#     for k in range(m * 2 - 1):
#         print("*", end="")
#     print()
#     m -= 1
#     s += 1

m = 1
s = 4
for i in range(5):
    for j in range(s):
        print(" ", end="")
    for k in range(m):
        print("* ", end="")
    print()
    m += 1
    s -= 1
