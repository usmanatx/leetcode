def convert_palindrome(_str):
    first_half = _str[:int(len(_str)/2)]
    middle = _str[int(len(_str)/2)]

    if middle == '0':
        middle = '9'
        first_half = str(int(first_half) -1 )
    elif middle == '9':
        middle = '0'
        first_half = str(int(first_half) +1 )

    second_half = ''
    for s in first_half:
        second_half = '{}{}'.format(s, second_half)

    return '{}{}{}'.format(first_half, middle, second_half)



def find_palindrome(num):
    int_to_str = ''
    while num > 0:
        int_to_str = '{}{}'.format(str(num % 10), int_to_str)
        num = int(num/10)
    return convert_palindrome(int_to_str)

find_palindrome(29024)


"""
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
 


"""