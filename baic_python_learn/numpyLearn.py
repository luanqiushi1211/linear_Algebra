

# 导入numpy库，用于数值计算和数组操作
import numpy as np

# 导入matplotlib.pyplot模块，用于数据可视化绘图
import matplotlib.pyplot as plt

# 创建一个包含[1,2,3]的numpy数组，并指定数据类型为int32
a = np.array([1,2,3],dtype=np.int32)

# 打印数组a的内容
print(a)

# 打印数组a的数据类型
print(a.dtype)

# 定义向量v，坐标为[2, 1]
v = np.array([2, 1])

# 定义向量w，坐标为[1, 3]
w = np.array([1, 3])

# 使用matplotlib进行向量可视化
# 创建一个图形和坐标轴对象
"""### 方法参数说明：
- nrows : 子图的行数，默认为1
- ncols : 子图的列数，默认为1
- sharex/sharey : 控制子图是否共享x轴或y轴
- squeeze : 控制返回的坐标轴对象的形状
- width_ratios/height_ratios : 控制子图的宽高比例
- subplot_kw : 传递给子图的关键字参数字典
- gridspec_kw : 传递给网格规范的关键字参数字典
- **fig_kw : 传递给Figure对象的其他关键字参数
### 返回元组中的两个对象：
1. Figure对象 ：
   
   - 代表整个图形窗口或页面
   - 包含所有的坐标轴、标题、标签等元素
   - 可以用来控制整个图形的属性，如大小、背景色、分辨率等
   - 提供了添加、删除和管理坐标轴的方法
2. Axes对象 ：
   
   - 代表图形中的绘图区域（坐标系）
   - 实际的绘图操作（如plot、scatter、bar等）都是在Axes对象上进行的
   - 包含坐标轴、刻度、标签、图例等元素
   - 每个子图都是一个独立的Axes对象
可以理解为fig是画板，ax是画笔，通过ax可以在fig上绘制向量。
   """

fig, ax = plt.subplots()

# 使用quiver函数绘制向量v，从原点(0,0)开始到点(v[0], v[1])
# angles='xy' 表示角度基于xy坐标系
# scale_units='xy' 表示缩放单位基于xy坐标系
# scale=1 表示缩放比例为1
# color='r' 表示颜色为红色
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r')

# 绘制向量w，从原点(0,0)开始到点(w[0], w[1])，颜色为蓝色
ax.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b')

# 绘制向量v+w（向量和），从原点(0,0)开始到点(v[0]+w[0], v[1]+w[1])，颜色为绿色
ax.quiver(0, 0, v[0]+w[0], v[1]+w[1], angles='xy', scale_units='xy', scale=1, color='g')

# 设置x轴的显示范围从-1到4
ax.set_xlim(-1, 4)

# 设置y轴的显示范围从-1到5
ax.set_ylim(-1, 5)

# 添加网格线并显示图形
plt.grid()  # 添加网格线以更好地观察坐标
plt.show()  # 显示绘制的图形