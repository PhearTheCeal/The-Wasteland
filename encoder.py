"""Encodes a given string in Base64. 
   By Crispin A. Stichart."""

def encode(string):
    """Takes a string and returns the Base64 representation."""
    binary = convert_to_binary(string)
    # Figures out how much padding the string needs, if any
    if len(user_input) % 3 != 0:
        if (len(user_input)+1) % 3 == 0:
            binary = binary << 2
            padding = 1
        else: 
            binary = binary << 4
            padding = 2
    else: padding = 0
    print("Binary after", len(bin(binary))-1)
    # The leadingzero part is because convert_to_binary() can return
    # an odd number if the first character is a number, because 
    # ord() of any digit is a 7 bit integer. 
    # The "- (1 - leadingzero)" is because bin returns a string
    # that includes the letter b.
    # chars is how many 6-bit chunks there are in the string
    leadingzero = (len(bin(binary)) - 1) % 2
    chars = (len(bin(binary)) - (1 - leadingzero)) // 6 
    b64 = "" # converted characters are placed in this string
    # the main conversion loop
    for char in range(chars-1, -1, -1): #counts down in reverse
        code = binary >> (6 * char)
        binary = binary - (code << (6*char))
        if 0 <= code <= 25:
            b64 += chr(code + ord("A"))
        if 26 <= code <= 51:
            b64 += chr(code + ord("a") - 26)
        if 52 <= code <= 61:
            b64 += chr(code + ord("0") - 52)
        if code == 62:
            b64 += "+"   
        if code == 63:
            b64 += "/"
    b64 += "=" * padding
    return b64


def convert_to_binary(string):
    """Takes a string and packs each letter into an integer,
       then returns that number."""
    binary = 0
    for letter in string:
        # okay, so what's going on here is that some characters oridinal values
        # are less than 8 bits. So this makes sure they're padded correctly. 
        code = ord(letter)
        bitnumber = len(bin(code))-1 # bin() returns string with "b" in it
        print("bitnumber", bitnumber)
        binary = code + (binary << (8))
    return binary

if __name__ == "__main__":
    print("Give me a line of text, and I'll give you the Base 64 representation!")
    print("Give me a blank line (Just press enter!) to quit me.")
    while True:
        user_input = input(">>> ")
        if user_input == "": break
        print(encode(user_input))
        print("")
    print("Bye!") 