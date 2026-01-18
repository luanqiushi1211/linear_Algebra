import numpy as np
import matplotlib.pyplot as plt

# 1. 定义我们刚才手算的矩阵 A
A = np.array([[2, 2],
              [-1, 1]])

# 2. 使用 NumPy 进行 SVD 分解
# 注意：np.linalg.svd 返回的是 U, Sigma(一维数组), V_transpose
U, S, Vt = np.linalg.svd(A)
V = Vt.T  # 转置回来得到 V

print(f"=== 我们的矩阵 A ===\n{A}")
print(f"\n=== 奇异值 (Sigma) ===\n{S}")
print(f"你的手算结果应该是: √8 ≈ 2.828, √2 ≈ 1.414 -> {'Match!' if np.allclose(S, [np.sqrt(8), np.sqrt(2)]) else 'Check calculations'}")
print(f"\n=== 左奇异向量 (U - 输出空间的轴) ===\n{U}")
print(f"\n=== 右奇异向量 (V - 输入空间的轴) ===\n{V}")

# --- 开始可视化 ---

# 准备画图数据：生成一个单位圆上的点
theta = np.linspace(0, 2*np.pi, 100)
circle_x = np.cos(theta)
circle_y = np.sin(theta)
circle_points = np.vstack([circle_x, circle_y])

# 应用矩阵 A 进行线性变换：圆 -> 椭圆
ellipse_points = A @ circle_points

# 设置画布
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# --- 左图：输入空间 (Input Space) ---
ax[0].plot(circle_x, circle_y, 'gray', alpha=0.5, label='Unit Circle')
ax[0].set_title("Input Space: V vectors")
ax[0].set_aspect('equal')
ax[0].grid(True)

# 画出 V 的两个向量 (输入基)
# v1 (对应最大奇异值) 用红色，v2 用蓝色
origin = [0, 0]
ax[0].quiver(*origin, V[0,0], V[1,0], color='r', scale=1, scale_units='xy', angles='xy', label='v1 (Right Singular)')
ax[0].quiver(*origin, V[0,1], V[1,1], color='b', scale=1, scale_units='xy', angles='xy', label='v2 (Right Singular)')
ax[0].legend()
ax[0].set_xlim(-2, 2)
ax[0].set_ylim(-2, 2)

# --- 右图：输出空间 (Output Space) ---
ax[1].plot(ellipse_points[0, :], ellipse_points[1, :], 'gray', alpha=0.5, label='Transformed Ellipse')
ax[1].set_title("Output Space: A * Circle")
ax[1].set_aspect('equal')
ax[1].grid(True)

# 画出 A*v (实际上就是 sigma * u)
# 这是变换后的向量位置
Av1 = A @ V[:, 0] # 应该是 sigma1 * u1
Av2 = A @ V[:, 1] # 应该是 sigma2 * u2

ax[1].quiver(*origin, Av1[0], Av1[1], color='r', scale=1, scale_units='xy', angles='xy', label='A*v1 (sigma1 * u1)')
ax[1].quiver(*origin, Av2[0], Av2[1], color='b', scale=1, scale_units='xy', angles='xy', label='A*v2 (sigma2 * u2)')

# 额外画出 U 向量的方向（虚线），验证它们是否重合
ax[1].plot([0, U[0,0]*S[0]], [0, U[1,0]*S[0]], 'r--', alpha=0.5, label='u1 direction')
ax[1].plot([0, U[0,1]*S[1]], [0, U[1,1]*S[1]], 'b--', alpha=0.5, label='u2 direction')

ax[1].legend()
ax[1].set_xlim(-4, 4)
ax[1].set_ylim(-4, 4)

plt.show()