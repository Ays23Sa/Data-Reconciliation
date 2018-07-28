#Data Reconciliation for the a simple network
# ------F1--------F3------F5-------F6
#       |         |
#      F2---------F4
import numpy as np
from scipy.optimize import fsolve
def func(X):
    
    x=[0,0,0,0,0,0]
    y=[101.91,64.45,34.65,64.20,36.44,98.88]
    L=[0,0,0,0]
    for i in range (0,6):
        x[i]=X[i]
    for j in range (6,len(X)):
         L[j-6]=X[j]    
      
    
    return (x[0] - y[0])**2 +(x[1] - y[1])**2+(x[2] - y[2])**2+(x[3] - y[3])**2+(x[4] - y[4])**2+(x[5] - y[5])**2 +L[0] * (x[0]-x[1]-x[2]) +L[1] * (x[1]-x[3]) + L[2] * (x[2]-x[4]) + L[3] * (x[3]+x[4]-x[5])
def dfunc(X):
         dLambda = np.zeros(len(X))
         h = 1e-3 # this is the step size used in the finite difference.
         for i in range(len(X)):
             dX = np.zeros(len(X))
             dX[i] = h
             dLambda[i] = (func(X+dX)-func(X-dX))/(2*h)
         return dLambda

X1 = fsolve(dfunc, [100, 64, 36, 64, 36, 100, 0, 0, 0, 0])
sliceobj = slice(0,6)
print("RECONCILED VALUES ARE :")
print (X1[sliceobj])