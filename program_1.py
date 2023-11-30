# Exercise 1

#Calculate the multiplication and sum of two numbers.

#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

x = int(input("Please Enter the first numner:"))
y = int(input("Please Enter the first numner:"))
numbers_product  = x * y
numbers_sum = x + y

if numbers_product <= 1000:
    print(numbers_product)
else:
    print(numbers_sum)
    
    