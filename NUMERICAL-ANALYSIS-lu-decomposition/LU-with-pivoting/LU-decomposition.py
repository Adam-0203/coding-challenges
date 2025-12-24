import numpy as np
n = 5
np.random.seed(5)

piv = np.eye(n)
A = np.round(5*np.random.randn(n,n)) #définition de la matrice A
L = np.eye(n)  #définition de la matrice L
safeA = A.copy()

#définition de la matrice élémentaire M_i
def M(i,A):
    M = np.eye(n)
    for k in range(i,len(M)):
        M[k][i-1] = -A[k][i-1]/A[i-1][i-1]
        L[k][i-1] = A[k][i-1]/A[i-1][i-1] #construction de L au fur et à mesure

    return M

def permuter_L(i,j,k):
    for w in range(k):
        L[i][w],L[j][w] = L[j][w],L[i][w]
    
# transformation de A en U = M*A
def LU_factor(A):
    for i in range(1,n):
        indice_max = i-1
        for k in range(i,n):
            if abs(A[k][i-1])>abs(A[indice_max][i-1]):
                indice_max = k
        
        A[[indice_max,i-1]] = A[[i-1,indice_max]]
        piv[[indice_max,i-1]] = piv[[i-1,indice_max]]
        if i>1:
            permuter_L(indice_max,i-1,i-1)
        
        A = np.matmul(M(i,A),A)


    return L, A #qui est devenu U (triangulaire supérieur)
    

L, U = LU_factor(A)

LfoisU = np.matmul(L,U)
print(np.matmul(piv,safeA))
print(LfoisU)
