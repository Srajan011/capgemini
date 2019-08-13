'''
 Write a program that takes a value (i.e. a number, string, etc)
 x and a list of values a,
 and returns True if x is a member of a,
'''

def is_member(x,y):
    if x in y:
        return True
    else:
        return False

x = input('Enter a number or a string:')
y = [10,20,30,58,'hiren']
c = is_member(x,y)
print(c)
