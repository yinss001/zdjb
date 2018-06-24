import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.DBconnection import DBConnection


class RegisterTest(MyTestCase):
    def test_register(self):
        #数据库验证测试的正常情况
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        driver.find_element(By.NAME, "username").send_keys("yss6")
        driver.find_element(By.NAME, "password").send_keys("123456")
        driver.find_element(By.NAME, "userpassword2").send_keys("123456")
        driver.find_element(By.NAME, "mobile_phone").send_keys("13577778877")
        driver.find_element(By.NAME, "email").send_keys("8574299@qq.com")
        driver.find_element(By.CLASS_NAME,"reg_btn").click()
        time.sleep(2)
        sql = 'select * from hd_user order by id desc;'
        new_record=DBConnection().execute_sql_command()
        self.assertEqual("yss6",new_record[1])
        self.assertEqual("8574299@qq.com",new_record[2])
        print(new_record)