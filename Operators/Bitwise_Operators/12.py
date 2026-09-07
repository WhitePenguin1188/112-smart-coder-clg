#Swap two numbers without using a XOR

a=int(input("Enter a number:"))
b=int(input("Enter another number:"))

a=a^b
b=a^b
a=a^b

print("After swapping, the value of a is:",a)
print("After swapping, the value of b is:",b)