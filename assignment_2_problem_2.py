# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

#   Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

# Createing the dictionary

dict_mine = {}
 
# for loops starts from here

for i in range(97, 97 + 26):
    # Matching the char to that of the asci value
    dict_mine[chr(i)] = i
 
# Print the  dictionary
print(dict_mine)