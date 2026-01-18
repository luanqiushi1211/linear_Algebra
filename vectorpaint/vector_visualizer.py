import numpy as np
from matplotlib import pyplot as plt
from typing import List, Tuple, Union
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial Unicode MS', 'Microsoft YaHei']
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义常量
COLORS = ['blue', 'red', 'green', 'yellow']
GRID_RANGE = range(-5, 6, 1)

class VectorVisualizer:
    """向量可视化基类"""
    
    @classmethod
    def show_vectors(cls, *vector_data: Tuple, auto_show: bool = True):
        """
        绘制向量
        :param vector_data: 可变数量的元组，每个元组格式为 (start_x, start_y, dx, dy, color) 或 (start_x, start_y, dx, dy) 或 (dx, dy)
        :param auto_show: 是否自动显示图形，默认为True
        :return: 返回matplotlib轴对象，用于进一步自定义
        """
        
        fig, ax = plt.subplots()
        
        for vector_info in vector_data:
            if len(vector_info) >= 6:
                start_x, start_y, dx, dy, color, label = vector_info
                ax.quiver(start_x, start_y, dx, dy, angles='xy', 
                         scale_units='xy', scale=1, color=color, label=label)
            elif len(vector_info) >= 5:
                start_x, start_y, dx, dy, color = vector_info
                ax.quiver(start_x, start_y, dx, dy, angles='xy', 
                         scale_units='xy', scale=1, color=color)
            elif len(vector_info) >= 4:
                start_x, start_y, dx, dy = vector_info
                ax.quiver(start_x, start_y, dx, dy, angles='xy', 
                         scale_units='xy', scale=1)
            elif len(vector_info) == 2:
                dx, dy = vector_info
                ax.quiver(0, 0, dx, dy, angles='xy', scale_units='xy', scale=1)
        
        ax.set_xticks(GRID_RANGE)
        ax.set_yticks(GRID_RANGE)
        ax.grid()
        
        # 检查是否有带标签的向量，如果有则显示图例
        has_labels = any(len(vector_info) >= 6 for vector_info in vector_data)
        if has_labels:
            ax.legend()
            
        if auto_show:
            plt.show()
            
        return ax
    def draw_grid_from_basis_vectors(cls, *vector_data: Tuple, new_hat: Tuple[np.ndarray, np.ndarray] = None, alpha: float = 0.5, auto_show: bool = True):
        """
        从基向量绘制网格
        :param vector_data: 可变数量的元组，每个元组格式为 (start_x, start_y, dx, dy, color) 或 (start_x, start_y, dx, dy) 或 (dx, dy)
        :param new_hat: 新的基向量，格式为 (i_hat, j_hat)，如果为None则使用默认基向量
        :param alpha: 网格线透明度
        :param auto_show: 是否自动显示图形，默认为True
        :return: 返回matplotlib轴对象，用于进一步自定义
        """
        ax = cls.show_vectors(*vector_data, auto_show=False)
        if new_hat is None:
            i_hat = np.array([1, 0])
            j_hat = np.array([0, 1])
        else:
            i_hat, j_hat = new_hat
            
        # 绘制平行于i_hat的网格线（保持j系数不变，变化i系数）
        for j_coeff in range(min(GRID_RANGE), max(GRID_RANGE)+1):
            for i_coeff in range(min(GRID_RANGE), max(GRID_RANGE)):
                start_point = i_coeff * i_hat + j_coeff * j_hat
                end_point = (i_coeff + 1) * i_hat + j_coeff * j_hat
                ax.plot([start_point[0], end_point[0]], 
                       [start_point[1], end_point[1]], 
                       color='lightblue', alpha=alpha, linewidth=0.5)
        
        # 绘制平行于j_hat的网格线（保持i系数不变，变化j系数）
        for i_coeff in range(min(GRID_RANGE), max(GRID_RANGE)+1):
            for j_coeff in range(min(GRID_RANGE), max(GRID_RANGE)):
                start_point = i_coeff * i_hat + j_coeff * j_hat
                end_point = i_coeff * i_hat + (j_coeff + 1) * j_hat
                ax.plot([start_point[0], end_point[0]], 
                       [start_point[1], end_point[1]], 
                       color='lightgreen', alpha=alpha, linewidth=0.5)
        
        if auto_show:
            plt.show()
            
        return ax
                
    


class BasicVectorVisualizer(VectorVisualizer):
    """基础向量可视化器"""
    pass

class AnimatedVectorVisualizer(VectorVisualizer):
    """动画向量可视化器"""
    
    @classmethod
    def show_vector_construction(cls, i_hat: np.ndarray, j_hat: np.ndarray, vector: np.ndarray):
        """展示向量构建过程的动画效果"""
        i_zoom = vector[0]
        j_zoom = vector[1]
        
        # 缩放i基向量
        scaled_i = i_hat * i_zoom
        cls.show_vectors(
            (0, 0, scaled_i[0], scaled_i[1], 'red'), 
            (0, 0, j_hat[0], j_hat[1], 'blue')
        )
        
        # 缩放j基向量
        scaled_j = j_hat * j_zoom
        cls.show_vectors(
            (0, 0, scaled_i[0], scaled_i[1], 'red'), 
            (0, 0, scaled_j[0], scaled_j[1], 'blue')
        )
        
        # 平移j基向量
        cls.show_vectors(
            (0, 0, scaled_i[0], scaled_i[1], 'red'), 
            (scaled_i[0], 0, scaled_j[0], scaled_j[1], 'blue')
        )
        
        # 绘制结果向量
        result_vector = scaled_i + scaled_j
        cls.show_vectors(
            (0, 0, scaled_i[0], scaled_i[1], 'red'), 
            (scaled_i[0], 0, scaled_j[0], scaled_j[1], 'blue'),
            (0, 0, result_vector[0], result_vector[1], 'green')
        )

class VectorVisualizerFactory:
    """向量可视化器工厂类"""
    
    @staticmethod
    def create_visualizer(visualizer_type: str = "basic") -> VectorVisualizer:
        """
        根据类型创建向量可视化器
        :param visualizer_type: 可视化器类型 ("basic" 或 "animated")
        :return: 向量可视化器实例
        """
        if visualizer_type == "basic":
            return BasicVectorVisualizer()
        elif visualizer_type == "animated":
            return AnimatedVectorVisualizer()
        else:
            return BasicVectorVisualizer()

class BasisVector:
    """基向量类"""
    
    def __init__(self, i_hat: np.ndarray, j_hat: np.ndarray, visualizer_type: str = "animated"):
        """
        初始化基向量
        :param i_hat: i基向量
        :param j_hat: j基向量
        :param visualizer_type: 可视化器类型
        """
        self.original_i_hat = i_hat.copy()
        self.original_j_hat = j_hat.copy()
        self.visualizer = VectorVisualizerFactory.create_visualizer(visualizer_type)

    def show_basis_vector(self):
        """绘制基向量"""
        self.visualizer.show_vectors(
            (0, 0, self.original_i_hat[0], self.original_i_hat[1], 'red'), 
            (0, 0, self.original_j_hat[0], self.original_j_hat[1], 'blue')
        )

    def show_vector_construction(self, vector: np.ndarray):
        """
        展示一个向量是如何通过基向量的缩放和加减操作得到的
        """
        if isinstance(self.visualizer, AnimatedVectorVisualizer):
            self.visualizer.show_vector_construction(self.original_i_hat, self.original_j_hat, vector)
        else:
            # 基础可视化
            i_zoom = vector[0]
            j_zoom = vector[1]
            scaled_i = self.original_i_hat * i_zoom
            scaled_j = self.original_j_hat * j_zoom
            result_vector = scaled_i + scaled_j
            self.visualizer.show_vectors(
                (0, 0, scaled_i[0], scaled_i[1], 'red'), 
                (0, 0, scaled_j[0], scaled_j[1], 'blue'),
                (0, 0, result_vector[0], result_vector[1], 'green')
            )

    def zoom_vector(self, vector: np.ndarray, zoom_factor: float):
        """
        缩放向量并展示过程
        """
        original_vector = vector.copy()
        zoomed_vector = vector * zoom_factor
        
        # 显示原始向量
        self.visualizer.show_vectors((0, 0, original_vector[0], original_vector[1]))
        
        # 显示缩放过程
        self.visualizer.show_vectors(
            (0, 0, original_vector[0], original_vector[1], 'blue'),
            (0, 0, zoomed_vector[0], zoomed_vector[1], 'red')
        )
        
        # 显示缩放后的基向量
        scaled_i = self.original_i_hat * vector[0] * zoom_factor
        scaled_j = self.original_j_hat * vector[1] * zoom_factor
        self.visualizer.show_vectors(
            (0, 0, scaled_i[0], scaled_i[1], 'red'), 
            (0, 0, scaled_j[0], scaled_j[1], 'blue')
        )
        
        # 显示缩放后的向量合成
        self.visualizer.show_vectors(
            (0, 0, scaled_i[0], scaled_i[1], 'red'), 
            (scaled_i[0], 0, scaled_j[0], scaled_j[1], 'blue'),
            (0, 0, zoomed_vector[0], zoomed_vector[1], 'green')
        )

    def add_vectors(self, *vectors: np.ndarray):
        """
        展示多个向量的加法过程
        """
        if not vectors:
            return
            
        # 显示所有向量
        vector_list = []
        for i, vector in enumerate(vectors):
            color = COLORS[i % len(COLORS)]
            vector_list.append((0, 0, vector[0], vector[1], color))
        
        self.visualizer.show_vectors(*vector_list)

        # 逐步相加
        current_sum = vectors[0].copy()
        for i in range(1, len(vectors)):
            next_vector = vectors[i]
            prev_sum = current_sum.copy()
            current_sum = prev_sum + next_vector
            
            self.visualizer.show_vectors(
                (0, 0, prev_sum[0], prev_sum[1], 'blue'),
                (prev_sum[0], prev_sum[1], next_vector[0], next_vector[1], 'red'),
                (0, 0, current_sum[0], current_sum[1], 'green')
            )
        
        # 最终结果
        self.visualizer.show_vectors((0, 0, current_sum[0], current_sum[1], 'green'))

if __name__ == '__main__':
    i_hat = np.array([1, 0])
    j_hat = np.array([0, 1])
    vector1 = np.array([-1, 2])
    vector2 = np.array([3, 4])
    vector3 = np.array([-2, 1])

    # 使用工厂模式创建不同类型的可视化器
    basis_vector_animated = BasisVector(i_hat, j_hat, visualizer_type="animated")
    basis_vector_basic = BasisVector(i_hat, j_hat, visualizer_type="basic")

    basis_vector_animated.zoom_vector(vector1, -2)
    
