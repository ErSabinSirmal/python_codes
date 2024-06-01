
#leap year checking if/else statements 
year = int(input("Enter the year: "))
# conditional statements
if year%4 ==0:
  if year%100==0:
    if year%400==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")