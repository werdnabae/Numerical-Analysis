import time
import numpy as np  

startTime = time.time() #records the time when the program starts executing
mul = 0
add = 0

def naive(A, B): #multiplies matrices using naive method
    # Global variables used for multiplication and addition count
    global mul 
    global add

    result = np.zeros(A.shape)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            result[i][j] = np.dot(A[i], B[:, j])
            mul += A.shape[1]
            add += A.shape[1] - 1
    return result

def strassen(A, B):
    n = len(A)

    # Global variables for multiplication and addition count
    global mul
    global add

    if len(A) == 32: # Base case when matrix is 32x32
        return naive(A, B)

    half = n // 2 #defines the half length of matrices

    # Sub-matrices
    a11 = A[:half, :half]
    a12 = A[:half, half:]
    a21 = A[half:, :half]
    a22 = A[half:, half:]

    b11 = B[:half, :half]
    b12 = B[:half, half:]
    b21 = B[half:, :half]
    b22 = B[half:, half:]

    # creates all m matrices
    m1  = strassen(a11 + a22, b11 + b22)
    add = add + 2 * half * half

    m2  = strassen(a21 + a22, b11)
    add += half * half

    m3 = strassen(a11, b12 - b22)
    add += half * half  

    m4 = strassen(a22, b21 - b11)
    add += half * half

    m5 = strassen(a11 + a12, b22)
    add += half * half 

    m6 = strassen(a21 - a11, b11 + b12) 
    add += 2 * half * half

    m7 = strassen(a12 - a22, b21 + b22)
    add += + 2 * half * half

    # Puts all m matrices together
    C = np.zeros(A.shape)
    C[:half, :half] = m1 + m4 - m5 + m7
    C[:half, half:] = m3 + m5
    C[half:, :half] = m2 + m4
    C[half:, half:] = m1 - m2 + m3 + m6
    add += 8 * half * half

    return C

# Empty lists for 2 matrices of dimension 2^9 x 2^9
matrix1 = np.zeros((2**9, 2**9))
matrix2 = np.zeros((2**9, 2**9))

for i in range(len(matrix1)): # Creates first 2^9 random matrix 
    for j in range(len(matrix1)):
        matrix1[i][j] = np.random.rand() * 4 - 2
        matrix2[i][j] = np.random.rand() * 4 - 2

matrixNaive = naive(matrix1, matrix2) # 2^9 matrix muliplaction using naive method
print("%d multiplications, %d additions" % (mul, add))
mul = 0
add = 0

matrixStrassen = strassen(matrix1, matrix2) # 2^9 matrix muliplication using Strassen method 
print("%d multiplications, %d additions" % (mul, add))
mul = 0
add = 0

# Empty lists for 2 matrices of dimension 2^12 x 2^12
matrix3 = np.zeros((2**12, 2**12))
matrix4 = np.zeros((2**12, 2**12))

for i in range(len(matrix3)): # Creates first 2^12 random matrix 
    for j in range(len(matrix3)):
        matrix3[i][j] = np.random.rand() * 4 - 2
        matrix4[i][j] = np.random.rand() * 4 - 2

matrixNaive2 = naive(matrix3, matrix4) # 2^12 matrix muliplaction using naive method
print("%d multiplications, %d additions" % (mul, add))
mul = 0
add = 0

matrixStrassen2 = strassen(matrix3, matrix4) # 2^12 matrix muliplication using Strassen method 
print("%d multiplications, %d additions" % (mul, add))

endTime = time.time() #records the time when the program stops      
print("Execution time:", (endTime - startTime), "seconds") #prints the time in seconds taken for the program to execute