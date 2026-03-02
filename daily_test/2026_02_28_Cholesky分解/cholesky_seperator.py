import numpy as np
def cholesky(matrix:np.array)->np.array:    
    row,cloum = np.shape(matrix)
    L = np.eye(row,cloum)
    sum1 = 0
    for i1 in range(0,cloum):
        L[i1][i1] = np.sqrt(matrix[i1][i1]-sum1)
        sum1 = 0
        for i2 in range(0,i1+1):
            if i1 == cloum-1:
                break
            sum2 = 0
            for i3 in range(0,i2-1):
                sum2 = sum2+L[i1+1][i3]*L[i2][i3]
            L[i1+1][i2] = (matrix[i1+1][i2]-sum2)/L[i2][i2]
            sum1 = sum1+np.square(L[i1+1][i2])
    return L

if __name__ == "__main__":
    matrix = np.array([[4,2,2],[2,5,3],[2,3,6]])
    L_matrix = cholesky(matrix)
    print(f"f原矩阵：{matrix}的Cholesky分解矩阵是：{L_matrix}")


    