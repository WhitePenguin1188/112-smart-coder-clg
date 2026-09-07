#Check if the Kth bit of a number is set or not

num=int(input("Enter a number: "))
k=int(input("Enter the value of k: "))
if num & (1 << (k-1)):
    print("The Kth bit is set")
else:
    print("The Kth bit is not set")