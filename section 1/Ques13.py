# To print first 10 fibonacci numbers
a = 0
b = 1

print("First 10 Fibonacci numbers are: ")
for i in range(10):
    print(a, " ",end='')
    a, b = b ,a+b
 