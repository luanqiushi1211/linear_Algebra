"""
编写一个 Python 脚本，完成以下功能：定义判别函数： 
编写一个函数 is_positive_definite(matrix)，
它接收一个 numpy 矩阵作为输入，利用 特征值 (Eigenvalues) 的方法判断其是否为正定矩阵，
并返回布尔值。提示：使用 np.linalg.eigvals()测试与验证：矩阵 A: [[2, 1], [1, 2]]
矩阵 B: [[1, 2], [2, 1]]分别打印这两个矩阵是否为正定矩阵。可视化（加分项）：
选择上述那个正定的矩阵，将其作为二次型 $f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$ 的系数矩阵。
利用 matplotlib 绘制该二次型的 3D 曲面图（范围可取 $x, y \in [-3, 3]$）。预期结果：
你应该能看到一个开口朝上的“碗”。
"""
import numpy as np
from matplotlib import pyplot as plt
from pandas.core.arrays import boolean

def is_positive_definite(matrix:np.array)->boolean:
    res = False
    eigenvalues,eigenvectors = np.linalg.eig(matrix)
    row,col = eigenvectors.shape
    """print("特征值集合：",eigenvalues)
    print("特征向量组",eigenvectors)
    print("特征向量的数量：",col)"""
    """for i in range(0,col):
        print("特征向量是",eigenvectors[:,i])"""
    if np.all(eigenvalues>0):
        res = True
    return res



def draw_positive_definite(matrix:np.array):
    res = is_positive_definite(matrix)
    if(res):
        print("是正定矩阵")
        x = {}
        rows,cols = matrix.shape
        if rows!=cols:
            print("系数矩阵不是方阵，无法作为二次型系数矩阵")
            return
        else:
            for i in range(0,cols):            
                x[i] = np.linspace(-3,3,100) 
            print(x[0][0])   

        
    else:
        print("不是正定矩阵")
    
    
    

if __name__ == "__main__":
    matrix_1 = np.array([[2,1],[1,2]])
    matrix_2 = np.array([[1,2],[2,1]])
    draw_positive_definite(matrix_1)
    draw_positive_definite(matrix_2)
