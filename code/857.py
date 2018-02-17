import enchant
d = enchant.Dict("en_US")

from nltk.corpus import words

hex_codes = {"0000":"0",
             "0001":"1",
             "0010":"2",
             "0011":"3",
             "0100":"4",
             "0101":"5",
             "0110":"6",
             "0111":"7",
             "1000":"8",
             "1001":"9",
             "1010":"a",
             "1011":"b",
             "1100":"c",
             "1101":"d",
             "1110":"e",
             "1111":"f"
             }

inverted_codes = {}
for code in hex_codes:
    inverted_codes[hex_codes[code]] = code

alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet_binary = "01100001 01100010 01100011 01100100 01100101 01100110 01100111 01101000 01101001 01101010 01101011 01101100 01101101 01101110 01101111 01110000 01110001 01110010 01110011 01110100 01110101 01110110 01110111 01111000 01111001 01111010".split()

capitalized_alphabet_binary = "01000001 01000010 01000011 01000100 01000101 01000110 01000111 01001000 01001001 01001010 01001011 01001100 01001101 01001110 01001111 01010000 01010001 01010010 01010011 01010100 01010101 01010110 01010111 01011000 01011001 01011010".split()

binary_to_alphabet = {}
for index in range(len(alphabet_binary)):
    binary_to_alphabet[alphabet_binary[index]] = alphabet[index]
    binary_to_alphabet[capitalized_alphabet_binary[index]] = alphabet[index].upper()

alphabet_to_binary = {}
for binary in binary_to_alphabet:
    alphabet_to_binary[binary_to_alphabet[binary]] = binary

def convert_word_to_binary(word):
    binary = []
    for letter in word:
        binary.append(alphabet_to_binary[letter])
    return binary

def convert_binary_to_word(binary):
    word = ""
    for entry in binary:
        word += binary_to_alphabet[entry]
    return word

def convert_hex_to_bits(hex_code):
    return inverted_codes[hex_code[0]]+inverted_codes[hex_code[1]]

def xor(seq1, seq2):
    xored_seq = []
    for index in range(len(seq1)):
        val = int(seq1[index]) + int(seq2[index])
        if val == 1:
            xored_seq.append('1')
        else:
            xored_seq.append('0')


    return "".join(xored_seq)

# def calculate_possible_from_xored(xored_sequence):
#     possible_pairs = []
#     for entry in alphabet_binary:
#         xored = xor(xored_sequence, entry)
#         if xored in alphabet_binary or xored in capitalized_alphabet_binary  and ((entry, xored) not in possible_pairs) and ((xored, entry) not in possible_pairs):
#             possible_pairs.append((entry, xored))

#     for entry in capitalized_alphabet_binary:
#         xored = xor(xored_sequence, entry)
#         if (xored in alphabet_binary or xored in capitalized_alphabet_binary) and ((entry, xored) not in possible_pairs) and ((xored, entry) not in possible_pairs):
#             possible_pairs.append((entry, xored))
#     return possible_pairs

# def get_possible_pairings(encoded_1, encoded_2):
#     xored_message = []
#     for index in range(len(encoded_1)):
#         xored_message.append(xor(encoded_1[index], encoded_2[index]))
#     possible_pairs = []
#     for entry in xored_message:
#         possible_pairs.append(calculate_possible_from_xored(entry))
#     return possible_pairs

# def build_possible_messages(possible_pairs):
#     possible_messages = [("","")]
#     for possible_pair in possible_pairs:
#         next_messages = []
#         for message in possible_messages:
#             for pair in possible_pair:
#                 next_messages.append((message[0]+pair[0], message[1]+pair[1]))
#         print("DONE WITH NEXT GROUP", len(next_messages))
#         possible_messages = next_messages
#     valid_messages = []
#     for message in possible_messages:
#         if d.check(message[0]) and d.check(message[1]):
#             valid_messages.append(message)
#     return valid_messages

encoded_message_1 = "a6 a5 6d f4 8c a0 fc 86 d6 1f 2f e9".split()
encoded_message_2 = "ac b9 60 e1 94 a3 f2 93 d2 01 24 f5".split()



encoded_1 = xor("1111","1010")
encoded_2 = xor("0101","1010")


message_1 = []
message_2 = []
for entry in encoded_message_1:
    message_1.append(convert_hex_to_bits(entry))
for entry in encoded_message_2:
    message_2.append(convert_hex_to_bits(entry))

xored_message = [xor(message_1[index], message_2[index]) for index in range(len(encoded_message_1))]



# possible_pairings = get_possible_pairings(message_1, message_2)
# possible_letters = []
# for possible_choices in possible_pairings:
#     choices_i = []
#     for pairing in possible_choices:
#         choices_i.append((binary_to_alphabet[pairing[0]], binary_to_alphabet[pairing[1]]))
#     possible_letters.append(choices_i)

possible_words = [word for word in words.words() if len(word) == 12]
binary_words = [convert_word_to_binary(word) for word in possible_words]

possible_words = []

for binary_word in binary_words:
    xored_possible_message = [xor(xored_message[index], binary_word[index]) for index in range(len(encoded_message_1))]
    possible_word = "".join([binary_to_alphabet[entry] for entry in xored_possible_message if entry in binary_to_alphabet])
    if len(possible_word) != 12:
        continue
    if d.check(possible_word):
        possible_words.append(possible_word)
print((possible_words))

#print(build_possible_messages(possible_letters))




'''
2b:
intended recipient has p, use to xor cipher. Then, lookup what entry would have 
resulted in the ouput from g (this gives you m xor c_i-1). Then xor this with 
c_i-1 to get message


2c:
xoring with c_i-1 doesn't tell you anything about pad as it uses previous pad bytes 
(i.e. they won't cancel out) and then indexing into g just adds one more level to 
encryption. You can treat g(m xor c_i-1) as essentially a message itself which then 
encryption mechanism just become OTP

2d:
- do same as before, xor Ci[k] with Cj[k] to then get some info and do for all entries
- then take these and do system of equations to get individual g(m xor c_i-1) 
(unclear whether or not this step will work ^)
- can do inverse look up to get m xor c_i-1, already know what c_i-1 is
- xor with c_i-1 to then get m

'''







