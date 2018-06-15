#inital list of the number while to be checked
lis = [1, 2, 3, -1, -2, -6, 0, 0, 0, 5, 1]
#list to store the tuples or output
trip = []
x = 0

for i in range(len(lis)):
    k = i + 1

    for j in range(k, len(lis) - 1):
        if (lis[k - 1] + lis[j] + lis[j + 1]) == 0:# this condition checks that the output is coming with all tuples and sum is equal to 0
            tup = (lis[k - 1], lis[j], lis[j + 1])
            trip.insert(x, tup)
            x += 1

print(trip)
