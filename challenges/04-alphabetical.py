# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input('give me a string to alphabetize!\n')
letters = list(string)
letters.sort()
print(letters)