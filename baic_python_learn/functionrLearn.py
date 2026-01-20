import numpy as np
import pandas as pd
def prc1(*args):                           #args是一个元组，包含所有位置参数
    for i in args:
        print(i)
def prc2(**kwargs):                        #kwargs是一个字典，包含所有关键字参数
    for key,value in kwargs.items():
        print(key,value)

def prc3(name,age):                     #name和age是位置参数，必须按顺序传递
    print(name,age)

def prc4(*args,**kwargs):              #args是一个元组，包含所有位置参数，kwargs是一个字典，包含所有关键字参数，不要求按顺序传递
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)
def prc5(name,age,sex = "unknow"):           #name和age是位置参数，必须按顺序传递，kwargs是一个字典，包含所有关键字参数，不要求按顺序传递
    print(name,age,sex)

def prc6(*args):                           
    for i in args:
        if isinstance(i,list):                 #对于可变参数，直接修改其值，会影响到原始参数
            i.append("a")
        if isinstance(i,int):                  #对于不可变参数，不能直接修改其值，只能返回一个新的对象
            i=i*2
    print(args)

def smallerNumbersThanCurrent(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)  # 初始化结果列表，避免索引错误
        gc1 = []
        for i,value in enumerate(nums):
            gclist = [value,i]  # 创建一个列表，包含当前值和其索引
            gc1.append(gclist)
        gc1 = sorted(gc1,key = lambda x:x[0])

        for j,jvalue in enumerate(gc1):
            res[jvalue[1]] = j 
        
        return res
        

parm1 = 1
parm2 = ["1","2"]
parm3 = {"1":"a","2":"b"}
parm4 = pd.Series([1,2,3])
#prc1(parm1,parm2,parm3,parm4)
#prc2(param1=parm1, param2=parm2, param3=parm3, param4=parm4)
#args = ["小胖",23]
#prc3(*args)    #*args将元组args解包，作为位置参数传递给prc3
#kwargs = dict(name = "小胖", age = 23)
#prc3(**kwargs)    #**kwargs将字典kwargs解包，作为关键字参数传递给prc3

#prc4(parm1,parm2,parm3,parm4)
#prc5("小胖",23)
#prc6(parm1,parm2)
#print(parm1,parm2)
add = lambda x,y:x+y
#print(add(1,2))
numbers = [1,2,2,4]
numdict = [["b",1],["a",2],["c",3]]
result = map(lambda x:x.append("a"),numdict)  #map()函数将lambda函数应用到numbers的每个元素上，返回一个新的迭代器
#result = filter(lambda x:x%2==0,numbers)  #filter()函数将lambda函数应用到numbers的每个元素上，返回一个新的迭代器，只保留返回值为True的元素
print(list(result))
print(numdict)
print(smallerNumbersThanCurrent([8,1,2,2,3]))  #高阶函数对可迭代对象进行解包，将每个元素作为参数传递给lambda函数

# 演示不同的列表初始化方法
print("\n=== 列表初始化方法演示 ===")
nums = [8, 1, 2, 2, 3]

# 1. 使用乘法操作符（当前方法）
res1 = [0] * len(nums)
print(f"方法1（乘法）: {res1}")

# 2. 使用列表推导式
res2 = [0 for _ in range(len(nums))]
print(f"方法2（推导式）: {res2}")

# 3. 使用append循环
res3 = []
for _ in range(len(nums)):
    res3.append(0)
print(f"方法3（循环）: {res3}")

# 4. 使用numpy（如果可用）
try:
    import numpy as np
    res4 = np.zeros(len(nums), dtype=int).tolist()
    print(f"方法4（numpy）: {res4}")
except ImportError:
    print("numpy不可用")

# 5. 不同初始值示例
res5 = [""] * len(nums)        # 空字符串
res6 = [None] * len(nums)      # None值
res7 = [i*2 for i in range(len(nums))]  # 根据索引计算初始值
print(f"空字符串初始化: {res5}")
print(f"None初始化: {res6}")
print(f"根据索引计算: {res7}")

# 注意：对于可变对象的陷阱
print("\n=== 可变对象初始化陷阱 ===")
wrong_list = [[]] * 3
right_list = [[] for _ in range(3)]

print(f"错误方法（所有元素引用同一个列表）: {wrong_list}")
print(f"正确方法（每个元素都是独立列表）: {right_list}")

# 验证陷阱
expected_list = [[] for _ in range(3)]
print(f"预期结果: {expected_list}")



