import numpy as np
from matplotlib import pyplot as plt

from vector_visualizer import BasisVector

class DeterminantVisualizer(BasisVector):
    """
    行列式可视化类,继承自 BasisVector,用于展示矩阵 A 的行列式值。
    """
    def __init__(self, i_hat:np.ndarray,j_hat:np.ndarray,matrix:np.ndarray,visualizer_type:str):
        """
        初始化 DeterminantVisualizer 类。

        参数:
        - i_hat: 单位向量 i_hat,表示 x 轴方向的单位向量。
        - j_hat: 单位向量 j_hat,表示 y 轴方向的单位向量。
        - visualizer_type: 可视化类型,可以是 '2D' 或 '3D'。
        - matrix: 2x2 矩阵,用于计算行列式值。
        """
        super().__init__(i_hat,j_hat,visualizer_type)
        # 由i_hat和j_hat组成变换矩阵A，其中i_hat作为第一列，j_hat作为第二列
        self.A = matrix
        # 计算行列式
        self.det_A = self.A[0,0]*self.A[1,1]-self.A[0,1]*self.A[1,0]
        
    
    def determinant(self):
        
        self.visualizer.show_vectors (
            (0, 0, self.original_i_hat[0], self.original_i_hat[1], 'red','原始i帽'),    # 原始
            (0, 0, self.original_j_hat[0], self.original_j_hat[1], 'blue','原始j帽'),
           )   # 原始j基向量（蓝色）)   
        
        self.visualizer.draw_grid_from_basis_vectors(
            (0,0,self.A [0,0],self.A[0,1],'green','行列式i帽'),
            (0,0,self.A[1,0],self.A[1,1],'orange','行列式j帽'),  
            (0,0,0,0,'purple','行列式的值='+str(self.det_A)),
            new_hat=(np.array([self.A[0,0], self.A[0,1]]), np.array([self.A[1,0], self.A[1,1]])) # 变换后
            
        )
if __name__ == '__main__':
    i_hat = np.array([1, 0])
    j_hat = np.array([0, 1])
    A = np.array([[2, 2],
                      [1, 3]])
    U, S_values, Vt = np.linalg.svd(A)
    V = Vt.T
    det1  = DeterminantVisualizer(i_hat,j_hat,A,'2D')
    A2 = A @ V
    det2 = DeterminantVisualizer(i_hat,j_hat,A2,'2D')
    det1.determinant()
    det2.determinant()
        
       
