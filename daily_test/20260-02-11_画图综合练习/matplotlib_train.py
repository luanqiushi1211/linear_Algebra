"""
1、绘制最小二乘的向量示意图，Ax=b,将A作为变换后的基画出来，将b画出来，并最终将最优解表示出来
2、绘制SVD示意图，将旋转，缩放，再旋转的过程画出来（最后做）
3、绘制二元的二次型的示意图
4、绘制向量的三种范数的等高线图
"""
from ast import List, Tuple
from turtle import color
import numpy as np
from matplotlib import pyplot as plt

def least_squares(point_set:List):
    cofficient_matrix = []
    res_vector = []
    for point_tuple in point_set:
        x,y = point_tuple
        cofficient_matrix.append([x,1])
        res_vector.append([y])
    cofficient_matrix = np.array(cofficient_matrix)
    res_vector = np.array(res_vector)
    rank_cofficient_matrix = np.linalg.matrix_rank(cofficient_matrix)
    argument_matrix = np.hstack((cofficient_matrix,res_vector))
    rank_argument = np.linalg.matrix_rank(argument_matrix)
    print(f"系数矩阵是：,{cofficient_matrix},秩是,{rank_cofficient_matrix}")
    print(f"结果向量是：,{res_vector},增广矩阵是：{argument_matrix},增广矩阵的秩是：{rank_argument}")
    if(rank_argument==rank_cofficient_matrix):
        print(f"线性方程组有解")
    else:
        print(f"线性方程组无解，开始使用最小二乘法求最优解")
        inverse_gram_matrix = np.linalg.inv(cofficient_matrix.T @ cofficient_matrix)           
        res = inverse_gram_matrix @ cofficient_matrix.T @ res_vector
        c,d = res
        print(f"最优解的偏移量= {d},斜率={c}")
        fig = draw_picture(point_set,(d,c))




def draw_picture(point_set:list,line_set:Tuple):
    c,d = line_set
    fig = plt.figure(figsize=(20,8))
    ax = fig.add_subplot(121)
    x_space = np.arange(-10,10,1)
    y_space = np.arange(-10,10,1) 
    X,Y = np.meshgrid(x_space,y_space)
    res_space = d * np.array(x_space)+c
    ax.grid(True,color = "gray",linestyle = '-',alpha = 0.3)
      
    
    ax.plot(x_space,res_space,"red")
    for point_tuple in point_set:
        x,y = point_tuple
        ax.scatter(x,y,c="blue")
    plt.show()
    return fig
        

def is_positive(matrix:np.array):
    eigenvalues,eigenvectors = np.linalg.eig(matrix)
    if np.all(eigenvalues>0):
        print(f"{matrix}是正定矩阵")
    x_data_set = np.linspace(-10,10,100)
    y_data_set = np.linspace(-10,10,100)
    z_data_set = []
    X,Y = np.meshgrid(x_data_set,y_data_set)
    for i in x_data_set:
        for j in y_data_set:
            res = np.array([[i,j]]) @ matrix @ np.array([[i,j]]).T
            z_data_set.append(res)
    Z = np.reshape(z_data_set,np.shape(X))
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(121,projection = "3d")
    ax.set_title("二次型3D曲面图")
    ax.set_label("X")
    ax.set_label("Y")
    ax.set_label("Z")
    surf = ax.plot_surface(X,Y,Z,cmap = 'viridis',rstride = 5)
    fig.colorbar(surf)   
    ax2 = fig.add_subplot(122)
    ax2.set_xlim(-2,2)
    ax2.set_ylim(-2,2)
    ax2.grid(True,color = 'b',linestyle = '-',linewidth = 2)
    for i in eigenvectors:
        x,y = i
        ax2.quiver(0,0,x,y,angles = 'xy',scale_units='xy',scale = 1,headwidth=4,  headlength=5, headaxislength=4.5)
    plt.show()



if __name__ == "__main__":
    point_set = [(1,2),(2,4),(3,7)]
    matrix = np.array([[1,2],[2,1]])
    is_positive(matrix)