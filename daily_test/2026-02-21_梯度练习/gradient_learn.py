import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
def quadratic_type(matrix:np.array):
    x = np.linspace(-2,2,100)
    y = np.linspace(-2,2,100)
    z = []
    X,Y = np.meshgrid(x,y)
    for i in x:
        for j in y:
            z_data = np.array([[i,j]]) @ matrix @ np.array([[i,j]]).T
            z.append(z_data)          
                        
    Z = np.reshape(z,np.shape(X))
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(121,projection="3d")
    ax2 = fig.add_subplot(122)
    surf = ax.plot_surface(X,Y,Z,cmap = 'viridis',rstride = 1)
    ax.set_title("二次型标量场示意图")
    ax.set_label("X")
    ax.set_label("Y")
    ax.set_label("Z")
    fig.colorbar(surf)
    ax2.grid(True,linestyle = '-',linewidth=2)
    ax2.set_xlim(-3,3)
    ax2.set_ylim(-3,3)
    ax2.set_title("等高线和梯度向量")
    ct = ax2.contour(X,Y,Z,levels = 1,colors = 'red',linewidth=2)
    h, _ = ct.legend_elements()
    path = ct.get_paths()
    for i,path in enumerate(path):
        vertices = path.vertices
        for j,coords in enumerate(vertices):
            if j%3==0:
                x_coords = coords[0]
                y_coords  =coords[1]
                x_gv = 4*x_coords-y_coords
                y_gv = 2*y_coords-x_coords
                gv_model = np.sqrt(x_gv**2+y_gv**2)
                x_gv = x_gv/gv_model
                y_gv = y_gv/gv_model
                q = ax2.quiver(x_coords,y_coords,x_gv,y_gv,angles = 'xy',scale_units='xy',scale = 1,color = 'blue')         
                ax2.quiverkey(q, X=0.9, Y=1.05, U=1,label="梯度向量",labelpos='E')

    ax2.legend(loc='upper left')
    plt.legend(h, ['二次型标量场等高线'])
    plt.show()




if __name__ == "__main__":
    matrix = np.array([[2,-0.5],[-0.5,1]])
    quadratic_type(matrix)

