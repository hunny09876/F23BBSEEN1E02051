# Exercise 2

#Print the sum of the current number and the previous number.

#Write a program to iterate the first 10 numbers,and in each iteration,print the sum of the current and previous number.

previous_number = 0
for current_number in range(0, 10, 1):
    numbers_sum = current_number + previous_number
    print("Current Number", current_number , "Previous Number", previous_number, "Sum:", numbers_sum)
    previous_number = current_number
    
    
    