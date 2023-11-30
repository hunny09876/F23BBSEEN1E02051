# Exercise 8

# Create a new list from two list using the following condition.

#  Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.


def create_new_list(list1, list2):
    odd_numbers = [num for num in list1 if num % 2 != 0]
    even_numbers = [num for num in list2 if num % 2 == 0]
    new_list = odd_numbers + even_numbers
    
    return new_list

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result_list = create_new_list(list1, list2)
print("Resulting List:", result_list)

#  Resulting List: [1, 3, 5, 6, 8, 10]