import numpy as np
import matplotlib.pyplot as plt



def Playgroung():
    fig,ax = plt.subplots()#A figure with axes

#fig, axs = plt.subplots(2,2) # A figure with 2*2 Grids axes

#fig, axs = plt.subplot_mosaic([["left","right_top"],["left","right_bottom"]])# Figure with custom axes in the Figure



    b = np.matrix([[1,2,3],[2,3,4]])
    ba_sarray = np.asarray(b)
#Coverting Matrix to array prior plottin
    ax.plot([1,2,3,4],[2,6,7,3]) 

    ax.set_title("Numbersvs Object")

    ax.set_xlabel("Number")

    # Most methods will also parse a string-indexable object like a dict, a structured numpy array, or a pandas.DataFrame. Matplotlib allows you to provide the data keyword argument and generate plots passing the strings corresponding to the x and y variables

    np.random.seed(1739983)
    data = {'a': np.arange(50),
    'c':np.random.randint(0,50,50),
    'd': np.random.randn(50)    
    }
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d'])* 100

    ax.scatter('a','b', c = 'c',s = 'd', data = data)


    # Annotating

    ax.annotate("The trial", xy = (10,20), xytext = (40,50), arrowprops = dict(facecolor = 'black', shrink = 0.05) )
     
    ax.legend()
#ax.plot()
    plt.show()

def playground2():
    arraY_1 = np.array([[1,2,3,4],[2,6,7,5]])

    print(np.add(arraY_1,1))

    print(arraY_1+1)
    #Perfoming additon along all columns in array

    print(np.add.reduce(arraY_1, axis=0)) #also arraY_1.sum(axis = 0)
    #Perfoming the the addition along all rows

    print(np.add.reduce(arraY_1, axis=1))

    print(arraY_1.sum(axis = 1))

#np.mean (computes arithmetic mean or average)
#np.std (computes the standard deviation)
#np.var (computes variance)
#np.sort (sorts an array)
#np.argsort (returns indices that would sort an array)
#np.min (returns the minimum value of an array)
#np.max (returns the maximum value of an array)
#np.argmin (returns the index of the minimum value)
#np.argmax (returns the index of the maximum value)
#np.array_equal (checks if two arrays have the same shape and elements)


def Numpy_Broadcasting():
    ary = np.array([[1,2,4,6],[9,1,4,5]])
    print(ary + 1)
    print(ary + np.array([1,2,3,4]))

def advanced_Indexong():

    ary = np.array([[1,2,4,6],[9,1,4,5],[2,3,4,5]])
    firts = ary[1:3]
    firts +=100
    print(ary)
# Fancy Index
    Seconds_Copy = ary[:,[1,3]] #Craeting a copy
    print(Seconds_Copy + 99) 
    print(ary)

#Boolean
    Bol_100 = ary > 100

    print([Bol_100])

#Random

    np.random.seed(123)
    print(np.random.rand(3))

    rng = np.random.RandomState(seed =123)
    print(rng.rand(3))

    gen = np.random.default_rng(seed = 123)
    print(gen.random(3))

def Reshaping_Index():
    ary = np.array([1,2,3,4,5,6])
    ary_2 = ary.reshape(-1,2)#any number or rows but fixed colums each have 2 values but can be broken by adding reshape(3,2) three rows and 2 columns

    ary_3 = np.array([2,3,4,5,6,7])
    print(np.concatenate((ary,ary_3 ), axis = 0))
    print(ary_2.flatten()) #return to 1D

def operation_Index():
    ary = np.array([1,2,3,4,5])

    mask = ary > 3

    print(ary[mask])
    print(ary[(ary > 3) | (ary<2 )])# | can be & ^ or ~ 

    print(np.where(ary > 2,10,0)) #Replace where value of ary greater than 2 else 0

def Linear_algebra():
    ary_1 = np.array([1,2,3,4,5,6])
    ary_2 = ary_1.reshape(3,-1)#Infinite columens but 3 rows
    ary_3 = np.array([[2,4,5],[6,7,8]])
    print(ary_2)
    print(ary_3)

    ary_Mult = np.matmul(ary_2,ary_3) #Perform matrix multiplication
    print(ary_Mult)
    print(np.dot(ary_2,ary_3))#Perform dot multiplications

    print(f"The transpos of ary_mult is {ary_Mult.transpose()}")
    


Linear_algebra()