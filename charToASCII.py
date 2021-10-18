# Function 2 (List of characters ↔ ASCII):
# it takes as input a list of characters
# and outputs a list of corresponding ASCII codes,
# or vice versa.
# For example,Input list: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
# Output list: [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
print("Function 2 - List of Characters <-> ASCII\n")

# Method to convert a list of characters to a list of corresponding ASCII codes
print("1. Convert a list of characters to a list of corresponding ASCII codes")
# Enter characters separated by comma like h,e,l,l,o, ,w,o,r,l,d for example
listChar = list(map(str, input("Input list : ").strip().split(',')))[:1000]
print("Output list: ", str([ord(ele) for sub in listChar for ele in sub]))

# Method to convert a list of ASCII codes to a corresponding list of characters
print("\n2. Convert a list of ASCII codes to a corresponding list of characters")
listASCII = list(map(int, input("Input list : ").strip().split(',')))[:1000]
print("Output list: ", str("".join(map(chr, listASCII))))
