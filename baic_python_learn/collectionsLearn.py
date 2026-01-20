## tuple（元组）的使用场景：
"""
tuple和Series的区别说明：

tuple（元组）的使用场景：
特性：
- Python内置的不可变序列类型
- 轻量级，占用内存小
- 不可修改（immutable）
- 主要用于数据聚合和打包

典型使用场景：
1. 函数返回多个值
2. 作为字典的键（因为不可变）
3. 数据记录和打包
4. 保护数据不被意外修改

Series（pandas系列）的使用场景：
特性：
- pandas库的数据结构
- 带有索引的一维数组
- 支持向量化操作
- 丰富的统计和数据处理方法

典型使用场景：
1. 数据分析处理
2. 时间序列数据
3. 数据清洗和转换
4. 统计分析和聚合

主要区别总结：
- tuple：不可变，轻量快速，用于数据打包和传递
- Series：可变，功能丰富，用于数据分析和处理

简单来说：
- 用tuple来打包和传递数据
- 用Series来分析和处理数据
"""



import pandas as pd
import numpy as np
#Series学习
def seriesLearn():
    a1 = pd.Series([1,2,3,4,5])
    print(a1)
    print(a1.index)
    print('------------------')
    a2 = pd.Series([1,2,3,4,5],index=['math','english','chinese','history','geography'])
    print(a2)
    print(a2.index)
    print(a2['math'])
    print('------------------')
    a3 = pd.Series(['jim','jason','curry'],index=['小张','小杰','小绿'])
    for name in a3.index:
        print(a3[name])

    for value in a3.values:
        print(value)

    for name,value in a3.items():
        print(name,value)
    print('------------------')
    a4 = {'小张':'jim','小杰':'jason','小绿':None}
    a4 = pd.Series(a4)
    print(a4[a4.notnull()])   #过滤出非空值
    print('------------------')
    for name,value in a4.items():
        if value is None:
           a4[name] = 'todo'
    print(a4[a4.notnull()])  
    a4 = {'小张':'jim','小杰':'jason','小绿':None}
    a4 = pd.Series(a4) 
    a4[a4.isnull()] = 'todo'
    print(a4)
    print('------------------')
    a4 = {'小张':'jim','小杰':'jason','小绿':None}
    a4 = pd.Series(a4) 
    a4.replace({None:'todo'},inplace=True)
    a4.replace({'todo':'green'},inplace=True)
    print(a4)
    print('------------------')
    a4 = {'小张':'jim','小杰':'jason','小绿':None}
    a4 = pd.Series(a4) 
    a4 = a4.fillna('todo',inplace=False)
    print(a4)

#列表学习
def listLearn():
    b1 = np.array(range(1,10,2))
    b2 = np.array(range(2,11,2))
    result = b1 + b2
    print(result)
    print('------------------')
    result = result.tolist()
    print(result[0])
    print(result[-1])   #最后一个元素
    print(result[1:5])  #左闭右开
    print(result[::-1])  #逆序
    print(result[::2])  #所有元素正向每隔一个元素取一个
    print(result[1::2]) #从第二个元素开始，步长为2取
    print(result[0:5:2]) #从第一个元素开始，步长为2取，取到第五个元素（不包括第五个元素）
    print('------------------')

    b3 = range(1,10,2)       #生成一个可迭代对象，元素为1,3,5,7,9
    b3 = list(b3)
    b3.append(10)   #尾插
    b3.insert(1,2)
    print(b3)
    print(id(b3))
    print('------------------')
    
    b3.remove(2)
    b3.pop()   #尾删
    print(b3)
    print(id(b3))

    b3.extend([11,12,13])
    print(b3)




def tupleLearn():
    tu1 = (1,'2',{"name":"luanqs"},[5,6])
    for item in tu1:
        print(item)

    tu2 = tu1 + (6,7,8)
    print(tu2)
    
print('------------------')

def dictLearn():
    dict1 = {'name':'luanqs','age':18,'gender':'male'}
    print(dict1)
    print(dict1['name'])
    print(dict1.get('name'))
    print(dict1.get('sex','todo'))
    print('------------------')
    dict1['age'] = 19
    dict1['sex'] = 'male'
    print(dict1)
    print('------------------')
    dict1.pop('age')
    print(dict1)
    print('------------------')
    dict2 = {('name','age','gender'):('lif',28,'female')}
    print(dict2)
    print('------------------')
    dict3 = dict([("name","jn"),("age",35),("gender","male")])
    print(dict3)
    print('------------------')
    if "name" in dict3:
        for key,value in dict3.items():
            if key == "name" and value == "jn":
                del dict3[key]
                break
    print(dict3)


"""给你一个长度为 n 的整数数组 nums 。请你构建一个长度为 2n 的答案数组 ans ，数组下标 从 0 开始计数 ，对于所有 0 <= i < n 的 i ，满足下述所有要求：

ans[i] == nums[i]
ans[i + n] == nums[i]
具体而言，ans 由两个 nums 数组 串联 形成。

返回数组 ans 。

 

示例 1：

输入：nums = [1,2,1]
输出：[1,2,1,1,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]"""
def getConcatenation(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = nums.copy()
        a.extend(nums)
        return a

"""
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

 

示例 1：

输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
示例 2：

输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]
示例 3：

输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]
"""
def shuffle(nums,n):
    a= []
    for i in range(n):
            a.append(nums[i])
            a.append(nums[i+n])
    return a 
  
def shuffle2(nums,n):
    b = nums[::n]
    c = nums[n:len(nums):1]    
    for i in range(1,n,2):
        b.insert(i,c[i-1])
    return b

   

print(shuffle2([1,2,3,4,4,3,2,1],4))
