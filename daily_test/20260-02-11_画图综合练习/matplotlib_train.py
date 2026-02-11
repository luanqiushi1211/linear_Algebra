"""
1、绘制最小二乘的向量示意图，Ax=b,将A作为变换后的基画出来，将b画出来，并最终将最优解表示出来
2、绘制SVD示意图，将旋转，缩放，再旋转的过程画出来（最后做）
3、绘制二元的二次型的示意图
4、绘制向量的三种范数的等高线图
"""
from ast import List, Tuple
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
        draw_picture(point_set,(d,c))


def draw_picture(point_set:list,line_set:Tuple):
    c,d = line_set
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    x_space = np.arange(-10,10,1)
    y_space = np.arange(-10,10,1) 
    X,Y = np.meshgrid(x_space,y_space)
    res_space = d * np.array(x_space)+c
    for i in range(0,len(y_space)):
       
        ax.plot(X[i,:],Y[i,:],"gray")
    for k in range(0,len(x_space)):
       ax.plot(X[:,k],Y[:,k],"gray")          
    
    ax.plot(x_space,res_space,"red")
    for point_tuple in point_set:
        x,y = point_tuple
        ax.scatter(x,y,c="blue")
    plt.show()
        

 


if __name__ == "__main__":
    point_set = [(1,2),(2,4),(3,7)]
    least_squares(point_set)