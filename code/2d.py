import string

#
# SETUP
#

# map from int to int
g = {}
g_inverse = {}

i = 0
for line in open("./gbox.txt", "r"):
	byte_array = line.split()
	for byte in byte_array:
		int_byte = int(byte, 16)
		
		g[i] = int_byte
		g_inverse[int_byte] = i
		i += 1

cts = [
    [0] + [
        int(byte, 16) for byte in line.split()
    ] for line in open("./10ciphs.txt", "r")
]

possible_bytes = set([int(hex(ord(char)), 16) for char in string.printable])

#
# DECRYPT
#

def decrypt(ct, ct_prev, pad):
    return g_inverse[ct ^ pad] ^ ct_prev

pad_array = [0]

for char_index in range(len(cts[0])):
    # for each character, check which byte pads give us a valid character
    for pad in range(256):
        # for each pad, check if the pad is valid for each ciphertext
        valid_pad = True
        for ciphertext in cts:
            if (decrypt(ciphertext[char_index], ciphertext[char_index - 1], pad)
                    not in possible_bytes):
                valid_pad = False
                break
        if valid_pad:  # ok since there's only one valid pad for each character
            pad_array.append(pad)

print("MESSAGES:")
for ciphertext in cts:
    msg = [
        chr(decrypt(ciphertext[i], ciphertext[i-1], pad_array[i]))
        for i in range(1, len(cts[0]))
    ]
    print("".join(msg))

pad_chars = [hex(char)[2:] for char in pad_array[1:]]
print ("\nPAD:")
print(" ".join(pad_chars))
