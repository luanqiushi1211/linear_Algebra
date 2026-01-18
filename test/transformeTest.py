import numpy as np
import sys
import os
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from vectorpaint.vectorTranform import transform

def generate_transformed_basis_vectors(transformer, transform_type: str, **kwargs):
    """
    根据线性变换的种类生成变换后的基向量
    :param transformer: transform对象
    :param transform_type: 变换类型
    :param kwargs: 变换参数
    :return: 变换后的i_hat和j_hat基向量
    """
    # 获取变换矩阵
    matrix = transformer.create_transformation_matrix(transform_type, **kwargs)
    
    # 对基向量应用变换
    new_i_hat = matrix @ transformer.original_i_hat
    new_j_hat = matrix @ transformer.original_j_hat
    
    print(f"原始基向量: i_hat={transformer.original_i_hat}, j_hat={transformer.original_j_hat}")
    print(f"变换后基向量: i_hat={new_i_hat}, j_hat={new_j_hat}")
    
    return new_i_hat, new_j_hat


def draw_grid_from_basis_vectors(ax, i_hat, j_hat, grid_range=(-5, 6), alpha=0.3):
    """
    根据基向量绘制网格
    :param ax: matplotlib轴对象
    :param i_hat: 变换后的i基向量
    :param j_hat: 变换后的j基向量
    :param grid_range: 网格范围
    :param alpha: 透明度
    """
    # 绘制平行于i_hat的线（保持j系数不变，变化i系数）
    for j_coeff in range(grid_range[0], grid_range[1]):
        # 绘制平行于i_hat的线
        for i_coeff in range(grid_range[0], grid_range[1]-1):
            start_point = i_coeff * i_hat + j_coeff * j_hat
            end_point = (i_coeff + 1) * i_hat + j_coeff * j_hat
            ax.plot([start_point[0], end_point[0]], 
                   [start_point[1], end_point[1]], 
                   color='lightblue', alpha=alpha, linewidth=0.5)
    
    # 绘制平行于j_hat的线（保持i系数不变，变化j系数）
    for i_coeff in range(grid_range[0], grid_range[1]):
        # 绘制平行于j_hat的线
        for j_coeff in range(grid_range[0], grid_range[1]-1):
            start_point = i_coeff * i_hat + j_coeff * j_hat
            end_point = i_coeff * i_hat + (j_coeff + 1) * j_hat
            ax.plot([start_point[0], end_point[0]], 
                   [start_point[1], end_point[1]], 
                   color='lightgreen', alpha=alpha, linewidth=0.5)


def visualize_transform_with_grid(transformer, transform_type: str, **kwargs):
    """
    将变换后的基向量和网格在同一个图中展示
    :param transformer: transform对象
    :param transform_type: 变换类型
    :param kwargs: 变换参数
    """
    # 生成变换后的基向量
    new_i_hat, new_j_hat = generate_transformed_basis_vectors(transformer, transform_type, **kwargs)
    
    # 创建新的图形和轴
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 绘制从变换后基向量生成的网格
    draw_grid_from_basis_vectors(ax, new_i_hat, new_j_hat, grid_range=(-3, 4), alpha=0.3)
    
    # 绘制变换后的基向量（更粗的箭头以便观察）
    ax.quiver(0, 0, new_i_hat[0], new_i_hat[1], angles='xy', scale_units='xy', scale=1, 
              color='red', width=0.008, headwidth=3, headlength=4, label='变换后i基向量')
    ax.quiver(0, 0, new_j_hat[0], new_j_hat[1], angles='xy', scale_units='xy', scale=1, 
              color='blue', width=0.008, headwidth=3, headlength=4, label='变换后j基向量')
    
    # 绘制原始基向量（用较淡的颜色）
    ax.quiver(0, 0, transformer.original_i_hat[0], transformer.original_i_hat[1], 
              angles='xy', scale_units='xy', scale=1, color='darkred', alpha=0.5, 
              width=0.005, headwidth=2, headlength=3, label='原始i基向量')
    ax.quiver(0, 0, transformer.original_j_hat[0], transformer.original_j_hat[1], 
              angles='xy', scale_units='xy', scale=1, color='darkblue', alpha=0.5, 
              width=0.005, headwidth=2, headlength=3, label='原始j基向量')
    
    # 设置图形属性
    max_val = max(abs(new_i_hat).max(), abs(new_j_hat).max(), 5)
    margin = max_val * 0.2
    ax.set_xlim(-max_val-margin, max_val+margin)
    ax.set_ylim(-max_val-margin, max_val+margin)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.set_aspect('equal')
    ax.legend()
    ax.set_title(f'{transform_type} 变换后的基向量和网格', fontsize=14)
    
    plt.show()


def test_scale_transform(zoom_factor: float):
    """
    测试缩放变换
    :param zoom_factor: 缩放倍数
    """
    print(f"开始测试缩放变换，缩放倍数: {zoom_factor}")
    
    # 定义标准基向量
    i_hat = np.array([1, 0])
    j_hat = np.array([0, 1])
    
    # 创建变换对象
    transformer = transform(i_hat, j_hat, visualizer_type="basic")
    
    # 使用新方法展示缩放变换
    visualize_transform_with_grid(transformer, "scaling", scale_x=zoom_factor, scale_y=zoom_factor)
    
    print(f"缩放变换完成")


def test_rotation_transform(angle: float):
    """
    测试旋转变换
    :param angle: 旋转角度（弧度）
    """
    print(f"开始测试旋转变换，旋转角度: {angle} 弧度 ({np.degrees(angle)} 度)")
    
    # 定义标准基向量
    i_hat = np.array([1, 0])
    j_hat = np.array([0, 1])
    
    # 创建变换对象
    transformer = transform(i_hat, j_hat, visualizer_type="basic")
    
    # 使用新方法展示旋转变换
    visualize_transform_with_grid(transformer, "rotation", angle=angle)
    
    print(f"旋转变换完成")


def test_shear_transform(k: float, direction: str = 'x'):
    """
    测试剪切变换
    :param k: 剪切因子
    :param direction: 剪切方向 ('x' 或 'y')
    """
    print(f"开始测试剪切变换，剪切因子: {k}，方向: {direction}")
    
    # 定义标准基向量
    i_hat = np.array([1, 0])
    j_hat = np.array([0, 1])
    
    # 创建变换对象
    transformer = transform(i_hat, j_hat, visualizer_type="basic")
    
    # 使用新方法展示剪切变换
    visualize_transform_with_grid(transformer, "shearing", k=k, direction=direction)
    
    print(f"剪切变换完成")


if __name__ == "__main__":
    print("运行变换测试...")
    
    # 测试缩放变换
    test_scale_transform(2.0)
    
    # 测试旋转变换 (45度)
    test_rotation_transform(np.pi / 3)
    
    # 测试剪切变换
    test_shear_transform(0.5, 'x')
    
    print("所有测试完成")