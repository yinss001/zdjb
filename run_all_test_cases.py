#这个 文件是用来批量执行unittest的测试用例
#该文件是我们这个测试工具的唯一入口
#1.导入unittest.因为批量执行测试用例的功能有unittest代码库提供
import smtplib
import unittest

import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner
def send_mail(path):
    #1.通过path打开测试报告文件
    #html格式不是文本格式,需要指定打开方式是二进制
    file=open(path,'rb')
    #2.读取文件的内容,作为邮件正文
    msg=file.read()
    #3.把读取出来的内容转换成MIMEText的格式
    #电子邮件类型一般分三种:分别是纯文本plain,html,富文本
    mime=MIMEText( msg, _subtype='html', _charset="utf-8")
    #4.除了正文以外,还需要设置主题,发件人,收件人
    mime['Subject']='海盗商城自动化测试报告'
    #发件人'bwftest126@126.com', 'abc123asd654'
    #因为发件人需要登录密码,这里的密码不是真正的密码,是客户端授权码
    #第三方登录不能直接用密码,必须用授权码
    mime['From']='bwftest126@126.com'

    mime['To']='807298155@qq.com'
    smtp=smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('bwftest126@126.com', 'abc123asd654')
    smtp.send_message(mime, from_addr='bwftest126@126.com', to_addrs='807298155@qq.com')
    smtp.quit()
if __name__ == '__main__':
    #2.要想批量执行,首先要明确你要执行哪些测试用例
    #只能执行继承了unittest.TestCase的类
    #比如执行这个项目中所有的unittest的测试用例
    #defaultTestLoader默认的测试用例加载器,可以用来发现所有的测试用例
    #*表示通配符,可以代替任何字符
    #*Test.py表示以Test.py结尾的所有文件
    #.表示当前路径,及项目的根路径
    #suite随意起名,变量名,suite本身是测试用例集的意思
    suite=unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')
    #suite = unittest.defaultTestLoader.discover('.', pattern='*.py')
    #3.找到测试用例后.执行测试用例
    #TextTestRunner()文本的测试用例的运行器
    #unittest.TextTestRunner().run(suite)
    #4.生成测试报告HTMLTestRunner
    #HTMLTestRunner类似于TextTestRunner,都是批量执行测试用例的
    #区别在于,他们执行完所有测试用例的输出,
    #一个是Text,另一个是HTMl
    #Test会被打印到控制台,HTML会单独生成一个文件
    #相比于Text,HTMl结构更清晰
    #所以二者选其中之一,用HTMLTestRunner代替unittest原生的测试用例运行器TextTestRunner
    #HTMLTestRunner().run(suite)代替unittest.TextTestRunner().run(suite)
    #我们需要把生成的HTML格式的测试报告保存到一个固定位置方便查看
    #在项目根节点下创建一个文件夹,叫report
    #以后生成的测试报告就保存在report下
    #5.定义测试报告的保存目录
    base_pth=os.path.dirname(__file__)
    path=base_pth+'/report/test_report.html'
    #6.创建测试文件
    file=open(path,'wb')

    HTMLTestRunner(stream=file, verbosity=1, title="海盗商城测试报告", description="测试环境:Server2008;浏览器:'Chrome'").run(suite)
    #7.把测试报告作为邮件发送,好处是,可以起到及时提醒的作用
    #前提条件准备2个邮箱
    #版本控制的前提条件.申请一个git账号
    #把html格式的测试报告,作为邮件正文发送
    send_mail(path)