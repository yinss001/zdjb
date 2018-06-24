import time
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase


class LoginTest(MyTestCase):
    #这时.这个类不需要在写setUp和teatDown方法了
    #只需要写测试用例方法即可
    def test_login(self):
        driver=self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element(By.NAME,"username").send_keys("yss1")
        driver.find_element(By.NAME,"password").send_keys("123456")
        old_title=driver.title
        driver.find_element(By.CLASS_NAME,"login_btn").click()
        time.sleep(5)
        new_title=driver.title
        print(old_title)
        print(new_title)
        self.assertNotEqual(old_title,new_title)

        print(driver.current_url)
