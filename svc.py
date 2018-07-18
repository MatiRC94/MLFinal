#!/usr/bin/python3

FOLDS=10
INPUTS='test.data'

import pprint
import csv
from sklearn import svm
from sklearn.model_selection import GroupKFold
from sklearn.utils import shuffle


#HARDCODEADO
inputs = []
classes = []
kfolds = 5



# n cant of elements of each array
def chunks(l, n,lenght):
    """Yield successive n-sized chunks from l."""
    return [l[i:i + n] for i in range(0, lenght, n)]
    

def chunkAll (data, clases, k):
    #cant of elements of array
    lendata = len(data)
    n = lendata//k
    return (chunks(data,n,lendata) , chunks(clases,n,lendata))


with open(INPUTS, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        inputs.append(list(map(lambda x : float(x), row[:-1])))
        classes.append(int(row[-1]))
        
#clf = svm.SVC(kernel=KERNEL, C=PARAM_C)
#clf.fit(inputs, classes)
#print(clf)

flatten = lambda l: [item for sublist in l for item in sublist]

def errorCalc (predictval,realval):
    return

#errorCalc [] [] n c         = c
#errorCalc (x:xs) (y:ys) n c = errorCalc xs ys n c if x===y else errorCalc xs ys n ((c+1)/n)

def errorCalc(x,y) :
    error=0
    for i,j in x,y:
        if (i!=j):
            error= error+1    
            
    return error/len(x)


def kfoldFitting (data,clases,ival):
    """ ival indice de validacion"""
    ##copiar lista
    tempData = data[:]
    tempClas = clases[:]
    
    valSet = data[ival]
    # Borro inplace el conjunto de validacion 
    del tempData[ival]
    del tempClas[ival]
    tempClas = flatten(tempClas)
    tempData = flatten(tempData)
    clf = svm.SVC()
    clf.fit(tempData, tempClas)

    print(data[ival])
    print(clases[ival])

    prediction=clf.predict(data[ival])
    print ("prediction:")
    print(prediction)
    return(errorCalc (clases[ival],prediction))
    

## MAIN



#shuffle 
shuffleInputs, shuffleClass = shuffle(inputs,classes)

print("inputs crudos: ")
print(inputs)

print("clases crudos: ")
print(classes)

#print(chunkAll(shuffleInputs, shuffleClass,kfolds))
print("Chunkeado: ")
(chunkdata,chunkclass) =chunkAll(shuffleInputs,shuffleClass,kfolds)

print((chunkdata,chunkclass))



kfoldFitting(chunkdata,chunkclass, 0)

def createFiles (i)
    file = open("fold"+i+".data","w") 

    file.write("")
    file.close() 









