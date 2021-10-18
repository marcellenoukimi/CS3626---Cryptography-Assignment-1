# CS3626---Cryptography-Assignment-1
**Problems:**

The aim of this assignment is to implement a text conversion program (Let’s call this “text
converter”), which is comprised of the three functions described below. Pre/post conditions
(inputs and outputs) for the text converter are defined as follows:

**Function 1 (String ↔ List of characters):** it takes as input an arbitrary length string and
outputs a list of characters, or vice versa. For example,

Input string: “hello world”

Output list: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]

, or

Input list: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]

Output string: “hello world”

You can check a type of input or use the second parameter to let the function know the type
of input.

**Function 2 (List of characters ↔ ASCII):** it takes as input a list of characters and outputs
a list of corresponding ASCII codes, or vice versa. For example,

Input list: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]

Output list: [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]

, or

Input list: [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]

Output list: [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]

**Function 3 (ASCII ↔ Binary):** it takes as input a list of ASCII codes and outputs a list of
binary numbers, or vice versa. For example,

Input list: [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]

Output list: [1101000, 1100101, 1101100, 1101100, 1101111, 100000, 1110111, 1101111,
1110010, 1101100, 1100100]

, or

Input list: [1101000, 1100101, 1101100, 1101100, 1101111, 100000, 1110111, 1101111,
1110010, 1101100, 1100100]

Output list: [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
