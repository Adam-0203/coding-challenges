import numpy as np
n = 5
np.random.seed(5)


A = np.round(5*np.random.randn(n,n)) #définition de la matrice A
L = np.eye(n)  #définition de la matrice L




#définition de la matrice élémentaire M_i
def M(i,A):
    M = np.eye(n)
    for k in range(i,len(M)):
        M[k][i-1] = -A[k][i-1]/A[i-1][i-1]
        L[k][i-1] = A[k][i-1]/A[i-1][i-1] #construction de L au fur et à mesure

    return M


# transformation de A en U = M*A
def LU_factor(A):
    matrix = A.copy()
    for i in range(1,n):
        matrix = np.matmul(M(i,matrix),matrix)

    return L, matrix #qui est devenu U (triangulaire supérieur)
    

L, U = LU_factor(A)
LfoisU = np.matmul(L,U)

AmoinsLU = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        AmoinsLU[i][j] = A[i][j] - LfoisU[i][j]


print(np.linalg.norm(AmoinsLU, 1))
