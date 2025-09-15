#To genrate a list of first n prime numbers
import math
def is_prime(n):
    if n < 2:
        return False 
    for i in range(2 , int(math.sqrt(n))+1 ):
        if n % i == 0:
            return False
    return True

def generate_prime(n):
    primes = []
    candidate = 2
    
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

count = int(input("Enter how many prime you want: "))
prime_list = generate_prime(count)
print(prime_list)