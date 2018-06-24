import unittest
import ddt
import time
from selenium import webdriver
#通过ddt代码库,实现数据驱动测试
#为类增加一个装饰器,类似java中的注解
#@ddt.ddt表示这个类实现了数据驱动测试
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


@ddt.ddt
class RegisterTest2(unittest.TestCase):
    #声明一个变量,读取csv文件的测试数据
    data_table=CsvFileManager4().read('test_data.csv')
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()
#4.为test_register方法添加装饰器@ddt.data
    #data_table是一个list类型,包含很多元素
    #在data_table前面加一个*星号,表示调用ddt.data()方法时
    #我们传入的不是列表.而是单独传的列表中的每个元素
    #所以,星号的作用就是.把列表中的每个元素都单独看做一个参数

    @ddt.data(*data_table)
    #5.给方法添加一个参数row
    #如果想取第一列数据,应该是row[1]
    def test_register(self,row):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, "username").send_keys(row[0])
        driver.find_element(By.NAME, "password").send_keys(row[1])
        driver.find_element(By.NAME, "userpassword2").send_keys(row[2])
        driver.find_element(By.NAME, "mobile_phone").send_keys(row[3])
        driver.find_element(By.NAME, "email").send_keys(row[4])
        check_tip = driver.find_element(By.CSS_SELECTOR, "form > ul > li:nth-child(1) > div > span").text
        self.assertEquals("用户名不低于三位，使用中文、数字、字母皆可！", check_tip)
if __name__ == '__main__':
    unittest.main()