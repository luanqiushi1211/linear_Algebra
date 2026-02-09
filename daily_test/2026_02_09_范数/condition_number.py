"""
构造“病态”矩阵：创建一个 $10 \times 2$ 的矩阵 $X$。第 1 列：随机数。
第 2 列：让它几乎等于第 1 列（例如：X[:, 0] * 0.9999 + 0.0001）。这模拟了极度相关的特征。
计算 Gram 矩阵： $M = X^T X$。计算条件数 (Condition Number)：
使用 np.linalg.cond(M) 计算 $M$ 的条件数。条件数越大，说明矩阵越“病态”，求逆越不准。
尝试求逆：计算 $M^{-1}$ （使用 np.linalg.inv）。观察结果或者是计算 $M^{-1} M$，
看它是否偏离了单位矩阵 $I$。引入 Ridge 正则化：构造新矩阵 $M_{ridge} = M + \lambda I$ （取 $\lambda = 0.1$, $I$ 是单位阵）。
计算这个新矩阵 $M_{ridge}$ 的条件数。对比输出：打印：原始条件数 vs 正则化后的条件数。
预期：正则化后的条件数应该大幅下降，说明矩阵变得“健康”了。
"""
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