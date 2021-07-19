"""
@code: utf-8
@Time : 2021/7/16
@Author : FengYu
作业要求:
题目：XML文件解析
目标：使用类装饰器完成对XML文件的解析，了解python装饰器相关知识。
"""
from lxml import etree
from os import path
import seaborn as sns
import warnings

# 解决中文显示问题，警告
sns.set(style='darkgrid', font='SimHei', rc={'axes.unicode_minus': False})
warnings.filterwarnings('ignore')


class largeXMLParse:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        if len(args) == 2:
            print("执行命令: python3 largeXMLParse.py " + args[0] + " " + args[1])
            print("输出:")
            # lxmld = largeXMLDealer.largeXMLDealer(hi)
            count = self.parse(args[0], args[1])
            print("已经解析了 %d 个XML %s 元素." % (count, args[1]))
        else:
            print("参数错误！")
        return self.__func(*args, **kwargs)

    def parse(self, fileName, elemTag):
        if (not path.isfile(fileName) or not fileName.endswith("xml")):
            raise FileNotFoundError

        count = 0
        es = ('end',)
        ns = self._getNamespace(fileName)
        ns = "{%s}" % ns
        context = etree.iterparse(fileName, events=es, tag=ns + elemTag)
        for event, elem in context:
            # 调用外部函数来处理这里的元素
            try:
                self.dealwithElement(elem)  # 输出元素内容
            except Exception:
                raise Exception("函数参数出错: dealwithElement")
            finally:
                elem.clear()
                count = count + 1
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
        del context
        # 返回已解析的元素数
        return count

    def _getNamespace(self, fileName):
        """"""
        if (not path.isfile(fileName) or not fileName.endswith("xml")):
            raise FileNotFoundError
        result = ''
        es = ('start-ns',)
        context = etree.iterparse(fileName, events=es)
        for event, elem in context:
            prefix, result = elem
            # print("%s, %s",prefix, result)
            # print("%s, %d" % (elem, len(elem)))
            break
        del context
        return result

    def dealwithElement(self, elem):
        if isinstance(elem, object):
            print(elem.text)


@largeXMLParse
def XMLParsing(fileName, elemTag):
    print("解析 %s xml文件的 %s 元素结束！" % (fileName,elemTag))


if __name__ == "__main__":
    print("请输入XML文件名和解析元素名(Ctrl+C退出循环)：")
    while True:
        fileName = input("XML文件名：")
        elemTag = input("解析元素名：")
        # print(fileName)
        # print(elemTag)
        XMLParsing(fileName, elemTag)
        x = input("是否继续(Y/N):")
        if x == 'N' or x == 'n':
            print("结束！")
            break

