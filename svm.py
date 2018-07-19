#!/usr/bin/python3
import argparse

import csv
from sklearn import svm

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input data file (without the .data suffix)', required=True)
parser.add_argument('-C', nargs='*',help='input data file (without the .data suffix)', required=False, default=["1.0"])
parser.add_argument('-K', '--kernel',help='Kernel type. Default Linear', required=False, default='linear')
parser.add_argument('-g', '--gamma', nargs='*',help='Factor de ', required=False, default='0')

args = parser.parse_args()

PARAM_C= list(map(lambda x : float(x),args.C))
KERNEL = args.kernel
FILE = args.input
GAMMA = list(map(lambda x : float(x),args.gamma))


datainputs = []
dataclasses = []
testinputs = []
testclasses = []

'''
Calcula el error dado el vector de clases original y el de prediccion
'''
def errorCalc(x,y) :
    error=0
    for i in range(len(x)):
        if (x[i]!=y[i]):
            error= error+1    
                 
    return (error/len(x)) * 100


with open(FILE+'.data', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        datainputs.append(list(map(lambda x : float(x), row[:-1])))
        dataclasses.append(int(row[-1]))

with open(FILE+'.test', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        testinputs.append(list(map(lambda x : float(x), row[:-1])))
        testclasses.append(int(row[-1]))
        

def kfoldFitting (data,clases,test,testclases,c,g):
    clf = svm.SVC(kernel=KERNEL, C=c, gamma=g)
    clf.fit(data, clases)

    testprediction=clf.predict(test)
    trainprediction=clf.predict(data)

    return(errorCalc (testclases,testprediction),errorCalc(clases,trainprediction))
    
#(testerror,trainerror) = kfoldFitting(datainputs,dataclasses,testinputs,testclasses)

#print ("TEST ERROR:",str(testerror)+"%")
#print ("TRAIN ERROR:",str(trainerror)+"%")


trainMinError, testMinError = 1e10, 1e10
minC = None
minG = None

for c in PARAM_C:
    for gamma in GAMMA:
        (testError,trainError) = kfoldFitting(datainputs,dataclasses,testinputs,testclasses,c,gamma)
        if(testError<testMinError):
            trainMinError = trainError
            minC = c
            testMinError = testError
            minG = gamma

print ("C:",minC)
print ("G:",minG)
print ("TEST ERROR:",str(testMinError)+"%")
print ("TRAIN ERROR:",str(trainMinError)+"%")        
    
     
    
            
    
    

