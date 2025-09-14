# To check if a string is palindrome

string = input("Enter a string : ")

normalized = string.replace(" ", "").lower()

if normalized == normalized[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")