# Randomly choose who will going to pay the bill today in the restaurant....
import random
names = ["stute","Bejamin","Gobardhan","Tina","Mina"]
new_items = len(names)
index = random.randint(0,new_items-1)
print(f"{names[index]} is going to buy the meal toaday! ")
