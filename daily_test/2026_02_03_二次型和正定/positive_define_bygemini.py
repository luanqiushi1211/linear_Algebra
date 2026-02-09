import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # 显式导入，防止某些版本报错

def is_positive_definite(matrix: np.array) -> bool:
    """
    判断矩阵是否正定
    """
    # 检查是否对称（二次型矩阵通常应是对称的）
    if not np.allclose(matrix, matrix.T):
        print("提示：非对称矩阵，将计算其对称部分的二次型")
    
    try:
        # 检查特征值
        eigenvalues, _ = np.linalg.eig(matrix)
        # 只要所有特征值大于0，即为正定
        if np.all(eigenvalues > 0):
            return True
        return False
    except np.linalg.LinAlgError:
        return False

def draw_positive_definite(matrix: np.array):
    # 1. 判断是否正定
    if not is_positive_definite(matrix):
        print(f"矩阵 \n{matrix} \n不是正定矩阵，跳过绘图。")
        return

    print(f"矩阵 \n{matrix} \n是正定矩阵，准备绘图...")
    
    rows, cols = matrix.shape
    if rows != 2 or cols != 2:
        print("为了演示方便，本代码仅支持 2x2 矩阵的 3D 绘图")
        return

    # 2. 生成网格数据 (Meshgrid) —— 这是画曲面的关键！
    # 创建 X 和 Y 的一维数组
    x_line = np.linspace(-3, 3, 50)
    y_line = np.linspace(-3, 3, 50)
    
    # 生成二维网格矩阵
    # X, Y 的形状现在都是 (50, 50)
    X, Y = np.meshgrid(x_line, y_line) 
    
    # 3. 计算对应的 Z 值 (二次型 f = x^T * A * x)
    # 矩阵 A = [[a, b], [c, d]]
    # 二次型展开公式: f(x,y) = a*x^2 + (b+c)*x*y + d*y^2
    
    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]
    
    # 利用 numpy 的广播机制直接计算矩阵，无需循环，速度极快
    Z = a * X**2 + (b + c) * X * Y + d * Y**2
    
    # 4. 绘图
    plot_3d_surface(X, Y, Z)

def plot_3d_surface(X, Y, Z):
    """
    绘制3D曲面图
    X, Y, Z 必须都是二维数组
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # cmap='viridis' 是颜色映射，alpha 是透明度
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolor='none')
    
    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')
    ax.set_zlabel('f(x)')
    ax.set_title('Positive Definite Quadratic Form: $x^T A x$')
    
    # 添加颜色条
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

if __name__ == "__main__":
    # 正定矩阵例子 (碗状，开口向上)
    matrix_1 = np.array([[2, 1], 
                         [1, 2]])
    
    # 不定矩阵例子 (马鞍面，虽然题目只画正定，但用来测试逻辑)
    # 注意：matrix_2 [[1, 2], [2, 1]] 特征值为 3 和 -1，不是正定矩阵
    matrix_2 = np.array([[1, 2], 
                         [2, 1]])
    
    draw_positive_definite(matrix_1)
    print("-" * 20)
    draw_positive_definite(matrix_2)