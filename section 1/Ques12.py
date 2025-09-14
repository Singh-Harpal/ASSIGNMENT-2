# To reverse a given number
num = int(input("Enter a number ="))
reverse = 0

is_negative = num < 0
num = abs(num)

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed no. is = ",reverse)