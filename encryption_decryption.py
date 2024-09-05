alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def caesar(original_text, shift_amaunt, fdirection):
    caesar_text = ""
    
    for letter in original_text:

        if fdirection == "decode":
            shift_amaunt*= -1
        shifted_position = alphabet.index(letter)+shift_amaunt
        shifted_position %= len(alphabet)
        caesar_text+= alphabet[shifted_position]
    print(f"Here the {direction} result is: {caesar_text}")  
caesar(original_text=text, shift_amaunt=shift, fdirection=direction)      

