alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO 1- Create a functio called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs. 
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)+shift
#         cipher_text += alphabet[shifted_position]

#     print(f"Here is the encoded result: {cipher_text}")   

#TODO 4- What happens if you try to shift z forwads by 9? can you fix the code???
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = (alphabet.index(letter)+shift)% len(alphabet) 
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")            

#TODO 2- Insid the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#by the shift amount and print the encrypted txt.

#TODO 3 -Call the 'encrypt()' function and pass in the user inputs. YOu should be able to test the code 
# and encrypt a messsage

encrypt(original_text=text, shift_amount=shift)