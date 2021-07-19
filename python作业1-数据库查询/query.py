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
import pymysql.cursors
import seaborn as sns
import warnings

# 解决中文显示问题，警告
sns.set(style='darkgrid', font='SimHei', rc={'axes.unicode_minus': False})
warnings.filterwarnings('ignore')

"""
condition_str:查询条件
*field:选取列的元组，默认为*
**config:数据库配置和选取的表名
return: 数据库连接 conn,是否连接成功 connected,sql语句 sql
"""
def select(*field, condition_str=None, **config):
    if type(field) is not tuple:
        print('错误: 查询列名参数不是元组类型！')

    if type(config) is not dict:
        print('错误: 访问信息参数不是字典类型！')
    else:
        for key in ['host', 'port', 'user', 'pw', 'db']:
            if key not in config.keys():
                print('错误: 访问信息参数字典缺少 %s' % key)
        if 'charset' not in config.keys():
            config['charset'] = 'utf8'
    try:
        conn = pymysql.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            passwd=config['pw'],
            db=config['db'],
            charset=config['charset'],
            cursorclass=pymysql.cursors.DictCursor)
        connected = True
    except pymysql.Error as e:
        print('数据库连接失败:', end='')

    sql = 'SELECT '
    field_num = len(field)
    if field_num == 0:
        sql = sql + "*"
    else:
        for index, item in enumerate(field):
            sql = sql + str(item) + ','
        sql = sql[:-1]

    sql = sql + ' FROM '
    tables = config['table']

    tables_num = len(tables)
    if tables_num == 0:
        print("错误: table参数缺少table")
    else:
        for item in tables:
            sql = sql + str(item) + ','
        sql = sql[:-1]

    sql = sql + ' WHERE ' + str(condition_str)
    return conn, connected, sql

# 数据库配置及查询表名
my_config = {"host": "localhost", "port": 3306, "user": "root", "pw": "123456", "db": "python", "charset": "utf8",
             "table": ["user", "fygd"]}
# 需要查询的列名
my_field = ("id", "name")
my_condition = 'user.id=1 and fygd.name = 1'

conn, connected, sql = select(*my_field, condition_str=my_condition, **my_config)
# SELECT id,name FROM user,fygd WHERE user.id=1 and fygd.name = 1
print(sql)
# True
print(connected)














