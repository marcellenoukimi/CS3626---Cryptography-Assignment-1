#Function 1 (String ↔ List of characters):
#it takes as input an arbitrary length string
#and outputs a list of characters, or vice versa.
#For example, Input string: “hello world” Output list: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
#,or Input list: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’] Output string: “hello world”

print("Function 1 - String <-> List of Characters\n")

# Method to split string into characters
print("1. Convert a string to a list of characters")
entry = input("Input String: ")
print("Output list: ", list(entry))

# Method to join list of characters into string
print("\n2. Convert a list of characters to a string")
# Enter characters separated by comma like h,e,l,l,o, ,w,o,r,l,d for example
listChar = list(map(str, input("Input list : ").strip().split(',')))[:1000]
print("Output string: ",str("".join(map(str, listChar))))

