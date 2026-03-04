import numpy as np
def cholesky(matrix:np.array)->np.array:    
    row,cloum = np.shape(matrix)
    L = np.zeros((row,cloum))
    sum = 0
    for i1 in range(0,row):
        for i2 in range(0,i1+1):
            sum=0
            for i3 in range(0,i2):
                sum = sum+L[i1][i3]*L[i2][i3]
            if i1!=i2:
                L[i1][i2] = (matrix[i1][i2]-sum)/L[i2][i2]
            else:
                cha = matrix[i1][i2]-sum
                L[i1][i2] = np.sqrt(cha)
   
    return L

if __name__ == "__main__":
    matrix = np.array([[4,2,2],[2,5,3],[2,3,6]])
    L_matrix = cholesky(matrix)
    L_matrix_np = np.linalg.cholesky(matrix)
    print(f"f原矩阵：{matrix}的Cholesky分解矩阵是：{L_matrix}")
    print(f"f原矩阵：{matrix}的使用numpy库方法的Cholesky分解矩阵是：{L_matrix_np}")


    