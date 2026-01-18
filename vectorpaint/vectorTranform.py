import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Union
from vector_visualizer import BasisVector


TRANSFORM_KINDS = [
    "identity", "rotation", "scaling", "reflection", "shearing", "projection", "singular"
]

class transform(BasisVector):
    """
    线性变换类，继承自基向量类
    实现基变换、矩阵乘向量运算和线性变换的可视化
    支持的变换类型包括：恒等变换、旋转变换、缩放变换、反射变换、剪切变换、投影变换、奇异变换
    """

    def init(self, i_hat: np.ndarray, j_hat: np.ndarray, visualizer_type: str = "basic"):
        """
        初始化线性变换类
        :param i_hat: i基向量
        :param j_hat: j基向量
        :param visualizer_type: 可视化器类型
        """
        super().init(i_hat, j_hat, visualizer_type)

    def get_standard_matrix(self) -> np.ndarray:
        """
        获取标准变换矩阵（以基向量作为列向量构成的矩阵）
        :return: 2x2变换矩阵
        """
        # 变换矩阵由变换后的基向量组成
        # 变换矩阵 = [T(i_hat), T(j_hat)]
        matrix = np.column_stack((self.original_i_hat, self.original_j_hat))
        return matrix

    def apply_transformation(self, vector: np.ndarray) -> np.ndarray:
        """
        应用线性变换到向量
        :param vector: 待变换的2D向量
        :return: 变换后的向量
        """
        # 使用变换矩阵乘以向量进行变换
        matrix = self.get_standard_matrix()
        transformed_vector = matrix @ vector
        return transformed_vector

    def create_transformation_matrix(self, transform_type: str, **kwargs) -> np.ndarray:
        """
        创建特定类型的变换矩阵
        :param transform_type: 变换类型
        :param kwargs: 变换参数
        :return: 2x2变换矩阵
        """
        if transform_type == "identity":
            # 恒等变换矩阵
            return np.array([[1, 0], [0, 1]])
        elif transform_type == "rotation":
            # 旋转变换矩阵
            angle = kwargs.get('angle', 0)
            cos_a = np.cos(angle)
            sin_a = np.sin(angle)
            return np.array([[cos_a, -sin_a], [sin_a, cos_a]])
        elif transform_type == "scaling":
            # 缩放变换矩阵
            scale_x = kwargs.get('scale_x', 1)
            scale_y = kwargs.get('scale_y', 1)
            return np.array([[scale_x, 0], [0, scale_y]])
        elif transform_type == "reflection":
            # 反射变换矩阵 - 默认关于x轴反射
            axis = kwargs.get('axis', 'x')
            if axis == 'x':
                return np.array([[1, 0], [0, -1]])  # 关于x轴反射
            elif axis == 'y':
                return np.array([[-1, 0], [0, 1]])  # 关于y轴反射
            elif axis == 'origin':
                return np.array([[-1, 0], [0, -1]])  # 关于原点反射
            else:  # 关于y=x线反射
                return np.array([[0, 1], [1, 0]])
        elif transform_type == "shearing":
            # 剪切变换矩阵
            k = kwargs.get('k', 1)  # 剪切因子
            direction = kwargs.get('direction', 'x')  # 剪切方向
            if direction == 'x':
                # x方向剪切
                return np.array([[1, k], [0, 1]])
            else:
                # y方向剪切
                return np.array([[1, 0], [k, 1]])
        elif transform_type == "projection":
            # 投影变换矩阵 - 投影到x轴或y轴
            axis = kwargs.get('axis', 'x')
            if axis == 'x':
                return np.array([[1, 0], [0, 0]])  # 投影到x轴
            else:
                return np.array([[0, 0], [0, 1]])  # 投影到y轴
        elif transform_type == "singular":
            # 奇异变换矩阵（行列式为0）
            return np.array([[1, 2], [2, 4]])  # 一个行列式为0的矩阵
        else:
            # 默认返回恒等变换矩阵
            return np.array([[1, 0], [0, 1]])

    def visualize_transformation(self, vector: np.ndarray, transform_type: str, **kwargs):
        """
        可视化线性变换过程
        :param vector: 待变换的向量
        :param transform_type: 变换类型
        :param kwargs: 变换参数
        """
        # 获取变换矩阵
        matrix = self.create_transformation_matrix(transform_type, **kwargs)

        # 计算变换后的向量
        original_vector = vector.copy()
        transformed_vector = matrix @ vector

        # 显示变换前的向量
        print(f"原始向量: [{original_vector[0]}, {original_vector[1]}]")
        print(f"变换后向量: [{transformed_vector[0]}, {transformed_vector[1]}]")

        # 使用可视化器显示变换过程
        self.visualizer.show_vectors(
            (0, 0, original_vector[0], original_vector[1], 'blue'),      # 原始向量（蓝色）
            (0, 0, transformed_vector[0], transformed_vector[1], 'red')   # 变换后向量（红色）
        )

        return transformed_vector

    def transform_basis_vectors(self, transform_type: str, **kwargs) -> Tuple[np.ndarray, np.ndarray]:
        """
        变换基向量
        :param transform_type: 变换类型
        :param kwargs: 变换参数
        :return: 变换后的i_hat和j_hat
        """
        # 获取变换矩阵
        matrix = self.create_transformation_matrix(transform_type, **kwargs)

        # 对基向量应用变换
        new_i_hat = matrix @ self.original_i_hat
        new_j_hat = matrix @ self.original_j_hat

        return new_i_hat, new_j_hat

    def visualize_basis_transformation(self, transform_type: str, **kwargs):
        """
        可视化基向量的变换
        :param transform_type: 变换类型
        :param kwargs: 变换参数
        """
        # 获取变换后的基向量
        new_i_hat, new_j_hat = self.transform_basis_vectors(transform_type, **kwargs)

        self.visualizer.show_vectors (
            (0, 0, self.original_i_hat[0], self.original_i_hat[1], 'red','原始i帽'),    # 原始i基向量（红色）
            (0, 0, self.original_j_hat[0], self.original_j_hat[1], 'blue','原始j帽'),
           )   # 原始j基向量（蓝色）)   

        # 显示变换前后的基向量
        self.visualizer.draw_grid_from_basis_vectors(
            (0, 0, self.original_i_hat[0], self.original_i_hat[1], 'red','原始i帽'),    # 原始i基向量（红色）
            (0, 0, self.original_j_hat[0], self.original_j_hat[1], 'blue','原始j帽'),   # 原始j基向量（蓝色）
            (0, 0, new_i_hat[0], new_i_hat[1], 'orange','变换后i帽'),                     # 变换后i基向量（橙色）
            (0, 0, new_j_hat[0], new_j_hat[1], 'cyan','变换后j帽'),                        # 变换后j基向量（青色）
            new_hat=(np.array([new_i_hat[0], new_i_hat[1]]), np.array([new_j_hat[0], new_j_hat[1]])) # 变换后的基向量
        )

        

if __name__ == '__main__':
    i_hat = np.array([1, 0])
    j_hat = np.array([0, 1])
    trans  = transform(i_hat,j_hat)
    trans.visualize_basis_transformation("scaling", scale_x=2, scale_y=2)#缩放变换
    trans.visualize_basis_transformation("rotation", angle=np.pi / 4)#旋转变换
    trans.visualize_basis_transformation("shearing", k=0.5, direction='x')#剪切变换
        