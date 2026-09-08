x = input("Enter a positive integer: ")

if x.lstrip('-').isdigit():
    n = int(x)
    
    if n < 0:
        print("Factorial does not exist for negative numbers.")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(f"The factorial of {n} is {result}")
else:
    print("Please enter a valid integer.")