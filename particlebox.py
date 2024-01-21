import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import pyplot as plt
from matplotlib.animation import PillowWriter
import matplotlib; matplotlib.use('Qt5Agg')



x0,y0,xv0,yv0= 0.5,0.5,0.3,0.1
t, tmax, dt = 0, 100, 0.05
tcords=[]
xcords=[]
ycords =[]
x,y,vx,vy= x0,y0,xv0,yv0
while t< tmax:
    t+=dt
    tcords.append(t)
    x+=vx*dt
    y+=vy*dt
    xcords.append(x)
    ycords.append(y)
    if x<=0 or x>=1:
        vx=-vx
    if y <= 0 or y >= 1:
        vy = -vy






fig = plt.figure()

ax = plt.axes(xlim=(0, 1), ylim=(0, 1))
points, = ax.plot(x0,y0, 'o')


# initialization function: plot the background of each frame

# animation function.  This is called sequentially

def animate(i):
    x=xcords[i]
    y=ycords[i]

    points.set_ydata(y)
    points.set_xdata(x)

    return points,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate,
                               frames=600, interval=20)

plt.show()
