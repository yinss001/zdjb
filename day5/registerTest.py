import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.csvFileManager4 import CsvFileManager4


class RegisterTest(unittest.TestCase):
    #3.重写setup和teardown方法
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(30)
        cls.driver.quit()

    #4.编写一个测试用例方法
    def test_register(self):
        for row in CsvFileManager4().read('test_data.csv'):
            driver=self.driver
            driver.get("http://localhost/index.php?m=user&c=public&a=reg")
            driver.find_element(By.NAME,"username").send_keys(row[0])
            driver.find_element(By.NAME,"password").send_keys(row[1])
            driver.find_element(By.NAME,"userpassword2").send_keys(row[2])
            driver.find_element(By.NAME,"mobile_phone").send_keys(row[3])
            driver.find_element(By.NAME,"email").send_keys(row[4])
         #   driver.find_element(By.CLASS_NAME,"reg_btn").click()
            check_tip=driver.find_element(By.CSS_SELECTOR,"form > ul > li:nth-child(1) > div > span").text
            print(check_tip)
            # if check_tip=="通过信息验证!":
            #     print("测试通过")
            # else:
            #     print("测试失败")
            self.assertEquals("通过信息验证!",check_tip)
if __name__ == '__main__':
    unittest.main()