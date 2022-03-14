from itertools import count
import matplotlib.pyplot as plt 
import math
import numpy as np

def applyRes(arr, res):
    return np.array(list(map(lambda x: x/res, arr)))


def taylorSineSeries(n, r): #n(Int) - depth of taylor series, r(Int) - range of values plotted in negative and positive direction
    res = 100

    xaxis = np.array(range(-r*res,r*res))
    xaxis = applyRes(xaxis, res)

    print(xaxis)
    

    yaxis = []
    for point in xaxis:
        counter = 0
        sum = 0
        for _ in range(n):
            sum += (  (point**((2*counter) + 1))   * (((-1)**counter) /( math.factorial((2*counter)+1)) ) )            


            counter += 1
        
        yaxis.append(sum)
    
    plt.plot(xaxis, yaxis)
    plt.axhline(0,color ='black')
    plt.axvline(0,color = "black")
    plt.show()



def taylorExponential(n, r): #n(Int) - depth of taylor series, r(Int)- 
    res = 10 

    xaxis = np.array(range(0, r*res))
    xaxis = applyRes(xaxis, res)


    yaxis = []
    for point in xaxis:
        sum = 0
        counter = 0 
        
        for _ in range(n):
            sum += (point**counter)/(math.factorial(counter))
            counter +=1 
        
        yaxis.append(sum)

    plt.plot(xaxis, yaxis)
    plt.axhline(0,color ='black')
    plt.axvline(0,color = "black")
    plt.show()
    

taylorExponential(15, 10)


def taylorCosineSeries(n, r): #n(Int) - depth of taylor series, r(Int) - range of values plotted in negative and positive direction
    res = 100

    xaxis = np.array(range(-r*res,r*res))
    xaxis = applyRes(xaxis, res)

    print(xaxis)
    

    yaxis = []
    for point in xaxis:
        counter = 0
        sum = 0

        for _ in range(n):
            sum += ( ((-1)**counter)  /  (math.factorial(2*counter)))  * (point**(2*counter))

            counter +=1
        yaxis.append(sum)
    
    plt.plot(xaxis, yaxis)
    plt.axhline(0,color ='black')
    plt.axvline(0,color = "black")
    plt.show()  


taylorCosineSeries(10,5)