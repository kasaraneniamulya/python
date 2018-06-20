import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
meanx=np.mean(x)  #mean of x
meany=np.mean(y)  #mean of y
num=np.sum((x-meanx)*(y-meany))#summation of (x2-x1)(y2-y1)
den=np.sum(pow((x-meanx),2)) #(x2-x1)^2
slope=num/den    #m
intercept=meany-(slope*meanx) #c=y-mx
print("slope",slope)
print("intercept",intercept)
val=(slope*x)+intercept
plt.scatter(x,y)
plt.plot(x,val)
plt.show()