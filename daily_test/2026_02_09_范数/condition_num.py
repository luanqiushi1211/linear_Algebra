import numpy as np

def condition_num():

    I = np.array([[1,0],[0,1]])

    a = np.linspace(-10,10,10)

    b = a*0.9999+0.0001

    sick_A = np.array([a,b]).T

    print("sick_A=",sick_A)

    Gram_sick_A = sick_A.T @ sick_A

    print("病态Gram矩阵是：",Gram_sick_A)

    sick_condition_num = np.linalg.cond(Gram_sick_A)

    print("病态Gram矩阵的条件数是：",sick_condition_num)

    inverse_Gram_sick_A = np.linalg.inv(Gram_sick_A)

    sick_i = inverse_Gram_sick_A @ Gram_sick_A

    print("病态Gram矩阵乘以逆矩阵的结果是：",sick_i)

    lamadaI = 0.1 * I

    Mridge = Gram_sick_A + lamadaI

    Mridge_condition_num = np.linalg.cond(Mridge)

    print("Mridge的条件数=",Mridge_condition_num)

    Mridge_inverse = np.linalg.inv(Mridge)

    Mridge_I = Mridge_inverse @ Mridge

    print("正则化后的Gram矩阵乘以逆矩阵的结果是：",Mridge_I)





if __name__ == "__main__":

    condition_num()