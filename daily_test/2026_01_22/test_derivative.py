import sympy as sp
from derivative_tool import DerivativeTool

# 示例1：线性函数 f(x) = 2x + 3
print("=" * 50)
print("示例1：线性函数 f(x) = 2x + 3")
print("=" * 50)
x = sp.symbols('x')
f1 = 2*x + 3
dt1 = DerivativeTool(f1, x=2)
dt1.print_derivative_info()

# 示例2：二次函数 f(x) = x^2 + 2x + 1
print("\n" + "=" * 50)
print("示例2：二次函数 f(x) = x^2 + 2x + 1")
print("=" * 50)
f2 = x**2 + 2*x + 1
dt2 = DerivativeTool(f2, x=1)
dt2.print_derivative_info()

# 示例3：三次函数 f(x) = x^3 - 2x^2 + x - 1
print("\n" + "=" * 50)
print("示例3：三次函数 f(x) = x^3 - 2x^2 + x - 1")
print("=" * 50)
f3 = x**3 - 2*x**2 + x - 1
dt3 = DerivativeTool(f3, x=2)
dt3.print_derivative_info()

# 示例4：三角函数 f(x) = sin(x)
print("\n" + "=" * 50)
print("示例4：三角函数 f(x) = sin(x)")
print("=" * 50)
f4 = sp.sin(x)
dt4 = DerivativeTool(f4, x=sp.pi/2)
dt4.print_derivative_info()

# 示例5：指数函数 f(x) = e^x
print("\n" + "=" * 50)
print("示例5：指数函数 f(x) = e^x")
print("=" * 50)
f5 = sp.exp(x)
dt5 = DerivativeTool(f5, x=0)
dt5.print_derivative_info()

# 示例6：不提供具体x值，只获取导数公式
print("\n" + "=" * 50)
print("示例6：只获取导数公式（不提供具体x值）")
print("=" * 50)
f6 = x**3 + 2*x**2 - x + 5
dt6 = DerivativeTool(f6)
print(f"原函数: f(x) = {dt6.f_expr}")
print(f"导函数: f'(x) = {dt6.get_derivative_formula()}")

# 计算多个点的导数值
print("\n计算多个点的导数值:")
for x_val in [-2, -1, 0, 1, 2]:
    derivative_val = dt6.evaluate_derivative(x_val)
    print(f"  f'({x_val}) = {derivative_val}")

# 示例7：获取线性近似函数
print("\n" + "=" * 50)
print("示例7：获取线性近似函数")
print("=" * 50)
f7 = x**2
dt7 = DerivativeTool(f7, x=2)
dt7.print_derivative_info()

# 获取线性近似函数（切线）
linear_approx = dt7.get_linear_approximation()
print(f"\n在 x=2 处的线性近似函数:")
print(f"  y = {linear_approx(1)} (当 x=1)")
print(f"  y = {linear_approx(2)} (当 x=2)")
print(f"  y = {linear_approx(3)} (当 x=3)")

# 验证：在切点处，原函数值等于线性近似值
print(f"\n验证：在 x=2 处")
print(f"  原函数值: f(2) = {dt7.y_value}")
print(f"  线性近似值: y(2) = {linear_approx(2)}")
print(f"  是否相等: {abs(dt7.y_value - linear_approx(2)) < 1e-10}")
