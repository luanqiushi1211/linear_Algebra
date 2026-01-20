import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 1. 准备图片
# 读取本地图片并转换为灰度图
img = np.array(Image.open(r'G:\素材\图片\鬼灭之刃\人物\富冈义勇\最终版放大.png').convert('L')) 

# 2. 进行 SVD 分解
# TODO: 使用 numpy 的 linalg.svd 函数
# 提示: full_matrices=False 可以让计算更快且维度对齐
U, S, Vt = np.linalg.svd(img)

# 3. 确定要保留的奇异值数量 (前 10%)
k = int(len(S) * 0.3)
print(f"原始奇异值数量: {len(S)}, 保留前 {k} 个")

# 4. 重构图像 (The Magic Step)
# 我们需要构建一个新的近似矩阵: A_approx = U[:, :k] @ Sigma_k @ Vt[:k, :]
# 注意: S 只是一个一维数组，需要把它变回对角矩阵

# TODO: 取出前 k 个奇异值，构建对角矩阵
"""
array[row_start:row_end:row_step, col_start:col_end:col_step]
"""
S_k_diag = np.diag(S[:k]) 

# TODO: 取出 U 的前 k 列
U_k = U[:, :k]

# TODO: 取出 Vt 的前 k 行
Vt_k = Vt[:k, :]

# TODO: 进行矩阵乘法重构图像 (推荐用 @ 符号)
img_compressed = U_k @ S_k_diag @ Vt_k

# 5. 可视化对比
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(img, cmap='gray')
ax[0].set_title("Original Image")
ax[0].axis('off')

ax[1].imshow(img_compressed, cmap='gray')
ax[1].set_title(f"Compressed (Top {k} Singular Values)")
ax[1].axis('off')

plt.show()