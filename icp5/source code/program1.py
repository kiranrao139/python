import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

#finding the mean values of x and y
mean_of_x = x.mean()
mean_of_y = y.mean()

#finding the slope
slope = np.sum((x - mean_of_x) * (y - mean_of_y)) / np.sum(np.square(x - mean_of_x))

#calculating intercept
intercept = mean_of_y - (slope * mean_of_x)

#y output
y_output = (slope * x) + intercept

# plotting the line made by linear regression
plt.plot(x, y)

plt.plot(x, y_output)

#plt.show()
plt.show()

