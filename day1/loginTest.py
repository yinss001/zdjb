#这个文件用来实现一个登录功能的自动化操作
#表示注释
#从谷歌公司的一个项目导入网络(web)驱动(driver),用来操作浏览器的
import time
from selenium import webdriver
#1.打开浏览器
driver=webdriver.Chrome()
#2.打开海盗商城网站
driver.get("http://localhost/")
#3.打开登录页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#4.输入用户名和密码
driver.find_element_by_id("username").send_keys("yss1")
driver.find_element_by_name("password").send_keys("123456")
#5.点击登录按钮
#所有调用方法,都会有提示信息,没有提示信息,就说明没有这个方法
driver.find_element_by_class_name("login_btn").click()
#6.检查登录是否成功,按照现在所学,还不能定位用户名信息,稍后考虑
#Alt+Enter 导包快捷键,选import this name,选最短的time
time.sleep(5)
username_text=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)
#我们可以通过if语句,判断页面显示的文本和预期的文本是否一致,来判断测试用来是否正常执行
if username_text=='您好 yss1':
    print("测试执行通过")
else:
    print("测试执行失败")
#因为selenium主要做回归测试,所以测试脚本都是pass的,只有开发做了代码变更,我们的测试用例才有可能失败
#一般工作中不用if....else 语句判断,后面再详细讨论这个问题
#7.点击"进入商城购物按钮"
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
#xpath有一个缺点,定位元素的可读性比较差
driver.find_element_by_link_text("进入商城购物").click()
#8.在商城主页,输入搜索条件"iphone"
driver.find_element_by_name("keyword").send_keys("iphone")
#9.点击搜索按钮
driver.find_element_by_class_name("btn1").click()
time.sleep(7)
#10.在搜索结果页,点击第一个商品的图片
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a/img").click()
# 窗口切换
driver.close() #关闭selenium正在工作的窗口
driver.switch_to.window(driver.window_handles[-1])
# 11.点击"加入购物车"
driver.find_element_by_id("joinCarButton").click()
