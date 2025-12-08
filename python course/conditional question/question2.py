age=int(input("Give me a age : "))
day ="Wednesday"
# if age<13:
#     print ("Ticket 8 dolar ")
# else:
#     print("Ticket 12 dolar")

price =12 if age>=18 else 8
if day=="Wednesday":
    price=price-2

print("Ticket price for you is ",price)