'''
Write a program that stores a number and keeps trying to get user input
until the user enters the number correctly.
As soon as the correct number is entered, it prints: Correct!
'''

i=9
while True:
   x = int(input('Enter a number:'))
   if i == x:
       print('Correct')
       break
