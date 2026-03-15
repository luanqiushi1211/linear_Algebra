import numpy as np
def PCAanalysis(A:np.array,K)->np.array:
    row,col = np.shape(A)
    mean_vec = np.zeros((1,col))
    cen_matrix = np.zeros((row,col))
    dr_matrix = []
    for i in range(col):
        mean_vec[0][i] = np.mean(A[:,i])
    for j in range(row):
        item = A[j,:]- mean_vec[0,:]
        cen_matrix[j,:] = item
    cov_matrix = (1/(row-1))*cen_matrix.T @ cen_matrix
    eigval,eigvec = np.linalg.eig(cov_matrix)
    sig_sort = sortEig(eigval)
    tp_list =  sig_sort[:K]
    for i,tp in enumerate(tp_list):
        index = tp[0]
        dr_matrix.append(eigvec[:,index])    
    dr_matrix = np.array(dr_matrix).T
    res = cen_matrix @ dr_matrix
    return res


def sortEig(eigval):
    res = []
    for index,eig in enumerate(eigval):
        item = [index,eig]
        if len(res)==0:
            res.append(item)
        else:
            for index2,i in enumerate(res):
                if eig > i[1]:
                    res.insert(index2,item)
    return res





if __name__ == "__main__":
    A = np.random.randn(2,2)
    """A = np.array([[5,2,0],[2,2,0],[0,0,3]])"""
    K = 2
    res = PCAanalysis(A,K)
    print(f"矩阵：{A}保留前{K}个主成分的降维矩阵是：{res}")
    



