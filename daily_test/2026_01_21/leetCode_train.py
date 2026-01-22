class Solution(object):
    """
    给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
重点是接触到了python的列表操作，比如[::-1]可以实现列表的反转，map(str,trandigts)可以将列表中的元素转换为字符串，
''.join()可以将列表中的元素连接起来。
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        digts = [int(d) for d in str(abs(x))]
        trandigts = digts[::-1]
        for index,i in enumerate(trandigts):
            if trandigts[0]==0:
                trandigts.remove(0)
            else:
                break
        


        #num = 0
        #for digt in trandigts:
         #   num = num*10+digt
        num = int(''.join(map(str,trandigts)))

        if num>(231-1) or num<(-231):
            return 0
        if x>0:
            return num
        else:
            return -num

"""
给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。
重点是学习了地板除，即//，得到的结果是商的整数部分向下取整，所以要注意如果是负数，商的整数部分要向负无穷取整。
整数则是向0取整，即向最近的整数取整。
"""
class Solution2(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==0 or divisor==0:
            return 0
        symbol = dividend/divisor
        res = abs(dividend)//abs(divisor)
        if symbol<0:
            res = -res
        if res>(231-1):
            res = 231-1
        if res<(-231):
            res = -231
        return res


"""
将输入的两个字符串表示的非负整数相乘，返回一个字符串表示的乘积，不可用直接将字符串转换为整数进行相乘。
"""
class Solution3(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1List = [int(d) for d in num1]

        num2List = [int(d) for d in num2]

        num1= 0
        num2= 0

        for index,i in enumerate(num1List):
            num1 = num110+i
        for index,i in enumerate(num2List):
            num2 = num210+i
        res = num1*num2
        return str(res)
    

    
class Solution4(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        tlist = list(range(1,n+1,1))
        res = []

        while len(tlist) > 0:
            perm = self.permutation(len(tlist)-1)
            div = (k-1) // perm
            first = tlist[div]
            res.append(first)
            tlist.remove(first)
            k = k - div * perm

        return ''.join(map(str,res))


    def permutation(self,num):
        if num<0:
            return None
        res = 1
        for i in range(1,num+1):
            res = res*i
        return res

               
        
if name == 'main':
    s = Solution4()
    print(s.getPermutation(4,9))