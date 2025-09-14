# To print all numbers between two given numbers(start, end)

def print_numbers(start, end):
    for num in range(start , end+1):
        print(num , end = ' ')

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
print_numbers(start ,end)


