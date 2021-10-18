# Function 3 (ASCII ↔ Binary): it takes as input a list of ASCII codes and outputs
# a list of binary numbers, or vice versa

import binascii

# binascii module is imported in this program
# to use some of its methods for the conversion between binary data and ASCII

print("Function 3 - ASCII <-> Binary\n")
# Method to convert a list of ASCII codes to a list of corresponding binary numbers
print("1. Convert a list of ASCII codes to a list of corresponding binary numbers")
liste = list(map(str, input("Input list : ").strip().split(',')))[:1000]
entry = str("".join(map(str, liste)))
result = bin(int.from_bytes(entry.encode(), 'big'))[2:]
print("Output list:", str([result]))

# Method to convert a list of binary numbers to a list of corresponding ASCII codes
print("\n2. Convert a list of binary numbers to a list of corresponding ASCII codes")
en = input("Input list : ")
m = int(en, 2)
output = binascii.unhexlify('%x' % m)
outputDecode = output.decode('utf-8')
print("Output list: ", str([outputDecode]))
