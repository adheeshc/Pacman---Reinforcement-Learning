import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy

myData1=np.genfromtxt('ApproxQlearning_smallGrid_100iterations.csv',delimiter = ',')
t=np.linspace(0,100,100)
t2=np.linspace(0,10000,10000)
x1=myData1[:,1]
print(x1)
myData2=np.genfromtxt('Qlearning_smallGrid_10000iterations.csv',delimiter=',')
x2=myData2[:,1]

plt.plot(t,x1)
plt.plot(t2,x2)
#plt.legend('Approx Q','Q Learning')
plt.show()