#Check if all 3 numbers are equal using bitwise operator

a=int(input("Enter the value for a: "))
b=int(input("Enter the value for b: "))
c=int(input("Enter the value for c: "))

if a&b==c:
    print("All 3 are equal")
else:
    print("All 3 are not equal")
