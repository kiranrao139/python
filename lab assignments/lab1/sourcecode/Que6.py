
import numpy
#imported for different numpy
import collections
x=numpy.random.randint(25,size=(1, 15))
list=[1]
print(x)
y=x[0]
def CountFrequency(arr):
    return collections.Counter(arr)


freq = CountFrequency(y)
print(freq)
print("most common: ")

print( (freq.most_common())[0][0])
