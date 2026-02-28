import numpy as np
from matplotlib import pyplot as plt
import time as tm
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
def inverse(matrix:np.array)->np.array:
    row,colum = np.shape(matrix)
    identity_matrix = np.eye(row,colum)
    augment_matrix = np.hstack((matrix,identity_matrix))
    a_row,a_colum = np.shape(augment_matrix)
    for colum_index in range(colum):
        main_element = augment_matrix[:,colum_index][colum_index]
        if main_element != 1:
                augment_matrix[colum_index] = augment_matrix[colum_index]*(1/main_element)
        for row_index,colum_data in enumerate(augment_matrix[:,colum_index]):
            if row_index == colum_index:
                continue
            multiple = -1*(colum_data/main_element)
            augment_matrix[row_index,:] = multiple * augment_matrix[colum_index] + augment_matrix[row_index,:]
            
    result = augment_matrix[:,colum:a_colum]
    return result


def init_matrix_inverse(shape_list:list)->np.array:
    time_list = []
    for shape in shape_list:
        matrix = np.random.randn(shape,shape)
        start_time = tm.perf_counter()
        matrix_inverse = inverse(matrix)
        end_time = tm.perf_counter()
        time_list.append(end_time-start_time)
    return np.array([shape_list,time_list])
        

def draw_relation_digram(r_matrix:np.array):
    shape_list = r_matrix[0,:]
    time_list = r_matrix[1,:]
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.set_title("矩阵逆运算复杂度与维度关系")
    ax.plot(shape_list,time_list,"red")
    ax.set_xscale('log')  # 使用 ax 对象设置
    ax.set_yscale('log')  # 使用 ax 对象设置
    ax.set_xlabel("矩阵维度")
    ax.set_ylabel("求逆用时")
    ax.grid(True,color = 'b',linestyle = '-',linewidth = 2)
    fig.legend()
    plt.show()


if __name__ == "__main__":
    """matrix = np.array([[2,1],[4,3]])
    matrix_inverse = inverse(matrix)
    print(f"原矩阵={matrix},原矩阵的逆={matrix_inverse}")"""
    shape_list = [500, 1000, 2000, 4000]
    r_matrix = init_matrix_inverse(shape_list)
    print(f"求逆运算的维度-用时矩阵={r_matrix}")
    draw_relation_digram(r_matrix)

            
