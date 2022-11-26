"""Fixed XOR
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:
746865206b696420646f6e277420706c6179"""
import secrets
import string


"""First version: encryption/decryption using randomized key:"""
#chr() takes numerical value and returns ascii character for each 128 unique ascii values
ascii_table = [char for char in ''.join(chr(i) for i in range(128))]
#print(ascii_table)

strings = [char for char in string.printable] #all printable ascii characters
int_values = [ord(char) for char in string.printable] #use ord() to get their integer values
binary_values = [bin(ord(char)) for char in string.printable] #use bin() to get binary values from ints

print(strings)
print(int_values)
print(binary_values)

#XORing strings together using ord()
int1, int2 = ord('e'), ord('0')
xor_num = int1 ^ int2
print(xor_num) #numeric value for the XOR'd string character = 85/U/01010101

#get string value of XOR
ascii_char = xor_num.to_bytes((xor_num.bit_length() + 7) // 8, byteorder = 'big').decode() #byteorder says most sig bit is at beginning of byte array
print(ascii_char)

#XORing binary strings
binary1 = '01000001'
binary2 = '00110001'
bit_string = ''.join([str(int(let1) ^ int(let2)) for let1, let2 in zip(binary1, binary2)])
print(bit_string) #01110000

#turn binary value into ascii character
ascii_char = chr(int(bit_string, 2)) #2 bits- 0 and 1
print(ascii_char) #'p', ascii value of 01110000

#XOR encryption
def xor_encryption(message):
    num_list = [ord(char) for char in message] #get numerical value of each character
    key = secrets.choice(range(128)) #XOR each of them against a fixed key (random number from ascii characters)
    encrypt_list = [num ^ key for num in num_list]
    return [''.join([xor_num.to_bytes((xor_num.bit_length() + 7) // 8, byteorder = 'big').decode() for xor_num in encrypt_list]), key]


#prints encrypted message and key
some_text = xor_encryption('1c0111001f010100061a024b53535009181c')
print(some_text)

st = some_text[0]
key = some_text[1]

#XOR decription:
def xor_decription(text_again, key):
    num_list = [ord(char) ^ key for char in text_again]
    return ''.join([xor_num.to_bytes((xor_num.bit_length() + 7) // 8, byteorder = 'big').decode() for xor_num in num_list])

decrypted_text = xor_decription(st, key)
print(decrypted_text)

"""Second version: XORing of two equal-length buffers:"""

#hex values:
hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"
print("original input: ", hex1)

#convert hex to int, then int to binary, and remove "0b" from beginning of both binary values:
binary1 = bin(int(hex1, 16))[2:]
binary2 = bin(int(hex2, 16))[2:]

#find out which binary value is longer:
final_length = len(binary1) if len(binary1) > len(binary2) else len(binary2)

#use result to make strings equal lengths so XORing is easier
binary1 = binary1.zfill(final_length)
binary2 = binary2.zfill(final_length)

#combine binary values with zip() and XOR bit by bit:
end_result = [int(bits1) ^ int(bits2) for bits1, bits2 in zip(binary1, binary2)]

#convert list format to string:
string_result = "".join([str(bits) for bits in end_result])

#convert binary back to hex, remove '0x' prefix:
encrypted_result = hex(int(string_result, 2))[2:]

print("Results after XORing against 686974207468652062756c6c277320657965:")
print(encrypted_result)