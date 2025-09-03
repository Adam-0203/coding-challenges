Mat= [[0,0,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0]]

def voisin_vivant(Mat,i,j):
    voisin = []
    row = range(0,len(Mat))
    col = range(0,len(Mat))
    if (i-1 in row) and (j-1 in col): voisin.append(Mat[i-1][j-1])
    if (i-1 in row) and (j in col): voisin.append(Mat[i-1][j])
    if (i-1 in row) and (j+1 in col): voisin.append(Mat[i-1][j+1])
    if (i in row) and (j-1 in col): voisin.append(Mat[i][j-1])
    if (i in row) and (j+1 in col): voisin.append(Mat[i][j+1])
    if (i+1 in row) and (j-1 in col): voisin.append(Mat[i+1][j-1])
    if (i+1 in row) and (j in col): voisin.append(Mat[i+1][j])
    if (i+1 in row) and (j+1 in col): voisin.append(Mat[i+1][j+1])

    return voisin.count(1)


def nouveau(Mat,i,j):
    if (Mat[i][j] == 0) and (voisin_vivant(Mat,i,j) == 3):
        return 1
    elif (Mat[i][j] == 1) and (voisin_vivant(Mat,i,j) in (2,3)):
        return 1
    elif (Mat[i][j] == 1)  and (voisin_vivant(Mat,i,j)<2 or voisin_vivant(Mat,i,j)>3):
        return 0
    else: return Mat[i][j]

 
def algo(Mat,step):
    print(Mat)
    for i in range(step):
        Mat_copy = [[Mat[u][v] for v in range(len(Mat))] for u in range(len(Mat))]
        for p in range(len(Mat)):
            for q in range(len(Mat)):
                Mat[p][q] = nouveau(Mat_copy,p,q)
        print(Mat)
        

algo(Mat,4)
