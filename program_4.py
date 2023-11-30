# Exercise 4

#  Check if the first and last number of a list is the same.


def first_and_last_number(numbers):
    if len(numbers) > 0:
        return numbers[0] == numbers[-1]
    else:
        return False
    
my_list = [1, 2, 3, 4, 5, 9]
result = first_and_last_number(my_list)

if result:
    print("The first and last numbers are the same.")
else:
    print("The first and last numbers are not the same.")
    
    
    
   #  the first number and the last number are not same .
    