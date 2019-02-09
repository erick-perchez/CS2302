import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):

    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    

    
    return x,y


def draw_circles(ax,n,center,radius,w):
    if n>0:
        
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        
        #moves the x and y axis by shrinking it
        center[0] = center[0]*w
        center[1] = center[1]*w
        
        draw_circles(ax,n-1,center,radius*w,w)
      


plt.close("all") 
fig, ax = plt.subplots() 
#draw_circles(ax, 10, [100,0], 100, .5)
#draw_circles(ax, 20, [100,0], 100, .75)
draw_circles(ax, 40, [100,0], 100, .9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
