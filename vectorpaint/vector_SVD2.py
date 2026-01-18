import numpy as np
import matplotlib.pyplot as plt

# --- 1. 数据准备 ---
# 定义矩阵 A
A = np.array([[2, 2],
              [-1, 3]])

# 进行 SVD 分解
U, S_values, Vt = np.linalg.svd(A)
# 将一维的奇异值数组转换为对角矩阵 Sigma
Sigma = np.diag(S_values)
# 获取 V (虽然这里变换主要用到 Vt)
V = Vt.T

# 生成单位圆上的点
theta = np.linspace(0, 2*np.pi, 200)
circle = np.vstack([np.cos(theta), np.sin(theta)])

# 定义标准基向量 e1, e2 (用于追踪变换过程)
basis = np.array([[1, 0],  # e1 (红色)
                  [0, 1]]) # e2 (蓝色)

# --- 辅助绘图函数 ---
def setup_plot(ax, title):
    """设置坐标轴样式"""
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.axhline(y=0, color='k', linewidth=0.5, alpha=0.3)
    ax.axvline(x=0, color='k', linewidth=0.5, alpha=0.3)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.6)
    # 设置统一的视野范围，方便对比
    limit = 3.5
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

def plot_vectors(ax, vectors, color_e1='r', color_e2='b', label_suffix=""):
    """画出当前的基向量位置"""
    origin = [0, 0]
    # 画变换后的 e1
    ax.quiver(*origin, vectors[0,0], vectors[1,0], color=color_e1, 
              scale=1, scale_units='xy', angles='xy', width=0.015, label=f'Transformed e1 {label_suffix}')
    # 画变换后的 e2
    ax.quiver(*origin, vectors[0,1], vectors[1,1], color=color_e2, 
              scale=1, scale_units='xy', angles='xy', width=0.015, label=f'Transformed e2 {label_suffix}')

# --- 开始绘图 ---
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
plt.subplots_adjust(wspace=0.3, hspace=0.3) # 调整子图间距

# === 图1：目标全貌 (Target: A @ x) ===
ax1 = axes[0, 0]
setup_plot(ax1, "1. Final Goal: A applied directly\n(A @ x)")
# 画原始单位圆 (灰色虚线背景)
ax1.plot(circle[0, :], circle[1, :], 'k--', alpha=0.3)
# 计算并画出最终变换后的椭圆
final_ellipse = A @ circle
ax1.plot(final_ellipse[0, :], final_ellipse[1, :], 'purple', linewidth=2)
# 追踪基向量变化
final_basis = A @ basis
plot_vectors(ax1, final_basis, label_suffix="(Final)")
ax1.legend(loc='lower right', fontsize=9)


# === 图2：第一步 - 旋转 (Step 1: Rotate by V.T) ===
# 含义：将标准基旋转到对齐输入主成分的方向
ax2 = axes[0, 1]
setup_plot(ax2, "2. Step 1: Rotation\n(Vt @ x)")
# 画原始单位圆 (背景)
ax2.plot(circle[0, :], circle[1, :], 'k--', alpha=0.3)
# 计算变换后的圆（正交矩阵变换后还是圆，只是转了）
step1_circle = Vt @ circle
ax2.plot(step1_circle[0, :], step1_circle[1, :], 'g', linewidth=2)
# 追踪基向量变化
step1_basis = Vt @ basis
plot_vectors(ax2, step1_basis, label_suffix="(rotated by Vt)")
ax2.legend(loc='lower right', fontsize=9)


# === 图3：第二步 - 伸缩 (Step 2: Stretch by Sigma) ===
# 含义：在当前的旋转基下，沿坐标轴拉伸
ax3 = axes[1, 0]
setup_plot(ax3, "3. Step 2: Stretching\n(Sigma @ Vt @ x)")
# 画上一步的圆 (背景)
ax3.plot(step1_circle[0, :], step1_circle[1, :], 'k--', alpha=0.3)
# 计算伸缩后的椭圆 (注意：此时是轴对齐的！)
step2_ellipse = Sigma @ step1_circle
ax3.plot(step2_ellipse[0, :], step2_ellipse[1, :], 'orange', linewidth=2)
# 追踪基向量变化 (它们被拉长了)
step2_basis = Sigma @ step1_basis
plot_vectors(ax3, step2_basis, label_suffix="(stretched)")
ax3.legend(loc='lower right', fontsize=9)


# === 图4：第三步 - 再旋转 (Step 3: Final Rotation by U) ===
# 含义：将轴对齐的椭圆旋转到最终方向
ax4 = axes[1, 1]
setup_plot(ax4, "4. Step 3: Final Rotation\n(U @ Sigma @ Vt @ x)")
# 画上一步的轴对齐椭圆 (背景)
ax4.plot(step2_ellipse[0, :], step2_ellipse[1, :], 'k--', alpha=0.3)
# 计算最终旋转后的椭圆
step3_ellipse = U @ step2_ellipse
ax4.plot(step3_ellipse[0, :], step3_ellipse[1, :], 'purple', linewidth=2)
# 追踪基向量变化
step3_basis = U @ step2_basis
plot_vectors(ax4, step3_basis, label_suffix="(final rotated)")
ax4.legend(loc='lower right', fontsize=9)

# 添加总标题
fig.suptitle("Visualizing SVD: The 'Rotation -> Stretch -> Rotation' Journey\nA = U @ Sigma @ Vt", fontsize=16, y=0.98)

plt.show()