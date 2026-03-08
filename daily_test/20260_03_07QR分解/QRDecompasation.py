import numpy as np
def QRDecompasation(matrix:np.array):
    row,col = np.shape(matrix)
    Q = np.zeros((row,col))
    R = np.zeros((row,col))
    for i1 in range(col):
        u = matrix[:,i1]
        for i2 in range(i1):
            shadow = u @ Q[:,i2]
            R[i2][i1] = shadow
            u =u-shadow * Q[:,i2]
        R[i1][i1] = np.linalg.norm(u)
        q = u/np.linalg.norm(u)
        Q[:,i1] = q
    return (Q,R)
    
if __name__ == "__main__":
    matrix = np.array([[3,1],[4,1]])
    Q,R = QRDecompasation(matrix)
    print(f"{matrix}的QR分解后的Q矩阵是：{Q}R矩阵是：{R}")