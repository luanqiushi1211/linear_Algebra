import numpy as np
import matplotlib.pyplot as plt

# 1. 定义原函数 f(x) = x^2
def func(x):
    return x ** 3

# 2. 定义数值求导函数
def numerical_derivative(f, x, h=0.00001):
    """
    计算函数 f 在 x 点的导数（斜率）
    f: 目标函数
    x: 目标点
    h: 极小的步长 (dx)
    """
    f=func(x)
    slope = (func(x+h)-func(x))/h # 修改这行
    return slope

# --- 测试部分 ---
x_target = 2.0  # 我们想求 x=2 处的导数

# 计算导数
slope_at_2 = numerical_derivative(func, x_target)
print(f"在 x={x_target} 处的数值导数: {slope_at_2:.4f}")
print(f"理论导数 (2x): {2 * x_target}")

# --- 可视化 (我帮你写好了框架，你运行看看切线对不对) ---
x = np.linspace(0, 4, 100)
y = func(x)

# 切线方程: y - y0 = m(x - x0)  =>  y = m(x - x0) + y0
y_target = func(x_target)
tangent_line = slope_at_2 * (x - x_target) + y_target

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = x^2")
plt.scatter([x_target], [y_target], color='red', s=50, label=f"Point ({x_target}, {y_target})")
plt.plot(x, tangent_line, 'r--', label=f"Tangent (Slope={slope_at_2:.2f})")
plt.title("Visualizing the Derivative")
plt.legend()
plt.grid(True)
plt.show()