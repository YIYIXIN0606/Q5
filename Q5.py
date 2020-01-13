myArray = [31, 2, 11, 23, 8, 7, 11, 14, 20]
ind = list(range(len(myArray)))
print("original:", end=" ")
print(myArray)

for i in range(len(myArray)):
    for j in range(0,len(myArray)-i-1):
        if myArray[j] > myArray[j+1]:
            myArray[j],myArray[j+1] = myArray[j+1],myArray[j]
            ind[j],ind[j+1] = ind[j+1],ind[j]
print("sorted:", end=" ")
print(myArray)
print("index:", end=" ")
print(ind)
