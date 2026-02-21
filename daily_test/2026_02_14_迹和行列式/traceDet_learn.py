import trace
import numpy as np

def traceDet():    
    matrix_data = np.random.rand(5,5)
    print(f"矩阵matrix={matrix_data}")
    trace_matrix = np.trace(matrix_data)
    det_matrix = np.linalg.det(matrix_data)
    eigvalue = np.linalg.eigvals(matrix_data)
    eigvalue_sum = np.sum(eigvalue)
    eigvalue_prod = np.prod(eigvalue)
    if(np.isclose(eigvalue_sum,trace_matrix)):
        print(f"矩阵的迹和特征值之和相等，迹={trace_matrix}，特征值={eigvalue}")
    if(np.isclose(det_matrix,eigvalue_prod) ):
        print(f"矩阵的行列式与特征值乘积相等，行列式={det_matrix}，特征值之积={eigvalue_prod}")


if __name__ == "__main__":
    traceDet()