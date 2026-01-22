import numpy as np
from matplotlib import pyplot as plt
import sympy as sp

class DerivativeTool:
    def __init__(self, f, x=None):
        self.x = sp.symbols('x')
        self.f_expr = f
        self.f_derivative = sp.diff(f, self.x)
        
        if x is not None:
            self.x_value = x
            self.y_value = float(f.subs(self.x, x))
            self.h = 0.0001
        else:
            self.x_value = None
            self.y_value = None
    
    def get_derivative_formula(self):
        return self.f_derivative
    
    def get_derivative(self):
        if self.x_value is None:
            raise ValueError("No x value provided. Use __init__(f, x) to provide x value.")
        return float(self.f_derivative.subs(self.x, self.x_value))
    
    def evaluate_derivative(self, x_val):
        return float(self.f_derivative.subs(self.x, x_val))
    
    def get_linear_approximation(self, x0=None):
        if x0 is None:
            x0 = self.x_value
        if x0 is None:
            raise ValueError("No x0 value provided.")
        
        f_x0 = float(self.f_expr.subs(self.x, x0))
        df_x0 = float(self.f_derivative.subs(self.x, x0))
        
        return lambda x: f_x0 + df_x0 * (x - x0)
    
    def print_derivative_info(self):
        print(f"原函数: f(x) = {self.f_expr}")
        print(f"导函数: f'(x) = {self.f_derivative}")
        if self.x_value is not None:
            print(f"在 x = {self.x_value} 处:")
            print(f"  f({self.x_value}) = {self.y_value}")
            print(f"  f'({self.x_value}) = {self.get_derivative()}")
            
            linear_func = self.get_linear_approximation()
            print(f"线性近似: y = {self.get_derivative()}x + {self.y_value - self.get_derivative() * self.x_value}")
    
    def plot_derivative(self, x_range=(-5, 5), num_points=200, show_tangent=True, show_derivative=True):
        fig, axes = plt.subplots(1, 2 if show_derivative else 1, figsize=(12, 5))
        
        if not show_derivative:
            axes = [axes]
        
        x_min, x_max = x_range
        x_vals = np.linspace(x_min, x_max, num_points)
        
        f_func = sp.lambdify(self.x, self.f_expr, 'numpy')
        f_vals = f_func(x_vals)
        
        if show_derivative:
            df_func = sp.lambdify(self.x, self.f_derivative, 'numpy')
            df_vals = df_func(x_vals)
        
        ax_idx = 0
        
        ax = axes[ax_idx]
        ax.plot(x_vals, f_vals, 'b-', linewidth=2, label=f'f(x) = {self.f_expr}')
        
        if self.x_value is not None and x_min <= self.x_value <= x_max:
            ax.plot(self.x_value, self.y_value, 'ro', markersize=8, label=f'Point ({self.x_value}, {self.y_value:.2f})')
            
            if show_tangent:
                linear_func = self.get_linear_approximation()
                tangent_vals = linear_func(x_vals)
                ax.plot(x_vals, tangent_vals, 'r--', linewidth=1.5, alpha=0.7, label='Tangent line')
        
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title('Original Function')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        if show_derivative:
            ax_idx += 1
            ax = axes[ax_idx]
            ax.plot(x_vals, df_vals, 'g-', linewidth=2, label=f"f'(x) = {self.f_derivative}")
            
            if self.x_value is not None and x_min <= self.x_value <= x_max:
                df_x0 = self.get_derivative()
                ax.plot(self.x_value, df_x0, 'ro', markersize=8, label=f"Point ({self.x_value}, {df_x0:.2f})")
                ax.axhline(y=df_x0, color='r', linestyle='--', alpha=0.5, linewidth=1)
            
            ax.set_xlabel('x')
            ax.set_ylabel("f'(x)")
            ax.set_title('Derivative Function')
            ax.grid(True, alpha=0.3)
            ax.legend()
        
        plt.tight_layout()
        plt.show()
    
    def plot_combined(self, x_range=(-5, 5), num_points=200, show_tangent=True):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        x_min, x_max = x_range
        x_vals = np.linspace(x_min, x_max, num_points)
        
        f_func = sp.lambdify(self.x, self.f_expr, 'numpy')
        f_vals = f_func(x_vals)
        
        df_func = sp.lambdify(self.x, self.f_derivative, 'numpy')
        df_vals = df_func(x_vals)
        
        ax.plot(x_vals, f_vals, 'b-', linewidth=2, label=f'f(x) = {self.f_expr}')
        ax.plot(x_vals, df_vals, 'g-', linewidth=2, label=f"f'(x) = {self.f_derivative}")
        
        if self.x_value is not None and x_min <= self.x_value <= x_max:
            ax.plot(self.x_value, self.y_value, 'ro', markersize=10, 
                   label=f'f({self.x_value}) = {self.y_value:.2f}')
            ax.plot(self.x_value, self.get_derivative(), 'ro', markersize=10, 
                   label=f"f'({self.x_value}) = {self.get_derivative():.2f}")
            
            if show_tangent:
                linear_func = self.get_linear_approximation()
                tangent_vals = linear_func(x_vals)
                ax.plot(x_vals, tangent_vals, 'r--', linewidth=1.5, alpha=0.7, label='Tangent line')
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Function and Derivative')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
  x = sp.symbols('x')
  f = x**2
  dt = DerivativeTool(f, x=3)
  dt.print_derivative_info()
  dt.plot_combined(x_range=(-3, 5), show_tangent=True)