import numpy as np
import scipy.linalg as sl

def QRLeastSquares():
    sick_matrix = sl.hilbert(15)
    a_0 = np.ones(15)
    y = sick_matrix @ a_0
    Q,R = np.linalg.qr(sick_matrix)
    a_1 = np.linalg.inv(sick_matrix.T @ sick_matrix)@sick_matrix.T@y
    """
    利用QR分解的方法求解最小二乘问题,solve_triangular函数可以求解上三角矩阵的线性方程组
    """
    a_2 = sl.solve_triangular(R,Q.T@y)

    deviation1 = np.linalg.norm(a_1-a_0)
    deviation2 = np.linalg.norm(a_2-a_0)

    print(f"希尔伯特矩阵是：{sick_matrix}")
    print(f"最小二乘结果向量是：{a_0}")
    print(f"Q,R分别是：{Q},{R}")
    print(f"求逆方法得到的最优解是：{a_1}，误差是：{deviation1}")
    print(f"QR分解方法得到的最优解是：{a_2}，误差是：{deviation2}")

if __name__ == "__main__":
    QRLeastSquares()
