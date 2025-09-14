#To print multiplication table of a given number
N = int(input("Enter a number: "))

print(f"Multiplication table of {N}")
for i in range(1, 11):
    print(f"{N} X {i}  = {N * i}")
      
