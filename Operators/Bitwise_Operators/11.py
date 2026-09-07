#Check if a number is odd or even using bitwise operator

num=int(input("Enter a number: "))
if num & 1:
    print("The number is odd")
else:
    print("The number is even")