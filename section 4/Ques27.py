# To find all prime numbers b/w 1 to 100
import math
def is_prime(n):
    if n < 2:
        return False 
    for i in range(2 , int(math.sqrt(n))+1 ):
        if n % i == 0:
            return False
    return True


print("Find prime number b/w 1 and 100")

for n in range(1 , 101):
    if is_prime(n):
        print(n, end =' ')