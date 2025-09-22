import numpy as np

def dot_product(a,b):
    z = 0
    for x in range(len(a)):
        z += a[x] * b[x]
    return z

def auto_Dot(a,b):
    return a.dot(b)

def dott():
    a  = np.array([1,2,3,4])
    b= np.array([2,3,4,5])

    a1 = [[1,2,3],[3,4,5]]
    print(np.array(a1))
    print(dot_product(a,b))
    print(a.dot(b))
    print(np.array(a1).shape)

def Construct_zero_one_arrays():
    print(np.ones((3,4)))

    print(np.zeros((3,3)) + 99)


#Construct_zero_one_arrays()

def arr_ay():
    print(np.eye(3))#creating the diag 1
    print(np.diag((2,2,3)))
    print(np.arange(4,10))# start from 4 to 9
    print(np.arange(5))#Count from 0 to 5
    print(np.arange(1,10,2)) # start from 1 to 10 but jump two units
    ary = np.array((np.arange(1,10,0.5)))
    print(f"The first argumen ti is {ary[0]}")
    print(f"Am trying to fetch the first three argiments {ary[0:3]}")
    ax1 = np.diag((1,9,3,4,5,6))
    ax2 = np.eye(6)
    nect = np.array((ax1,ax2))
    print(ax1)
    print(ax1[1,1])#X and Y
    print(ax1[:,1])#Printing entire column
arr_ay()
