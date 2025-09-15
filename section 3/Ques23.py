# To remove duplicate elements from the list

def remove_duplicates(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
   
    return unique_list


list = [4,35,56,32,1,2,34,99,4,34,32]
print("Orignal list :",list)
print("List after removes duplicates", remove_duplicates(list))