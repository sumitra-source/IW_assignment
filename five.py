'''
Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

str1=input("Enter the string:")
def add_string(str1):
    lenght = len(str1)
    if length > 2:
        if str1[-3:]=='ing':
            print(str1 + "ily")
        else:
            print(str1 + "ing") 
    return str1
print(add_string(str1))
