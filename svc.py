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
kfolds = 2



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
        
#clf = svm.SVC()
#clf.fit(inputs, classes)
#print(clf)


def kfoldFitting (data,clases,ival):
    """ ival indice de validacion"""
    ##copiar lista
    tempData = data[:]
    tempClas = clases[:]
    
    valSet = data[ival]
    # Borro inplace el conjunto de validacion 
    del tempData[ival]
    




#shuffle 
shuffleInputs, shuffleClass = shuffle(inputs,classes)


#print(chunkAll(shuffleInputs, shuffleClass,kfolds))
print(chunkAll(shuffleInputs,shuffleClass,kfolds))












