m = 1
for i in range(5):
    for j in range(m):
        print("*", end="")
    print()
    m += 1
m = 5
for i in range(0, 5, -1):
    for j in range(m):
        print("*", end="")
    print()
    m -= 1