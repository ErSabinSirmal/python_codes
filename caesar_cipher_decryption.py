alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO 1-Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount as 2 points.
def decrypt(original_text, shift_amount):
    cipher_text= ""
    for letter in original_text:
        # shifted_position = (alphabet.index(letter)-shift+len(alphabet))%len(alphabet) ---it is right also...
        shifted_position = (alphabet.index(letter)-shift)%len(alphabet)

        cipher_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")  
decrypt(original_text=text, shift_amount=shift)      
#TODO 2 -Inside the decrypt() function, shift each letter of the 'original_text'  backwards 
 # by the shift_amount and print the decrypted text.

#TODO 3- Combine the 'encrypt()' and 'decrypt()' functions into one function called caesar().
 #use the value of the user choosen 'direction' variable to determine which functionality to use .
 # call the caesar funtion decrypt() and pass in all three variables. direction/text/shift....