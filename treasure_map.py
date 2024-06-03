#https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/e806e25c-5f84-4d7c-9c7c-2c0fcd0bfe84?sl=5a6962c9-0e42-448b-b7df-0616c6d30431&st=SEfB5kQTLxCzgxd1DdyJRDPpY9Rp1HhB
#link for the auditorium
#lists....
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3] #nested list
print("Hiding your treasure! X marks the spot.")
position = input(" Where do you want to put the treasure?") #position like column: A, B, C and row 1,2,3 as matrix form 
letter = position[0] 
abc = ['A', 'B','C']
letter_index = abc.index(letter)
number_index = int(position[1])-1 #index is starting with 0 so..(-1)
map[number_index][letter_index] = 'X'
print(f"{line1}\n{line2}\n{line3}")