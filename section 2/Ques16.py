# To calculate sum of all numbers from 1 to n

n = int(input("Enter a integer number: "))
total = 0

for i in range(1 , n+1):
    total = total + i

print(f"The sum of numbers from 1 to {n} is = {total}")
       