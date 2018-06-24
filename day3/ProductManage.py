import time
from selenium import webdriver
#1.登录海盗商城后台
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("username").submit()
#2.选择商品管理模块
#driver.find_element_by_css_selector("body > div.header > div.menu-box > div.menu.fl > a:nth-child(2)").click()
driver.find_element_by_link_text("商品管理").click()
#3.点击添加商品链接
#driver.find_element_by_xpath("/html/body/div[2]/ul[1]/li[2]/a").click()
driver.find_element_by_link_text("添加商品").click()
#4.输入商品名称
#先点击操作子框架中的元素,首先要进行frame切换
driver.switch_to.frame('mainFrame')
driver.find_element_by_name("name").send_keys("大樱桃")
time.sleep(4)
#driver.find_element_by_xpath("/html/body/div[2]/div[2]/dl/form/dd[1]/ul/li[1]/input").send_keys("大樱桃")
#driver.find_element_by_css_selector("body > div.content > div.install.tabs.mt10 > dl > form > dd:nth-child(1) > ul > li:nth-child(1) > input").send_keys("大樱桃")
#5.选择商品分类(双击或者点击"选择当前分类")
#driver.find_element_by_link_text(" 手机、数码、通讯 ").click()
driver.find_element_by_xpath('//*[@id="2"]').click()
driver.find_element_by_link_text(" 手机通讯 ").click()
driver.find_element_by_link_text(" 手机 ").click()
driver.find_element_by_link_text(" 苹果 (Apple) ").click()
actions=ActionChains(driver)
actions.send_keys(Keys.LEFT).double_click()

#6.在下拉框中选择商品品牌
dropdown=driver.find_element_by_name("brand_id")
Select(dropdown).select_by_visible_text("苹果 (Apple)")
#7.点击提交按钮
driver.find_element_by_class_name("button_search")
#根据以上7步,编写代码,找出第一个不能实现的地方