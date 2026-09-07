#Check if a character is uppercase, lowercase, digit, or special character

char=(input("Enter a character: "))

if char.isupper():
    print("The character is uppercase")
elif char.islower():
    print("The character is lowercase")
elif char.isdigit():
    print("The character is a digit")
else:
    print("The character is special character")