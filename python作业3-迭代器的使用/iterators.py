"""
@code: utf-8
@Time : 2021/7/16
@Author : FengYu
作业要求:迭代器的使用
迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器
"""
# 导入包
import seaborn as sns
import warnings

# 解决中文显示问题，警告
sns.set(style='darkgrid', font='SimHei', rc={'axes.unicode_minus': False})
warnings.filterwarnings('ignore')

"""
创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。在 30 次迭代后停止执行
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 30:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
# 调用
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print("-----------每次x的值：\n", x)






