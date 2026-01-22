import sympy as sp
from derivative_tool import DerivativeTool
import matplotlib.pyplot as plt

x = sp.symbols('x')

print("=" * 60)
print("示例1：二次函数 f(x) = x^2，在 x=2 处")
print("=" * 60)
f1 = x**2
dt1 = DerivativeTool(f1, x=2)
dt1.print_derivative_info()
print("\n绘制图像...")
dt1.plot_derivative(x_range=(-3, 5), show_tangent=True, show_derivative=True)

print("\n" + "=" * 60)
print("示例2：三次函数 f(x) = x^3 - 2x^2 + x - 1，在 x=1 处")
print("=" * 60)
f2 = x**3 - 2*x**2 + x - 1
dt2 = DerivativeTool(f2, x=1)
dt2.print_derivative_info()
print("\n绘制图像...")
dt2.plot_derivative(x_range=(-2, 4), show_tangent=True, show_derivative=True)

print("\n" + "=" * 60)
print("示例3：正弦函数 f(x) = sin(x)，在 x=π/2 处")
print("=" * 60)
f3 = sp.sin(x)
dt3 = DerivativeTool(f3, x=sp.pi/2)
dt3.print_derivative_info()
print("\n绘制图像...")
dt3.plot_derivative(x_range=(0, 2*sp.pi), show_tangent=True, show_derivative=True)

print("\n" + "=" * 60)
print("示例4：只显示原函数，不显示导数")
print("=" * 60)
f4 = x**2 - 2*x + 1
dt4 = DerivativeTool(f4, x=1)
dt4.print_derivative_info()
print("\n绘制图像（只显示原函数）...")
dt4.plot_derivative(x_range=(-2, 4), show_tangent=True, show_derivative=False)

print("\n" + "=" * 60)
print("示例5：组合显示原函数和导数在同一图中")
print("=" * 60)
f5 = x**3 - 3*x
dt5 = DerivativeTool(f5, x=1)
dt5.print_derivative_info()
print("\n绘制组合图像...")
dt5.plot_combined(x_range=(-3, 3), show_tangent=True)

print("\n" + "=" * 60)
print("示例6：指数函数 f(x) = e^x，在 x=0 处")
print("=" * 60)
f6 = sp.exp(x)
dt6 = DerivativeTool(f6, x=0)
dt6.print_derivative_info()
print("\n绘制图像...")
dt6.plot_derivative(x_range=(-2, 2), show_tangent=True, show_derivative=True)

print("\n" + "=" * 60)
print("示例7：对数函数 f(x) = ln(x)，在 x=1 处")
print("=" * 60)
f7 = sp.log(x)
dt7 = DerivativeTool(f7, x=1)
dt7.print_derivative_info()
print("\n绘制图像...")
dt7.plot_derivative(x_range=(0.1, 5), show_tangent=True, show_derivative=True)

print("\n" + "=" * 60)
print("示例8：不显示切线")
print("=" * 60)
f8 = x**2 + 2*x + 1
dt8 = DerivativeTool(f8, x=0)
dt8.print_derivative_info()
print("\n绘制图像（不显示切线）...")
dt8.plot_derivative(x_range=(-3, 3), show_tangent=False, show_derivative=True)
