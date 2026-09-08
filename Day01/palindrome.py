a = input("Enter the no. : ")
b = len(a)

if a == a[::-1]:
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is not a palindrome.")