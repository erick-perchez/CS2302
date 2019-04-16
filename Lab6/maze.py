
# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import time


def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
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

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
        
def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S, i):
    if S[i] < 0:
        return i
    r = find_c(S, S[i])
    S[i] = r
    return r


def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj: 
        S[rj] = ri  
        
def unionBySize(S, i, j):
    ri = find_c(S, i)
    rj = find_c(S, j)
    if ri != rj:
        if S[ri] > S[rj]:  #Checks if  root i is greater than root of j
            S[rj] += S[ri]
            S[ri] = rj  #points i to j
        else:
            S[ri] += S[rj]
            S[rj] = ri  #points j to i
      
def numSets(S):
    sets = 0
    for i in range(len(S)):
        if S[i] < 0:
            sets += 1
    return sets

def sameSet(S,a,b):
    rA = find(S,a) #Checks for the roots of both indices 
    rB = find(S,b)
    if rA == rB:
        return True
    return False

def buildMaze_Standard(W, S):
    while numSets(S) > 1: #if theres more than 1 set, we arent done
        rand = random.randint(0, len(W)-1)
        if sameSet(S, W[rand][0], W[rand][1]) is False: #checks if they dont belong in the same set
            union(S, W[rand][0], W[rand][1]) #creates union between the two sets
            W.pop(rand) #removes rand from the maze
    return W

def buildMaze_Compression(W, S):
    while numSets(S) > 1: #if theres more than 1 set, we arent done
        rand = random.randint(0, len(W)-1)
        if sameSet(S, W[rand][0], W[rand][1]) is False: #checks if they dont belong in the same set
            unionBySize(S, W[rand][0], W[rand][1]) #creates union between the two sets
            W.pop(rand) #removes rand from the maze
    return W

'''
===============================================================================
Main
'''

plt.close("all")

maze_rows = 10
maze_cols = 15

Walls = wall_list(maze_rows, maze_cols)
S = np.zeros(maze_rows * maze_cols, dtype = np.int)-1 #DSF

print('========================================================')
print()
print('Building Maze with Standard Unions...')
start = time.time()
Maze = buildMaze_Standard(Walls, S)
end = time.time()
print('Running Time for Maze with Standard Unions:', round((end - start) * 1000, 6))
draw_maze(Maze, maze_rows, maze_cols)
print('========================================================')
print()

SN = np.zeros(maze_rows * maze_cols, dtype = np.int)-1 #DSF
WallsN = wall_list(maze_rows, maze_cols)

print('Building Maze with Union by Size...')
startN = time.time()
MazeN = buildMaze_Compression(WallsN, SN)
endN = time.time()
print('Running Time for Maze with Union by Size:', round((endN - startN) * 1000, 6))
draw_maze(MazeN, maze_rows, maze_cols)
print('========================================================')