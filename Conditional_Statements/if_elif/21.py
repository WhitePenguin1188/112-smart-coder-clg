#Ticket Pricing : Calculate ticket price based on the customer's age.

age=int(input("Enter your age: "))

if age<5:
    print("Ticket is free")
elif age>=5 and age<=12:
    print("Ticket price is $10")
elif age>=13 and age<=64:
    print("Ticket price is $20")
else:
    print("Ticket price is $15")