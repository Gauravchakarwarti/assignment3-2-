#Write a Python program to reverse a string.


﻿#Sample String : "1234abcd"

#Expected Output : "dcba4321"

#solution

def reverse_string(string):
    return string[::-1]

sample_string = "1234abcd"
reversed_string = reverse_string(sample_string)
print(reversed_string)
