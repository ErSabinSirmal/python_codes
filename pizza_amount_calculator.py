print("Thank you for choosing Python Pizza Deliveries!")
size = input( "What size pizza do you want? S, M, or L: ")
add_pepperoni = input(" Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size =="S":
  price = 15
elif size == "M":
  price = 20
else:
  price = 25
if size == "S":
 if add_pepperoni == "Y":
  price +=2
else:
  if add_pepperoni == "Y":
    price +=3

if extra_cheese == "Y":
  price +=1


print(f"Your final bill is: ${price}.")
   