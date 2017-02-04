def joshDecrypter(letters):
    message = [None] * len(letters)                   # initialize an array the same size as 'letters'
    for x in range(len(letters)):
        message[x] = chr(int(letters[-1 - x][2:], 2)) # flips 'letters' around and changes binary to ascii char

    return "".join(message)





print("Hey guys!\nIt's Joey\nWelcome\nPlease append your introduction using the same function I've used here\n\n")
print("What's up, I'm Eric, let's code some sh*t\n")
print("Hey everyone, it's Travis. Let's get coding .\n")
x = ['0b1111010', '0b1100101', '0b1110101', '0b1100111', '0b1101001', '0b1110010', '0b1100100', '0b1101111', '0b1010010', '0b100000', '0b1100001', '0b1110101', '0b1101000', '0b1110011', '0b1101111', '0b1001010', '0b100000', '0b1100001', '0b1101011', '0b1100001', '0b100000', '0b1100100', '0b1100101', '0b1111010', '0b1101001', '0b1110111', '0b1100101', '0b100000', '0b1101101', '0b100111', '0b1001001', '0b100000', '0b101100', '0b1111001', '0b1100101', '0b1001000']
print("That is my message above...")


print(joshDecrypter(x))
