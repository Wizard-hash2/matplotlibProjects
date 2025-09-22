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

Playgroung()