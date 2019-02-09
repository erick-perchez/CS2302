import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):

    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    

    
    return x,y


def draw_manyCircles(ax,n,center,radius,sVal):
    if n>0:
        
        #moves the x axis over to the left while leaving y axis along, shrinks the whole circle by 1/3
        leftCir = [(center[0] - (2 * (radius / sVal))), center[1]]
        
        #moves the x to the right while shrinking the circle by 1/3        
        rightCir = [(center[0] + (2 * (radius / sVal))), center[1]]   
        
        #keeps the x axis as is, moves the y axis up and shrinks the circle by 1/3
        topCir = [center[0], (center[1] + (2 * (radius / sVal)))]     
        
        #keeps x axis still, moves the y axis down and shrinks the circle
        bottomCir = [center[0], (center[1] - (2 * (radius / sVal)))]  
        
        x,y = circle(center,radius) 
        
        ax.plot(x,y,color='k') 
        
        #recursive methods shrink radius by a 1/3
        
        #draws center circle
        draw_manyCircles(ax, n - 1, center, radius / sVal,sVal)
        draw_manyCircles(ax, n - 1, leftCir, radius / sVal,sVal) 
        draw_manyCircles(ax, n - 1, rightCir, radius / sVal,sVal)  
        draw_manyCircles(ax, n - 1, topCir, radius / sVal,sVal)  
        draw_manyCircles(ax, n - 1, bottomCir, radius / sVal,sVal)   
      


plt.close("all") 
fig, ax = plt.subplots() 
draw_manyCircles(ax, 5, [100,0], 100,3)
#draw_manyCircles(ax, 4, [100,0], 100, 3)
#draw_manyCircles(ax, 3, [100,0], 100, 3)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('manyCircles.png')
