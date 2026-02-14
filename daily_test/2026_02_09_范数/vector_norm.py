"""
生成 $x, y$ 网格 (范围 -1.5 到 1.5)。
计算每个网格点上的范数值 $Z_1 = ||(x,y)||_1$, $Z_2 = ||(x,y)||_2$, $Z_{inf} = ||(x,y)||_\infty$。
提示：可以使用 np.abs(X) + np.abs(Y) 计算 L1使用 plt.contour (等高线图) 
分别画出 $Z=1$ 的那条线。你可以把三条线画在同一张图上，用不同颜色区分。
观察：$L_1$ 是不是菱形？$L_2$ 是不是圆形？
"""
from tkinter import Label
import numpy as np
from matplotlib import colors, pyplot as plt
def xy_grid():
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负
    x_list = np.linspace(-1.5,1.5,100)
    y_list = np.linspace(-1.5,1.5,100)
    X,Y = np.meshgrid(x_list,y_list)
    Z1 = np.abs(X)+np.abs(Y)
    Z2 = np.sqrt(X**2 + Y**2)
    Z3  = np.maximum(np.abs(X),np.abs(Y))
   
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    for i in range(0,len(y_list)):
        ax.plot(X[i,:],Y[i,:],"gray")
    for j in range(0,len(x_list)):
        ax.plot(X[:,j],Y[:,j],"gray")
    labels = ["向量1范数", "向量谱范数", "向量无穷范数"]
    c1 = ax.contour(X,Y,Z1,levels = 1,colors = "red",Label="向量1范数")
    c2 = ax.contour(X,Y,Z2,levels = 1,colors = "black",Label = "向量谱范数")
    c3 = ax.contour(X,Y,Z3,levels = 1,colors = "blue",Label = "向量无穷范数",linewidths=2)
    proxy = [plt.Rectangle((0,0),1,1,fc = pc.get_edgecolor()[0]) 
             for pc in [c1.collections[0], c2.collections[0], c3.collections[0]]]
    plt.legend(proxy, labels)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("向量范数等高线")
    ax.set_aspect("equal")
    plt.show()
    

if __name__ == "__main__":
    xy_grid()