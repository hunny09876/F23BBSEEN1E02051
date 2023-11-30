# Exercise 3

#Print characters from a string that are present at an even index number.

#Write a program to accept a string from the user and display characters that are  present at an even index number.


input_string = input("Please enter the string:")


for i in range(0, len(input_string), 2):
    print("Character at", i, "index is:", input_string[i])
    
    