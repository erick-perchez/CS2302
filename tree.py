#import numpy as np
#import matplotlib.pyplot as plt
#
#
#def draw_tree(ax,n,p):
#    if n>0:
#
#        i1 = [0,1]
# 
#        p[i1,0] = p[i1,0]*-1
#        
#        
#        print(p[i1])
#        
#        ax.plot(p[:,0],p[:,1],color='k')
#        
#        draw_tree(ax,n-1,p)
#        
#        
#
#plt.close("all") 
##orig_size = 800
##p = np.array([[0,0],[-25,-50]])
#ax = plt.subplots()
#
#
##draw_tree(ax,3,p)
#
#
#ax.set_aspect(1.0)
#ax.axis('on')
#ax.show()
#fig.savefig('tree.png')


import numpy as np
import math
import matplotlib.pyplot as plt


def plot_point(point, angle, length, n):
     if n > 0:
         

         x, y = point
#         x = x*1.2
#         y = y*1.2


         endy = length * math.sin(math.radians(angle)) + y
         endx = length * math.cos(math.radians(angle))+x
         

         rightEX= endx *-1
         rightEY = endy
         
         point = [endx,endy]
         point2 = [rightEX,rightEY]
         
         
         ax.plot([x, endx], [y, endy], color = 'k')
         length = length*.75
         ax.plot([x * -1, rightEX], [y, rightEY],color = 'k')
         print(angle)
#         print([x, endx], [y, endy])
#         print()
#         print([x, rightEX], [y, rightEY])
#         print()
#         print(point)
#         print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
         plot_point(point2, angle+10, length, n-1)
         plot_point(point, angle+10, length, n-1)
     

fig = plt.figure()
ax = plt.subplot(111)
ax.set_ylim([-100, 100])   # set the bounds to be 10, 10
ax.set_xlim([-100, 100])
fig.show()
plot_point([0,0], 225, 15, 4)