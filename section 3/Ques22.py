# To find maximum and minimum number in a list

def find_max_min(numbers):
    if not numbers :         #empty list 
        return None ,None  

    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers[1:]:
       if num > max_num:
        max_num = num
       if num < min_num:
        min_num = num
    
    return max_num ,min_num

list1 = [45,46,18,90,24,56,86]
maximum , minimum = find_max_min(list1)
print(f"Maximum number is = {maximum}")
print(f"Minimum number is = {minimum}")

