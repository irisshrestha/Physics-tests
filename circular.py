import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

def shm(t,y):
    dydt = np.sin(t)
    dxdt = np.cos(t)
    return dydt,dxdt

sol = scipy.integrate.solve_ivp(shm,(0,10),(0,1),t_eval= np.linspace(0,10,100))

plt.plot(sol.y[1],sol.y[0])
plt.show()
