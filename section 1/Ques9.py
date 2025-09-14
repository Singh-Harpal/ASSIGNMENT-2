#To print the sum of digits in a given number
num = int(input("Enter a number: "))
digit_sum = 0

while num > 0:
    digit = num % 10      #get the last digit

    digit_sum += digit    #add it to sum
    
    num = num // 10       # Remove the last digit

print("Sum of digit is = ",digit_sum)