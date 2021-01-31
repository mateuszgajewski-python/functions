def podwoj(x):
    return x * 2

def funkcjaFilter(x):
    if x % 2 == 0:
        return x

print(podwoj(4))

print("------------------")

test = lambda x: x * 2

print(test(4))

print("------------------")

print((lambda x: x * 2)(4))

print("------------------")

myList = [4,5,6,4,3,1,2]

myList2 = [x for x in myList if x % 2 == 0]

print(myList2)

print("------------------")

print(filter(lambda x: x % 2 == 0, myList)) 

myFilterList1 = list(filter(lambda x: x % 2 == 0, myList)) #trzeba obiekt flter przerobic na liste

print(myFilterList1)


print("------------------")

print(filter(funkcjaFilter, myList)) 

myFilterList2 = list(filter(funkcjaFilter, myList)) #trzeba obiekt flter przerobic na liste

print(myFilterList2)





