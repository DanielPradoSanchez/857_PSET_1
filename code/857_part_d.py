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



g_values = "01 58 84 e9 a2 27 b9 ed ee 9f a4 4c 3b 90 61 5e d6 c4 d5 dd 41 74 31 de e0 3f 33 76 9d 6a 35 2d bf 3a fd 47 94 fe 83 28 2b 39 0d 80 b2 1e 2e e2 b7 43 f3 2c 06 c0 ac 1d 20 d2 52 aa 8e 13 e7 7f a1 92 a8 c3 69 45 f9 f6 1a 97 d7 be 5c f5 56 04 70 6d 0b 32 63 60 b0 75 5f f4 c6 b1 57 a9 44 99 e5 05 6e 59 da 89 0c 07 68 36 77 15 65 9b 1c d3 7b 22 5d 02 a6 e6 6c 2a d1 4b bb 0e 4e 29 fb f0 bd 73 87 fc ec 3c ca 46 86 64 ae 09 26 21 16 11 79 c9 08 ef b6 2f a7 b3 93 ad 62 98 d8 cb 49 96 a5 df ce 8a bc c7 1f 4a cd f2 1b 7d f8 51 14 ff 72 8b 24 3d 38 91 30 10 e1 53 db 3e 55 7e d0 00 a0 ab b5 66 b8 17 03 8c 0f fa 85 71 f1 8d 34 a3 9c 50 6f 5a dc 8f 78 54 af d9 12 ba 19 4f 25 9a cf b4 88 40 cc 9e 18 c1 ea 48 23 81 37 e8 e4 95 5b 7a 4d d4 c8 eb 67 7c 82 f7 42 0a 6b e3 c2 c5".split()


def g(hex_input):
    index = convert_hex_to_bits(hex_input)
    return convert_hex_to_bits(g_values[index])

def inverse_g(hex_input):
    return convert_hex_to_bits(g_values.index(hex_input))

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

cipher_texts = ["5d 24 7d b9 8d ea 8a d3 5e 5c e3 a3 28 82 b7 65 d3 6a ba 42 c7 6d 04 1c 89 e1 eb 87 d5 93 db 0f 6e 93 25 1d 83 a9 01 6f 0c e2 a1 41 92 bd 51 64 d7 86 d8".split(),
                "21 dc f0 e3 26 b5 cd ed 86 c6 fd a5 bb cc fa 1f 7b 20 8d e2 31 14 b9 54 28 e6 c1 9e a8 44 ae 80 c5 bb b8 53 8e 5d 81 36 28 d2 4c bc 55 b2 dd cf 77 3c ae".split(),
                "9b 2d 43 70 c4 e9 60 bf 68 cb e5 e7 38 e4 b4 99 70 61 e0 80 2f 0e 1f 62 4c 41 42 9c 01 d5 06 24 15 2f 95 85 0a 6e 3c f5 91 cf de 29 a7 7a 04 ff ed d0 a2".split(),
                "4f 6c e1 94 7c 8c 35 97 8d 23 32 96 8f df 9c ac 9a b0 3d 2b c1 e4 2e 8c f8 32 aa d7 51 11 52 c7 f1 b9 24 95 b7 66 90 7b f2 cd bd 9d 85 fb ae 83 b8 d2 7e".split(),
                "05 23 a4 7d 9d 20 ee 9a a1 fd f4 ee 69 23 9b 9b 82 33 54 97 94 5a 56 d5 4a 64 da e4 29 b8 0b d3 bb 85 85 1f e7 1f 83 e9 4b 2f e8 3d f6 75 64 44 55 5b 18".split(),
                "9c 8e bf 51 7f 82 65 95 99 19 37 a8 59 0d fb 9f ff ce 3b 89 76 8e f0 32 75 aa 24 e3 73 de db 2b a3 9f c3 47 e3 66 58 42 2e 66 a3 31 3e 4c e5 8d 4a bf 16".split(),
                "44 1c d6 c8 bc 75 cb a3 68 68 78 17 89 e2 c4 cd 44 6e e5 53 28 0c 56 6d ee 32 4c 28 0d 87 51 2a c2 a2 02 62 65 77 25 6c cf 1c 5c 19 1a 77 54 25 d3 08 3f".split(),
                "21 cd ec bf 71 23 fd 1e 66 33 55 86 94 52 4e c5 89 b7 7e 56 e8 9b 0f e5 79 83 7c 7b 00 d9 93 b3 34 6b c6 ca 68 45 22 b1 c2 56 21 6a 46 83 ef 1d 5e 43 84".split(),
                "9b ad db e4 b8 32 fc d7 9b 4c fb 7b 98 f8 af b0 ce 05 1a 6b 6d 6b c3 a8 8d a7 f4 7a e9 8d db c0 44 34 84 47 ca 05 3a 98 8c c5 a4 be db 18 79 07 69 ca f4".split(),
                "92 e2 28 c7 1b 99 88 5b 28 76 38 21 82 dc a6 b9 47 a9 80 17 d9 80 ac 56 7f c6 b7 7a 76 5f ae db 6a c3 52 3d a7 09 c4 1a 96 d3 de 69 f6 44 bf 0c 3d 37 ed".split()]





