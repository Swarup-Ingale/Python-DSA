user_inputs = input("Enter numbers:")

number_list = user_inputs.split()

for num in number_list:
    if num.isdigit():
        digit_sum = sum(int(digit) for digit in num)
        print(f"{digit_sum}")
    else:
        print(f"'{num}' is not a valid number.")