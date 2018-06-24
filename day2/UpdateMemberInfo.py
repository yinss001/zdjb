#1.登录海盗商城
#因为大部分测试用例都会用到登录功能,那么我们把登录功能单独封装成一个方法,
#每次直接调用这个方法就可以了
import time
from selenium import webdriver
#文件名,类名,包名,变量名,都应该以字母开头,可以有数字和下划线,
#但是不能有空格和中文
from day2.loginTest import Login
#我们现在已经创建好一个空白的浏览器了,后续的所有操作都应该在这个浏览器上执行
driver=webdriver.Chrome()
#每次创建浏览器时,implicitly_wait固定写一次,对在这个浏览器上执行的所有代码都生效
#implicitly_wait主要是检测页面的加载时间,检测什么时候页面加载完,什么时候执行后续的操作
driver.implicitly_wait(20)
#实例化对象会占用内存,pycharm会自动帮我们释放内存
#代码运行完,检测到Login()这个对象,不再被使用,系统会自动释放内存
#把driver浏览器传入到方法中
#让登录方法和下面的点击账号设置使用同一个浏览器

Login().loginWithDefaultUser(driver)
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# driver=webdriver.Chrome()
# driver.get("http://localhost/")
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
# driver.find_element_by_link_text("登录").click()
# driver.find_element_by_id("username").send_keys("yss1")
# actions=ActionChains(driver)
# actions.send_keys(Keys.TAB).send_keys("123456").perform()
# driver.find_element_by_id("username").submit()
#2.点击"账号设置"
#本来要点"账号设置",需要使用driver这个变量,但是现在文件中没有driver变量了
#可以重新声明一个driver 吗
driver.find_element_by_link_text("账号设置").click()
#3.点击"个人资料"
#partial_link_text可以使用链接的一部分进行元素定位
#当链接文本过长时,推荐使用partial_link_text
#使用partial_link_text方法时,可以用链接中的任意一部分,只要这部分文字在网页中唯一即可
#driver.find_element_by_link_text("个人资料").click()
driver.find_element_by_partial_link_text("个人资料").click()
#xpath的方法比较通用,可以用工具自动生成,但是不推荐使用,作为一种没有办法时的使用方法
#因为xpath的可读性和可维护性比较差
#4.修改真实姓名
#如果输入框中文本有内容,那么我们修改内容时,往往需要先清空原来的值,用clear()方法
#实际上,一个良好的编程习惯是在每次sendkeys之前,都应该先做clear操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("李四")
#5.修改性别
#通过观察发现,保密,男,女三者唯一的区别就是value属性的值不同
#要想通过value属性定位有两种方法:xpath和css_selector
#通过css_selector定位元素,只需要在唯一属性的两边加一对中括号即可
#driver.find_element_by_css_selector('[value="2"]').click()
#在xpath中,//表示采用相对路径定位元素,一般通过元素的特殊属性查找元素
#/表示绝对路径,一般都是从/html根节点开始定位元素,一般通过元素的位置,层级关系查找元素
#绝对路径比较长,涉及到的节点比较多,当开发人员修改页面布局时,受到影响的可能性比较大
#相对路径,查询速度比较慢,因为可能需要遍历更多的节点
#工作中推荐用css_selector
#css_selector的查询速度比xpath快一点
#xpath在某些浏览器上支持的不太好,比如IE8
#css_selector所有前端开发都会用,易于沟通交流
#*表示任意节点,[@]表示通过属性定位
#driver.find_element_by_xpath('//*[@value="2"]').click()
#javascript的getElementsByClassName()方法可以找到页面上符合条件的所有元素
#然后下标选取其中第n个元素,也可以用于定位,selenium也可以
#要找页面上所有符合条件的元素就用find_elements
#要找页面上唯一符合条件的元素用find_element
driver.find_elements_by_id("xb")[2].click()
#6.修改生日
#一下一下点年月日是可以实现的,但是稳定性比较差,很容易点错
#并且很难修改日期,比如写完1990-02-02,下次想换个日期,还需要重新定位,所以尽量不要click()点击选日期
#我们右键检查,发现日历控件是一个input文本输入框,但是不能用send_keys,因为readonly属性,写一个javascript,删除readonly属性
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1989-05-05")
#7.修改QQ
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("7899900")
#8.点击确定,保存成功
driver.find_element_by_class_name("btn4").click()
time.sleep(3)
driver.switch_to.alert.accept()