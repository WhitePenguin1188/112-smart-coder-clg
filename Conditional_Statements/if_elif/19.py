#Find the largest of three numbers

a=int(input("Enter a value for a: "))
b=int(input("Enter a value for b: "))
c=int(input("Enter a value for c: "))

if a>b and a>c:
    print("a is the largest number")
elif b>c and b>a:
    print("b is the largest number")
else:
    print("c is the largest number")