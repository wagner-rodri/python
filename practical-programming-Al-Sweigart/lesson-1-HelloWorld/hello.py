# This program says Hello and asks for my name

print('Hello, World!')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName + '!')
print('The length of your name is:')
print(len(myName))
print('How old are you?') # ask how old are they
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
