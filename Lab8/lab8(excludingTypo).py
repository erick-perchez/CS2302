import random
import numpy as np
from mpmath import *
from math import *

"""
The equal method and the subsetsum method were given to us 
in class
"""
def equal(f1, f2, tries = 1000, tolerance = 0.0001):
    
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
    
    if res == True:
        subset.append(S[last])
        return True, subset
    
    else:
        return subsetsum(S,last-1,goal) # Don't take S[last]
    


#Number 1
"""
Takes a list and compares all of the items on the list with each other,
the list is supposed to be a list of the trig functions, so I call the 
equal method to see if the items(trig functions) are equal to each other.
"""
def equal_for_trig_probs(theList):
    number = 1
    for i in range(len(theList)):
        for j in range(i + 1, len(theList)):
            
            if equal(theList[i], theList[j]) == True: #here's where I compare them
                
                print(number, ')', theList[i], ' = ', theList[j])
                print()
                number += 1
                

#Number 2
"""
This method takes a list of numbers and is supposed to split it into two different
sets, which have to have the same sum, and add up to the sum of the inital list.
I used the subsetsum function to get a subset with the sum of half of the sum
of the original list provided. I then took everything from the original list that
wasn't in the new list made with the subsetsum and added it to a blank list.
Lastly I compared the sums of the two lists to see if they are a match, then I
return the two lists.
"""
def partition_get_two_sets(theList):

    if sum(theList) % 2 == 0:  #check if inital sum is even
        
        total = sum(theList)
        a,set1 = subsetsum(theList, len(theList) - 1, total / 2)  #get an inital subset
        set2 = []     #blank list for the remaining elements in the original list
        
        for i in range(len(theList)):
            
            if theList[i] not in set1: #makes sure there's no repeats
                
                set2.append(theList[i])
                
        if sum(set1) != sum(set2):   #check the two sums
                
            return None
                
        return set1, set2
    
    else:
        
        return None
    

                
        
        
    

#Main
        
trigList = ['sin(x)', 'cos(x)', 'tan(x)', 'sec(x)','-sin(x)', '-cos(x)', 
            '-tan(x)', 'sin(-x)', 'cos(-x)', 'tan(-x)', '(sin(x))/(cos(x))', 
            '((2 * sin(x/2)) * cos(x/2))', 'sin(x) * sin(x)', '1 - (cos(x) * cos(x))', 
            '(1 - (cos(x) * cos(x))) / 2', '1 / cos(x)']

print('Number 1: ')
equal_for_trig_probs(trigList)


subSet_list = [2, 4, 5, 9, 12]
#test1 = [1, 2, 3]
#test2 = [2, 4, 5, 9, 13]
#test3 = [4, 4, 4, 4]


print()
print('Number 2: ')
print(partition_get_two_sets(subSet_list))
#print()
#print(partition_get_two_sets(test3))