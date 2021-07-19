"""
@code: utf-8
@Time : 2021/7/16
@Author : FengYu
作业要求:
函数修饰器:修饰器包括可以生成一个随机数的生成器，参数为随机数的数量和范围,
被修饰函数是散点图生成函数，将修饰器生成的随机数以散点图形式输出
"""
# 导入包
import matplotlib.pyplot as plt
from functools import wraps
import random
import seaborn as sns
import warnings

# 解决中文显示问题，警告
sns.set(style='darkgrid', font='SimHei', rc={'axes.unicode_minus': False})
warnings.filterwarnings('ignore')

"""
生成随机数组（整数型的）:
min：起始位置
max：结束位置
num：个数 大于等于0
random.randint(参数1，参数2) 参数1、参数2必须是整数
len = int(abs(len)) if len else 0
"""
def generate_random(min, max, num):
    if(min <= max):
        min, max = int(min), int(max)
    else:
        min, max = int(max), int(min)
    if(num < 0):
        num = 0
    else:
        num = int(abs(num))
    # 设置随机数组
    random_arr = []
    for i in range(num):
        random_arr.append(random.randint(min, max))
        print("-----------添加后的随机数组：\n", random_arr)
    print("-----------for循环结束，最终的随机数组：\n", random_arr)
    return random_arr

"""
函数修饰器：
函数修饰器是 Python 的一个重要部分。
简单地说：他们是修改其他函数的功能的函数。
@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。
这可以让我们在装饰器里面访问在装饰之前的函数的属性
"""
def decorators(num, min, max):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            x = generate_random(min, max, num)
            y = generate_random(min, max, num)
            f(x, y)
        return wrapper
    return decorator


# 使用 @ 来运行之前的代码 decorators(num, min, max)
@decorators(50, 1, 30)


# 散点图函数
def plt_scatter(x, y):
    plt.figure(figsize=(10, 10), dpi=100)
    plt.scatter(x, y)
    plt.xlabel("X", fontdict={'size': 16})
    plt.ylabel("Y", fontdict={'size': 16})
    plt.title("冯瑜-2020103139-PythonHomework4", fontdict={'size': 20})
    plt.show()


# 调用函数，生成随机数组并画出散点图
plt_scatter()
