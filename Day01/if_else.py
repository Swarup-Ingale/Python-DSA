a = int(input("enter a no. : "))

if a % 3 == 0:
    if a % 5 == 0:
        print(f"{a} is divsible by both 3 and 5")

    else:
        print(f"{a} is not divisible by 5")

else:
    if a % 5 == 0:
        print(f"{a} is divisible by and 5")

    else:
        print(f"{a} is not divisible by 5 and 3")
