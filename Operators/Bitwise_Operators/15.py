#Count the number of set bits in a number

num=int(input("Enter a number: "))
count=0
while num:
    count+=num&1
    num>>=1
print("The number of set bits is:",count)