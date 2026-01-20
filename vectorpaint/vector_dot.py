import numpy as np
import matplotlib.pyplot as plt
from common.steupGrid import SteupGrid

st = SteupGrid(4)
class VectorDot():
    def __init__(self,basis_matrix:np.array):
        self.basis_matrix = basis_matrix
        self.i_hat = basis_matrix[0,:]
        self.j_hat = basis_matrix[1,:]

    def plot_vector_with_basis(self,ax:plt.Axes,title:str,vectors:list,origin=None):
        """
        绘制基向量和额外的向量
        
        参数:
        - ax: 坐标轴对象
        - title: 图形标题
        - vectors: 额外向量列表，每个元素为(vector, color, label)的元组
        """
        st.steup_plot(ax,title)
        st.plot_matrix(ax,self.basis_matrix,'b')
        for vector, color, label in vectors:
            st.plot_matrix(ax,vector,color,[label],origin)
        st.steup_grid_line(ax,self.basis_matrix,[-st.limit,st.limit])

    def unit_dot(self,unit_vector:np.array,dot_vector:np.array):
        res = np.dot(unit_vector,dot_vector)
        st = SteupGrid(5)
        fig,aex = st.steup_grid(2)
        ax1 = aex[0,0]
        ax2 = aex[0,1]
        ax3 = aex[1,0]
        ax4 = aex[1,1]
        
        self.plot_vector_with_basis(ax1,"unit_vector",[(unit_vector,'r','unit={}'.format(unit_vector))])
        self.plot_vector_with_basis(ax2,"dot_vector",[
            (unit_vector,'r','unit={}'.format(unit_vector)),
            (dot_vector,'g','dot={}'.format(dot_vector))
        ])
        self.plot_vector_with_basis(ax3,"res",[
            (res*unit_vector,'y','res={}'.format(res*unit_vector)),
            (unit_vector,'r','unit={}'.format(unit_vector)),
            (dot_vector,'g','dot={}'.format(dot_vector))
        ])
        self.plot_vector_with_basis(ax4,"process",[
            (res*unit_vector,'y','res={}'.format(res*unit_vector)),
            (unit_vector,'r','unit={}'.format(unit_vector)),
            (dot_vector,'g','dot={}'.format(dot_vector))
            
        ])
        self.plot_vector_with_basis(ax4,"process",[
            (res*unit_vector-dot_vector,'m','process={}'.format(res*unit_vector-dot_vector))
        ],origin=dot_vector)
        plt.show()
         
           
    
if __name__ == "__main__":
    basis_matrix = np.array([[1,0],[0,1]])
    vd = VectorDot(basis_matrix)
    unit_vector = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    dot_vector = np.array([2,-1])
    vd.unit_dot(unit_vector,dot_vector)