import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
def ridge_fix()->tuple:    
    data_set1 = np.random.randn(100)
    data_set2 = data_set1+np.random.normal(0,0.0001,100)    
    matrix_i = np.eye(2)
    matrix_sick = np.array([data_set1,data_set2]).T
    gram_matrix = matrix_sick.T @ matrix_sick
    lambda_set = np.logspace(-6,1,50)
    cond_set = []
    for i in lambda_set:
        matrix_fix = gram_matrix+i*matrix_i
        conditionNum = np.linalg.cond(matrix_fix)
        cond_set.append(conditionNum)
    return (lambda_set,cond_set)
    
    
def draw_plot(data_tuple:tuple):
    lambda_set,cond_set = data_tuple
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.set_title("岭回归参数对矩阵条件数的影响")
    ax.grid(True,color = "gray",linestyle = '-',alpha = 0.3)
    ax.plot(lambda_set,cond_set,"red")
    ax.set_xscale('log')  # 使用 ax 对象设置
    ax.set_yscale('log')  # 使用 ax 对象设置
    ax.set_xlabel("正则化系数")
    ax.set_ylabel("条件数")
    fig.legend()
    plt.show()



if __name__ == "__main__":
    data_tuple = ridge_fix()
    draw_plot(data_tuple)