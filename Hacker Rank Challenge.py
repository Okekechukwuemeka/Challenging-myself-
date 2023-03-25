'''Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username. according to the following rules: '''

#1. The username is between 4 and 25 characters.
#2. It must start with a letter.
#3. It can only contain letters, numbers, and the underscore character.
#4. It cannot end with an underscore character.

'''If the username is valid then your program should return the string true, otherwise return the string false.'''
#Examples
#Input: "aa_"
#Output: false
#Input: "u__hello_world123"
#Output: true

def CodelandUsernameValidation(str):
    x = len(str)
    if str.isalpha() and str.isdigit() and '_' in str:                 print('This Username is True')

        if str[0].isalpha() and str[-1] != _:                 print('This Username is True')

            if x >= 4 and  x >= 25:                 print('This Username is True')

    else:
        print('This Username is False')

import re
def CodelandUsernameValidation(str):
    if str==re.match('^a:zA:z', str) and (r'\wa:zA:Z0:9', str) and ('_!$', str):  print('True.') 
    if len(str) >3 and len(str) < 26: print('True.')  
    else: print('False')

def FindIntersection(str):
    str1 = int(input('Please enter your first set of numbers.'))
    str2 = int(input('Please enter your second set of numbers.'))
    x = str1{}
    y = str2{}
z = x.intersection(y)
    if x.intersection(y)==z: return z 
    else: print('False')
    







