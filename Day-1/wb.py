# Given a string of letters, write a function to see if the word  is a palindrome (the same word spelled forward and backwards).

# The given string will contain only letters 

# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False


"""

input string of letters
output=boolean
contraints: inputs only letters, only one word
Racecar

approach:
look at each letter and check equality
if unequal then non palindrome
if equal look at next letters
next letters moving first letter one to right
last letter one to left
continue checking all letters for equality until unequal or i've checked to the middle

sudo code:
if not letter=
return false
else=
continue
"""


def check_palindrome(astring):
    left_point = 0
    right_point = len(astring) - 1
    while left_point < right_point:
        if astring[left_point].lower() != astring[right_point].lower():
            return False
        else:
            left_point += 1
            right_point -= 1
    return True
    
print(check_palindrome("RaceCar"))
print(check_palindrome("Mom"))
print(check_palindrome("Shoha"))