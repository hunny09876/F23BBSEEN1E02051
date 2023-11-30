# Exercise 5

#  Display numbers divisible by 5 from a list.

# Iterate the given list of numbers and print only those numbers which are divisible by 5.


numbers = [10, 25, 7, 30, 45, 12, 5, 20]

for i in numbers:
    if i % 5 == 0:
        print(i)
        
