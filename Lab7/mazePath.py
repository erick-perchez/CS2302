'''
Course: CS2302
Author: Erick Perchez
Assignment: Lab 7
Instructor: Dr. Fuentes
TA: Andita Nath
Date: 05/06/2019
Purpose: To modify a maze and show a path using differrent algorithms
'''

import matplotlib.pyplot as plt
import numpy as np
import time
import random
import queue

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    return False

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    return False

def union_by_size(S,i,j):
    # if i is a root, S[i] = number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]:
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def NumSets(S):
    count =0
    for i in S:
        if i < 0:
            count += 1
    return count


'''
=============================================================================
'''


def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    # Draws a maze
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)
    return ax


def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w


# Creates the adj list fora graph
def get_adj_list(p, A):
    for i in range(len(p)):
        temp0 = p[i][0]
        temp1 = p[i][1]
        A[temp0].append(temp1)
        A[temp1].append(temp0)
    return A



# Check's for a path recursively backwards from end to start by checking
#a path exists
def path(plot, prev, vertex, x, y):
    # Only element at previous[0] should equal -1 if a path exists
    # If a -1 is found before it, it means no path exists.
    if prev[vertex] != -1:
        # path is ploted in red from removed wall 
        if vertex == (prev[vertex] + maze_cols):
            x1 = x
            y1 = y - 1
            
            path(plot, prev, prev[vertex], x1, y1)
            
            plot.plot([x1, x], [y1, y], linewidth = 3, color = 'r')
            
        if  vertex == (prev[vertex] - maze_cols):
            x1 = x
            y1 = y + 1
            
            path(plot, prev, prev[vertex], x1, y1)
            
            plot.plot([x1, x], [y1, y], linewidth = 3, color = 'r')    
            
        if vertex == (prev[vertex] + 1):
            x1 = x - 1
            y1 = y
            
            path(plot, prev, prev[vertex], x1, y1)
            
            plot.plot([x1, x], [y1, y], linewidth = 3, color = 'r')     
            
        if vertex == (prev[vertex] - 1):
            x1 = x + 1
            y1 = y
            
            path(plot, prev, prev[vertex], x1, y1)
            
            plot.plot([x1, x],[y1, y], linewidth = 3, color = 'r')
    
    
#Traverses adjacency list using depth-first search
def depth_first_search(G):
    start = time.time()*1000
    #creates a list of boolean
    visited = [False] * len(G)  
    
    #creates a list of length G
    prev = [-1] * len(G)  
    
    #a list is used as a stack
    S = []  
    #appends 0 as its the start then changes to True
    S.append(0)
    visited[0] = True 
    #Traversal starts from 0
    while S: #not empty
        #vertex popped from S
        v = S.pop()
        for t in G[v]:
            #checks if its visited
            if not visited[t]:
                visited[t] = True
                prev[t] = v
                S.append(t)
    stop = time.time()*1000
    print('Depth First Search took: ', stop-start, ' milliseconds')
    return prev


# Traverses(w/ recursion) adjacency list using depth-first search
def depth_first_search_recursion(G, source):
    #source starts at 0
    visited[source] = True
    for t in G[source]:
        #checks if visited
        if not visited[t]:
            #then source is appended to prev list
            prev[t] = source 
            depth_first_search_recursion(G, t)
    return prev

# Travereses adjacency list with breadth-first search
def breadth_first_search(G):
    visited = [False] * len(G)
    prev = [-1] * len(G)
    #creates queue from function
    Q = queue.Queue()
    #0 is the start, so its put first and changesd to True on visited
    Q.put(0)
    visited[0] = True
    while Q.empty() is False:
        #vertex gets popped then saved to v
        v = Q.get()
        for t in G[v]:
            #checks if visited then added to prev list
            if not visited[t]:
                visited[t] = True
                prev[t] = v
                Q.put(t)
    return prev


# creates a maze and removes walls depending on users input
def Union_Maze(M, w, m):
    popped = []
    while m > 0:
        #D is the wall that gets removed at random
        d = random.randint(0, len(walls)-1)
        if NumSets(M) == 1:
            popped.append(walls.pop(d))
            m -= 1
        elif union_c(M, walls[d][0], walls[d][1]) is True:
            popped.append(walls.pop(d))
            m -=1
    
    temp_list = []
    #creates a temporary list
    for i in range(maze_rows*maze_cols):
        temp_list.append([])  
    
    adj_list = get_adj_list(popped, temp_list)
    print('Adj list =========',adj_list)
    return adj_list

plt.close("all") 
maze_rows = 15
maze_cols = 15
num_cells= maze_rows*maze_cols

walls = wall_list(maze_rows,maze_cols) # Creates the walls for the maze
M = DisjointSetForest(maze_rows*maze_cols)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True)

'''
===============================================================================
Main
'''

print('=============================================================')
print()

print('There are', maze_rows*maze_cols,' cells.')
m = int(input('How many walls do you want to remove: '))
while m < 0 or m > 3000000: #max number of walls in a 15X20
    m = int(input('Invalid input, try a different number:'))
if m > len(walls) - 1:
    print('The number of walls you want to remove exeeds the number of walls that are present.')     
if m > num_cells - 1:
    print('There is at least one path from source to destination (m > n-1).')
if m < num_cells - 1:
    print('A path from source to destination is not guaranteed to exist (m < n-1).')
if m == num_cells - 1:
    print('There is a unique path from source to destination (m = n-1).')
    
print()
print('=============================================================')
print()

start = time.time() * 1000

G = Union_Maze(M, walls, m)  # Creates maze

end = time.time() * 1000

print('This maze is a', maze_rows, 'X', maze_cols, 'maze.')
print('Running time for this maze is:', (end-start), 'milliseconds')    

print()
print('============================================================')
print()
#variable created to be used in depth_first_search_recursion
visited = [False] * len(G) 
#variable created to be used in depth_first_search_recursion 
prev = [-1] * len(G)  

start = time.time() * 1000

bfs = breadth_first_search(G)

end = time.time() * 1000

print('Breadth First Search:', bfs)
print('Breadth First Search took:', end-start, 'milliseconds')

print()
print('============================================================')
print()

start = time.time() * 1000
dfs = depth_first_search(G)
end = time.time() * 1000

print('Depth First Search: ', dfs)
print('Depth First Search took: ', end-start, ' milliseconds')

print()
print('============================================================')
print()

start = time.time()
dfsr = depth_first_search_recursion(G, 0)
end = time.time()

print('Depth First Search using recursion took: ', end-start, ' milliseconds')
print('Depth First Search using recursion: ', dfsr)

print()
print('============================================================')
print()

print('How do you want to generate a path?')
print('Type 1 for Breadth First Search')
print('Type 2 for Depth First Search')
print('Type 3 for Depth First Search (Recursively)')
print()
ans = int(input('Your Choice:'))

#sends the path to generate a path from start to end
plot = draw_maze(walls,maze_rows,maze_cols)  

start = time.time()*1000
#1 generates path with BFS
if ans == 1: 
    path(plot,bfs,(num_cells)-1,maze_cols-.5,maze_rows-.5)

#2 generates a path with DFS
elif ans== 2:
    path(plot,dfs,(num_cells)-1,maze_cols-.5,maze_rows-.5)
    
#3 generates path with DFS recursive
else: 
    path(plot,dfsr,(num_cells)-1,maze_cols-.5,maze_rows-.5)
    
end = time.time()*1000

print('To generate path, it took', end-start, 'milliseconds to generate a path from start to finish')
plt.show()
