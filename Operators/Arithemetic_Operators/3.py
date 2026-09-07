#Calculate simple interest given P, R, T → (P × R × T) / 100

p=int(input("Enter the amount money loaned:"))
r=float(input("Enter the Yearly Interest Rate:"))
t=int(input("Enter the Time required to pay:"))

sp=(p*r*t)/100

print("The Interest Rate is ",sp)