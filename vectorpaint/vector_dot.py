import numpy as np
import matplotlib.pyplot as plt
from common.steupGrid import SteupGrid

st = SteupGrid(4)
class VectorDot():
    def __init__(self,basis_matrix:np.array):
        self.basis_matrix = basis_matrix
        self.i_hat = basis_matrix[0,:]
        self.j_hat = basis_matrix[1,:]

    def unit_dot(self,unit_vector:np.array,dot_vector:np.array):
        res = np.dot(unit_vector,dot_vector)
        st = SteupGrid(5)
        fig,aex = st.steup_grid(2)
        ax1 = aex[0,0]
        ax2 = aex[0,1]
        ax3 = aex[1,0]
        st.steup_plot(ax1,"unit_vector")
        st.plot_matrix(ax1,self.basis_matrix,'b')
        st.plot_matrix(ax1,unit_vector,'r')
        st.steup_grid_line(ax1,self.basis_matrix,[-st.limit,st.limit])
        st.steup_plot(ax2,"dot_vector")
        st.plot_matrix(ax2,self.basis_matrix,'b')
        st.plot_matrix(ax2,dot_vector,'r')
        st.steup_grid_line(ax2,self.basis_matrix,[-st.limit,st.limit])
        st.steup_plot(ax3,"res")
        st.plot_matrix(ax3,self.basis_matrix,'b')
        st.plot_matrix(ax3,res*unit_vector,'r')
        st.plot_matrix(ax3,unit_vector,'g')
        st.steup_grid_line(ax3,self.basis_matrix,[-st.limit,st.limit])
        plt.show()
         
           
    
if __name__ == "__main__":
    basis_matrix = np.array([[1,0],[0,1]])
    vd = VectorDot(basis_matrix)
    unit_vector = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    dot_vector = np.array([-2,-1])
    vd.unit_dot(unit_vector,dot_vector)