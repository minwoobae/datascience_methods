
import numpy as np

def getSampleMean(Sample):

    xT = Sample
    sampleMean = 0

    n = len(xT)
    sampleMean = np.sum(xT)/n

    return sampleMean


def getProjection(Sample):

    yT = Sample
    n = len(yT)
    xMean = getSampleMean(yT)
    oneVect = np.ones(n)

    projection = xMean*oneVect

    return projection

def getDeviationVect(Sample):

    yT = Sample
    deviation = 0
    projection = getProjection(yT)
    deviation = yT - projection

    return deviation


def checkOrthogonality(X, Y):

    result = 0
    x = X
    y = Y
    result = np.dot(x,y)

    return result

def getNormDeviation(Deviation):

    norm = 0
    temp = []
    deviation = Deviation


    for i, di in enumerate(deviation):

        temp.append(di**2)

    tempSum = np.sum(temp)

    norm = np.sqrt(tempSum)

    return norm

# Get Sample Variance of Input Data
def getSampleVar(Sample):

    sampleDev = 0
    xT = Sample
    n = len(xT)
    deviation = getDeviationVect(xT)

    norm = getNormDeviation(deviation)

    sampleDev = norm/np.sqrt(n-1)

    return sampleDev


Y = [3497900, 2485475, 1782875, 1725450, 1645575, 1469800]

deviation = getDeviationVect(Y)
projection = getProjection(Y)
print(getSampleVar(Y))
