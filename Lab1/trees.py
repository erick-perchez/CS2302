#Course: CS2302
#Author: Erick Perchez
#Assignment: Lab 1
#Instructor: Dr. Fuentes
#TA: Andita Nath
#Date: 02/08/2019
#Purpose: To draw a recursive tree using a given program
import numpy as np
import matplotlib.pyplot as plt
 

def draw_tree(ax,n,p):
    if n>0:
        #used to traverse the array
        i1 = [0,1,2]

        #changes the elements to lower by the original size
        ltT = p[i1] - (tSize) 
        
        print(ltT,n)
        print()       
        #changed all x axis by dividing them by 2
        ltT[i1,0] = (ltT[i1,0] * .5)
        
        #made a copy of the parameter array
        rtT = p[i1]
        
        #change y axis of leftTree by subtracting the original size
        rtT[i1,1]=(rtT[i1,1] - tSize)
        
        #divided the x axis to prevent them from touching
        rtT[i1,0]=((rtT[i1,0] + tSize) * .5) + tSize
        
        
        
        ax.plot(p[:,0],p[:,1],color='k')
        
        draw_tree(ax,n-1,ltT)
        draw_tree(ax,n-1,rtT)


plt.close("all") 
tSize =1000
p = np.array([[0,0],[tSize,tSize],[tSize*2,0]])
fig, ax = plt.subplots()
#draw_tree(ax,2,p)
#draw_tree(ax,3,p)
draw_tree(ax,4,p)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('tree.png')
