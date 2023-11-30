# Exercise 7

#  Check Palindrome Number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome number.


def palindrome_number(number):
    num_str = str(number)
    reversed_str = num_str[::-1]
    
    if num_str == reversed_str:
        return True
    else:
        return False

number_to_check = 545
if palindrome_number(number_to_check):
    print(number_to_check, "is a palindrome number.")
else:
    print(number_to_check, "is not a palindrome number.")
    
    
    #  545 is a palindrome number.