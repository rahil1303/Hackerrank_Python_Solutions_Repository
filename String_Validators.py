#### You are given a string .
##Your task is to find out if the string  S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


s = str(input())
print(any(a.isalnum()) for a in s)
print(any(a.isalpha()) for a in s)
print(any(a.isdigit()) for a in s)
print(any(a.islower()) for a in s)
print(any(a.isupper()) for a in s)
