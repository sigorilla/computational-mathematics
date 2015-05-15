from math import *
import copy
eps = 1e-3
angle = 0.0
I = 0
J = 0
MAX_COUNT = 500

def maxElement():
    global I
    global J
    maxEl = 0
    for i in list(range(N)):
        for j in list(range(N)):
            el = A[i][j]
            if (i != j and abs(maxEl) < abs(el)):
                I = i
                J = j
                maxEl = el
    pass

def calculateAngle():
    global angle
    angle = 0.5 * atan(2*A[I][J]/(A[J][J] - A[I][I]))
    pass

def rotateMatrix():
    global A
    B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in list(range(N)):
        for j in list(range(N)):
            B[i][j] = A[i][j]
    c = cos(angle)
    s = sin(angle)
    A[I][J] = (pow(c, 2) - pow(s, 2)) * B[I][J] + s * c * (B[I][I] - B[J][J])
    A[J][I] = (pow(c, 2) - pow(s, 2)) * B[I][J] + s * c * (B[I][I] - B[J][J])
    A[I][I] = (pow(c, 2) * B[I][I] - 2 * c * s * B[I][J] + pow(s, 2) * B[J][J])
    A[J][J] = (pow(s, 2) * B[I][I] + 2 * c * s * B[I][J] + pow(c, 2) * B[J][J])
    for k in list(range(N)):
        if (k != I and k != J):
            A[I][k] = c * B[I][k] - s * B[J][k]
            A[k][I] = c * B[I][k] - s * B[J][k]
            A[J][k] = c * B[J][k] + s * B[I][k]
            A[k][J] = c * B[J][k] + s * B[I][k]
            # A[k][l] save
    pass

def checkEps():
    sumCurr = 0.0
    for i in list(range(N)):
        for j in list(range(N)):
            if (i != j):
                sumCurr += pow(A[i][j], 2)
    if (sumCurr < pow(eps, 2)):
        return False
    return True
    pass

def printMatrix(B=None):
    if not B:
        B = copy.copy(A)
    print("=========================================================================")
    for i in list(range(N)):
        print("|\t", "".join(["%.6f\t|\t" % (a) for a in B[i]]))
    print("=========================================================================\n")
    pass

if __name__ == "__main__":
    N = 3
    A = [[18, -6, -7], [-6, 6, 0], [-7, 0, 6]]
    print("Start matrix:")
    printMatrix()
    
    iteration = 0
    while (checkEps() and iteration < MAX_COUNT):
        maxElement()
        calculateAngle()
        rotateMatrix()
        iteration += 1
        
    print("Iterations:",  iteration, "\n")
    print("Finish matrix:")
    printMatrix()
    print("END!")

