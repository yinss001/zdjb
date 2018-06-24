from selenium.webdriver.common.by import By


class MemberCenterPage:
    def __init__(self,driver):
        #self.driver=webdriver.Chrome()
        self.driver=driver
        self.url="http://localhost/index.php?m=user&c=index&a=index"
    welcome_link_loc=(By.PARTIAL_LINK_TEXT,"您好")
    '''get_welcome_link_text()用于返回"您好"链接的所有文本内容.这是页面上实际结果'''
    def get_welcome_link_text(self):
        return self.driver.find_element(*self.welcome_link_loc).text
    #如果当前类中,赋值driver时,没有先用driver=webdriver.Chrome()
    #那么后面写代码.想用selenium方法时,因为IDE不知道driver的类型,就不会给出提示信息
    #
