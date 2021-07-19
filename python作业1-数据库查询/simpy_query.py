"""
@code: utf-8
@Time : 2021/7/16
@Author : FengYu
作业要求:
题目：采用函数封装SQL查询语句
目标：熟练掌握函数封装的4种参数类型的使用
要求：
1. 此函数能够根据输入的任意查询信息合成符合SQL语法要求的查询语句
2. 函数输入包括数据库服务器的访问信息（IP，端口等），数据库的访问信息（数据库名称，访问权限等），任意查询条件，任意查询目标
3. 函数输出为一条字符串，内容是满足输入目标的SQL语句
4. 另写一个测试函数调用SQL语句生成函数，通过传参得到相应的SQL查询语句
5. 至少满足在单一数据库的多表查询需求，即无论测试函数的输入如何变化，SQL语句生成函数都不需要修改代码就能得到正确输出*
6. 仅考虑常规数据库查询操作即可，无需考虑极端查询问题
"""
# 导入包
import pymysql
import seaborn as sns
import warnings

# 解决中文显示问题，警告
sns.set(style='darkgrid', font='SimHei', rc={'axes.unicode_minus': False})
warnings.filterwarnings('ignore')

# 打开数据库连接
db = pymysql.connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")
finally:
 # 关闭数据库连接
 db.close()
