"""
@code: utf-8
@Time : 2021/7/16
@Author : FengYu
作业要求:
题目：XML文件解析
目标：使用类装饰器完成对XML文件的解析，了解python装饰器相关知识。
"""
# 导入包
import xml.sax
import seaborn as sns
import warnings

# 解决中文显示问题，警告
sns.set(style='darkgrid', font='SimHei', rc={'axes.unicode_minus': False})
warnings.filterwarnings('ignore')

"""
XML文件解析
"""
class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")

            title = attributes["title"]
            print("Title:", title)


    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)

        elif self.CurrentData == "format":
            print("Format:", self.format)

        elif self.CurrentData == "year":
            print("Year:", self.year)

        elif self.CurrentData == "rating":
            print("Rating:", self.rating)

        elif self.CurrentData == "stars":
            print("Stars:", self.stars)

        elif self.CurrentData == "description":
            print("Description:", self.description)

        self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")