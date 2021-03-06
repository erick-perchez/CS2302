#Course: CS2302
#Author: Erick Perchez
#Assignment: Lab 1
#Instructor: Dr. Fuentes
#TA: Andita Nath
#Date: 02/08/2019
#Purpose: To draw a square collage using a given program
import numpy as np
import matplotlib.pyplot as plt

def draw_squares(ax,n,coord,ave):
    if n>0:
        
        i1 = [0,1,2,3,4]
        
        #for the initial square i modified the coordinates to shifting everything
        #800 positive units to both the x and y axis then multiplied by the ave value
        #which is .5 (to get the squares lined up)
        corner1 = (coord + 800) * ave
        
        #for the second square/corner i did what i did with the first just shifted
        #everything by 800 negative units on both axis
        corner2 = corner1*-1
        
        #to be able to modify one column at a time i had to set corner3 to be equal to coord
        corner3 = coord
        
        #after that i changed the second column coordinates by 800 positive units then 
        corner3[i1,1] = ((coord[i1,1] + 800) * ave)
        #afterwards i changed the first column coordinates as well
        corner3[i1,0] = ((coord[i1,0] - 800) * ave)
        #i then multiplied everything by the ave to get a smaller square
        
        #to get the last corner(right bottom corner) i had to copy the same array as in corner3
        #then invert the values to get the opposite coordinates.
        corner4 = corner3 * -1        
        
        ax.plot(coord[:,0],coord[:,1],color='k')
        
        #recursive calls for every corner of the initial square
        draw_squares(ax, n-1,corner4,ave)
        draw_squares(ax,n-1,corner3,ave)
        draw_squares(ax,n-1,corner2,ave)
        draw_squares(ax,n-1,corner1,ave)
        
        
plt.close("all") 
#i had to center the main square by using the following coordinates
coord = np.array([[-400,-400],[-400,400],[400,400],[400,-400],[-400,-400]])
fig, ax = plt.subplots()
#the squares lined up by changing the average to .5(r)
#draw_squares(ax,4,coord,.5)
#draw_squares(ax,3,coord,.5)
draw_squares(ax,2,coord,.5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')
