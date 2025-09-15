# To print triangle pattren using stars

def print_triangle(n):
    for i in range(1 , n+1):
        print('*' * i)


rows = int(input("Enter number of rows = "))
print_triangle(rows)