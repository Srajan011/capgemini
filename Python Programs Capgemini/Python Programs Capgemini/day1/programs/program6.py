'''
Write a program which will perform sum and  multiplication  ,
that sums and multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4])
should return 10, and multiply([1, 2, 3, 4]) should return 24. 
'''

#sum program
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

#multiply program

def multiplyList(myList):  
    result = 1
    for x in myList: 
         result = result * x  
    return result





print(sum([1,2,3]))
print(multiplyList([1,2,3]))


