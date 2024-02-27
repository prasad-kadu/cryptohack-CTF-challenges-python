#string label to be XOR with integer 13. Convert this integer back to string and submit the flag.
given_string = "label"
for char in given_string:
    val = ord(char)
    print(chr(val ^ 13), end = '')
