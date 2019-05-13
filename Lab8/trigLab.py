'''
Course: CS2302
Author: Erick Perchez
Assignment: Lab 8
Instructor: Dr. Fuentes
TA: Andita Nath
Date: 05/12/2019
Purpose: To find similarities between two trig functions and to find
         equal subsets of the same set.
'''

import random
import numpy as np

def equal(f1, f2,tries=1000,tolerance=0.01):
    for i in range(tries):
        x = random.random()
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True


def subsetsum(S,last,goal):
    if goal ==0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) # Take S[last]
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]

''' #1
================================================================
'''

#Takes list of equations and compares all items on the list with
#each other. The list sees the list of trigonometric functions
#then i check their values and compare them using the given equal
#method to see if theyre similar.
def equalTrig(eq):
    number = 1
    for i in range(len(eq)):
        for j in range(i + 1, len(eq)):
            
            if equal(eq[i], eq[j]) == True:
                
                print(number, ')', eq[i], ' is equal to', eq[j],'\n')
                number += 1
    
''' #2
================================================================
'''

#Takes a set of numbers and splits into two different sets containing
#the same numbers but their sums are equal. Given the subsetsum
#method given i will be able to get two equal value sets. 
#I then check if their sums are similar, if so i return both.
def equalPartition(S):
    if sum(S) % 2 == 0:
        
        total = sum(S)
        x, set1 = subsetsum(S, len(S) - 1, total/2)
        set2 = []
        for i in range(len(S)):
            if S[i] not in set1:
                
                set2.append(S[i])
        if sum(set1) != sum(set2):
            
            return None
        return set1, set2
    
    return None

''' M A I N
================================================================
'''            



tList = ['sin(x)', 'cos(x)', 'tan(x)', 'sec(x)','-sin(x)', '-cos(x)', '-tan(x)', 'sin(-x)', 'cos(-x)',
         'tan(-x)', '(sin(x))/(cos(x))', '((2 * sin(x/2)) * cos(x/2))', 'sin(x) * sin(x)', '1 - (cos(x) * cos(x))', 
            '(1 - (cos(x) * cos(x))) / 2', '1 / cos(x)']


print('\n =====================Trig List=====================')

for i in range(len(tList)):
    print(i+1,')',tList[i])
print('\n ==================Similarity Test==================\n')

equalTrig(tList)

print('\n ====================Partitions=====================\n')

set1 = [2, 4, 5, 9, 12]
set2 = [2, 4, 5, 9, 13]
set3 = [1, 2, 4, 5, 6]

print('The partitions for set 1 (', set1, ')', 'are:\n')
print(equalPartition(set1), '\n')

print('The partitions for set 2 (', set2, ')', 'are:\n')
print(equalPartition(set2), '\n')

print('The partitions for set 3 (', set3, ')', 'are:\n')
print(equalPartition(set3), '\n')



