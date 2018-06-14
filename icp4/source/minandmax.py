import numpy as np

# creating some random array of size 10*10
x = np.random.randint(25,size=(10,10))

print("Original Array:")

# printing the randomly generated array
print(x)

# searching for the min and max numbers in the randomly generated array
xmin, xmax = x.min(axis=1), x.max(axis=1)

print("\n Minimum and Maximum Values:")
print(xmin, xmax)