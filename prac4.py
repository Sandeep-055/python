def decode_string(s):
    result = ""
    i = 0
    while i < len(s):
        # Extract the letter
        letter = s[i]
        i += 1

        # Extract the number
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1

        # Convert the number to an integer and repeat the letter
        result += letter * int(num)

    return result


# Test cases
input1 = "a1b10"
input2 = "b3c6d15"

output1 = decode_string(input1)
output2 = decode_string(input2)

print(output1)  # Output: abbbbbbbbbb
print(output2)  # Output: bbbccccccddddddddddddddd

