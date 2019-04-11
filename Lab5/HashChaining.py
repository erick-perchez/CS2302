'''
Course: CS2302
Author: Erick Perchez
Assignment: Lab 2
Instructor: Dr. Fuentes
TA: Andita Nath
Date: 04/10/2019
Purpose: To use hash tables and binary trees to find similarities
         between words using a long file given and my own file of 
         words
'''



import numpy as np
import time
import statistics
import math


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T


class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        for i in range(size):
            self.item.append([])
        
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
    
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
    
def h(s,n):
    r = 0
    for c in s:
        r = (r*255 + ord(c))% n
    return r


def loadFactor(H,i):
    return i/len(H.item)

'''
===============================================================================
BST Section

'''
#def Building_BST(file1,file2):


def findWord(T,k):
    t = T  
    while t is not None:  
        if t.item[0] == k:
            return t.item[1]
        
        elif t.item[0] > k:  
            t= t.left
            
        elif t.item[0]<k:
            t = t.right
            
    return None 


def numNodes(T):
    if T is None:
        return 0
    
    else:
        return 1 + numNodes(T.left)+numNodes(T.right)
    
    return 0


def getHeight(T):
    if T is None:
        return 0
    
    leftH = getHeight(T.left)
    rightH = getHeight(T.right)
    
    if rightH<leftH:
        return leftH+1
    
    else:
        return rightH+1
    
'''
#==============================================================================
Hash Table Methods
'''
    
#finds number of items in table
def numItems(H):
    Num=0
    for i in range(len(H.item)):
        Num+=len(H.item[i])
        
    return Num

#counts how many are empty
def numEmpty(H):
    count=0
    for i in range(len(H.item)):
        if len(H.item[i])==0:
            count+=1
            
    return count

#finds element in hash, returns -1 if not found
def findHash(H,k):
    b=h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            
            return H.item[b][i][1]
        
    return -1

#used to find the length of the standard diviation
def lenList(H):
    L=[]
    for i in range(len(H.item)):
        L.append(len(H.item[i]))
    return L

#method to double the size of the table
def doubleSize(H):
    new = HashTableC(2*len(H.item)+1)
    for i in range(len(H.item)):
        for j in range(len(H.item[i])):
            if H.item[i]==None:
                print()
            else:
                InsertC(new,H.item[i][j][0],H.item[i][j][1])
    return new
    



'''
===============================================================================
Main
'''
print('___________________________________________')
print('|       Choose table implementation       |')  
print('|      Type 1 for Binary Search Tree      |')
print('|   Type 2 for Hash Table with Chaining   |')
print('|_________________________________________|')
x = input('Choice: ')
print()
print('=====================================================')
print()

file1 = open('glove.6B.50d.txt',encoding='utf-8') #uses the text provided to be read later on
file2 = open('myFile.txt',encoding='utf-8') #uses my own text file to be read later on

if int(x) == 1:
    print('Building Binary Search Tree...')
    print()
    
    T = None
    start = int(time.time())
    
    for line in file1:
        
        info = line.split(' ')
        #inserts words and embeddings text file
        T = Insert(T, [info[0], np.array(info[1:]).astype(np.float)]) 
    
    end = int(time.time())
    
    print('Binary Search Tree Stats:')
    print('Number of nodes:',numNodes(T))
    print('Height:', getHeight(T))
    print('Running Time for Binary Search Tree Construction:',(end-start))
    print('Reading word file to determine similarities...')
    print()
    print('=====================================================')
    print()
    print('Word Similarities Found:')
    
    
    start2=int(time.time())
    
    for line2 in file2:
        
        info = line2.split(',')
        #returnslist when found
        e0 = findWord(T,info[0])
        e1 = findWord(T,info[1])
        #Prints and compute the similarity
        print("Similarity", info[0:2], " = ", round(np.sum(e0 * e1) / (math.sqrt(np.sum(e0 * e0)) * math.sqrt(np.sum(e1 * e1))), 4))
    end2 = int(time.time())
    print()
    print('=====================================================')
    print('Running Time for Binary Search Tree Query Processing:',(end2-start2))

   
elif int(x) == 2 :
    
    print('Building Hash Table...')
    print()
    
    H = HashTableC(29)
    
    print('Hash Table Stats:')
    print('Initial Table Size:', len(H.item))
    
    count=0
    #used for big .TXT file given
    for line in file1:
        #gets index of first character in file
        info = line.index(' ')
        #gets first word
        word = line[:info]
        
        #creates embedding
        embedding = np.fromstring(line[info:-1],dtype=float,sep=' ')  
        
        if loadFactor(H,count) == 1:
            #doubles size if loadfactor is 1
            H=doubleSize(H)
            InsertC(H,word,embedding)
            count+=1
            
        else:
            InsertC(H,word,embedding)
            count+=1
    
    print('Final Table Size:', len(H.item))
    print('Reading word file to determine similarities...')
    print()
    print('=====================================================')
    print()
    print('Word Similarities Found:')
    #used to store infro from file
    l=list() 
    startTime=int(time.time())
    
    #Used for my own .TXT file
    for line in file2:
        #gets index of first character in file
        info = line.index(',') 
        #gets first word
        word = line[:info]
        #gets second word
        word2=line[info+1:-1]
        l.append([word,word2])
        info=line.split(",")
        
        #returns the list when found
        e0=findHash(H, info[0]) 
        e1=findHash(H, info[1])
        
        #Prints and compute the similarity
        print("Similarity", info[0:2], " = ", round(np.sum(e0 * e1) / (math.sqrt(np.sum(e0 * e0)) * math.sqrt(np.sum(e1 * e1))), 4))
        
    endTime=int(time.time())  

    print()
    print('=====================================================')
    print()
    print('Load Factor:', loadFactor(H, numItems(H)))
    print('Percentage of empty lists:', round((numEmpty(H)/len(H.item)), 2))
    print('Standard deviations of the lengths of the lists:', round(statistics.stdev(lenList(H))))
    print('Running time for Hash table query construction:', endTime-startTime)
    print()
    print('=====================================================')
    
else:
    print ('Invalid Input')
    
file1.close()
file2.close()