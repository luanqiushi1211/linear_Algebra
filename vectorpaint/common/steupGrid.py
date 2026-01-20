import numpy as np
from matplotlib import pyplot as plt

class SteupGrid:
    def __init__(self,limit:int):
        self.limit = limit  


    def steup_grid(self,aexnum:int):
        fig,aex = plt.subplots(aexnum,aexnum,figsize=(5,5))
        plt.subplots_adjust(wspace=0.3,hspace=0.3)
        return fig,aex


    def steup_plot(self,ax:plt.Axes,title):
    
        #设置标题
        ax.set_title(title)
        #设置横轴
        ax.axhline(y=0,color='k',alpha=0.3,linewidth=0.5)
        #设置纵轴
        ax.axvline(x=0,color='k',alpha=0.3,linewidth=0.5)
        #设置纵横轴比例
        ax.set_aspect('equal')
        #设置网格，网格线为虚线，透明度为0.3，线宽为0.5
        #ax.grid(visible=True,linestyle='--',alpha=0.3,linewidth=0.5)
        #设置横轴纵轴范围
        ax.set_xlim(-self.limit,self.limit)
        ax.set_ylim(-self.limit,self.limit)

    def plot_matrix(self,ax:plt.Axes,matrix,color='r',label_suffix=None,origin=None):
        if origin is None:
            origin = [0,0]
        if matrix.ndim == 1:
            if label_suffix is not None:
                ax.quiver(*origin,matrix[0],matrix[1],angles='xy',scale_units='xy',scale=1,color=color,label=f'{label_suffix[0]}')
            else:
                ax.quiver(*origin,matrix[0],matrix[1],angles='xy',scale_units='xy',scale=1,color=color)
        else:
            if label_suffix is not None:
                ax.quiver(*origin,matrix[0,0],matrix[0,1],angles='xy',scale_units='xy',scale=1,color=color,label=f'{label_suffix[0]}')
                ax.quiver(*origin,matrix[1,0],matrix[1,1],angles='xy',scale_units='xy',scale=1,color=color,label=f'{label_suffix[1]}')
            else:
                ax.quiver(*origin,matrix[0,0],matrix[0,1],angles='xy',scale_units='xy',scale=1,color=color)
                ax.quiver(*origin,matrix[1,0],matrix[1,1],angles='xy',scale_units='xy',scale=1,color=color)
        if label_suffix is not None:
            ax.legend()


    def steup_grid_line(self,ax:plt.Axes,matrix:np.array,rangeList:list):
        min_range = min(rangeList)
        max_range = max(rangeList)
        i_hat = matrix[0,:]
        j_hat = matrix[1,:]
        for j_coeff in range(min_range,max_range+1):
            for i_coeff in range(min_range,max_range):
                start_point = i_coeff * i_hat + j_coeff * j_hat
                end_point = (i_coeff + 1) * i_hat + j_coeff * j_hat
                ax.plot([start_point[0], end_point[0]],
                        [start_point[1], end_point[1]],
                        color='black', alpha=1, linewidth=0.5)
        for i_coeff in range(min_range,max_range):
            for j_coeff in range(min_range,max_range):
                start_point = i_coeff * i_hat + j_coeff * j_hat
                end_point = i_coeff * i_hat + (j_coeff + 1) * j_hat
                ax.plot([start_point[0], end_point[0]],
                        [start_point[1], end_point[1]],
                        color='black', alpha=1, linewidth=0.5)


