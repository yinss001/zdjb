#selenium执行javascript中的两个关键字:return(返回值)和arguments(参数)
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("http://localhost")
#点击"登录"链接
#用javascript的方法找登录链接的代码
#document.getElementsByClassName("site-nav-right fr")[0].childNodes[1]
#用selenium的方法找登录链接的代码:
#driver.find_element_by_link_text("登录")
#某些元素,用selenium的方法找元素比javascript更容易
#虽然selenium不支持recoceAttribute的方法
#但是selenium找到登录链接和javascript找到的是同一个元素
#我们可不可以用selenium找到元素后,转换成javascript的元素?
#这样以后写javascript就容易很多,不需要childNodes这些方法了
#比如,driver.find_element_by_link_text("登录"),removeAttribute()(此种写法是不支持的)
#driver.execute_script("document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute('target')")
login_link=driver.find_element_by_link_text("登录")
#把原来的javascript看成是一个无参无返的方法,现在直接从外面传入一个页面元素,就变成了一个有参无返的方法,把selenium找到的元素,传入到javascript方法里,代替原来的javascript定位
#arguments参数的复数形式,[0]表示第一个参数,指的就是js后面的login_link
#相当于把driver.find_element_by_link_text("登录")带入到javascript语句中
#变成了driver.find_element_by_link_text("登录"),removeAttribute()
#arguments是参数数组,指的是js字符串后面的所有参数
#一般情况下我们只用到arguments[0],即js后面的第一个字符串
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
#登录
driver.find_element_by_id("username").send_keys("yss1")
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
#driver.find_element_by_id("password").send_keys("123456")
#driver.find_element_by_id("password").submit()
time.sleep(5)

#返回商城首页
driver.find_element_by_link_text("进入商城购物").click()
#搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#点击商品(用这种方法在实现一次)
#因为img没有target属性,所以我们复制xpath的时候要找他的父节点a标签
#复制出来的css往往比较长,我们可以适当的缩写长度
#我们定位元素的目标节点是最后一个节点
#大于号>的前面是父节点,后面是子节点
#每个节点的第一个单词是标签名,比如a,div,body
#小数点后面表示class属性
#:nth-child(2),nth表示第几个,4th,5th,nth表示第n个,child表示子节点
#所以.:nth-child(2)表示当前标签是他的父节点的第二个子节点
product_link_css="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a"
product_link_xpath="/html/body/div[3]/div[2]/div[3]/div/div[1]/a"
iphone=driver.find_element_by_xpath(product_link_xpath)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
#购买商品
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_css_selector(".shopCar_T_span3").click()
#点击结算按钮
#driver.find_element_by_class_name("shopCar_btn_03").click()
#在每个class前面都加一个小数点,并且去掉中间的空格,我们就可以同时用两个属性定位一个元素
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
#点击添加新地址
driver.find_element_by_class_name("add-address").click()
#输入收货人等信息
driver.find_element_by_name("address[address_name]").clear()
driver.find_element_by_name("address[address_name]").send_keys("yss111")
driver.find_element_by_name("address[mobile]").clear()
driver.find_element_by_name("address[mobile]").send_keys("18744444444")
#下拉框是一种特殊的网页元素,对下拉框的操作和普通网页元素不太一样
#selenium为这种特殊的元素专门创建了一个类select
#dropdown1的元素类型是一个普通的网页元素
dropdown1=driver.find_element_by_id("add-new-area-select")
#把一个普通的网页元素,转换成一个下拉框的特殊网页元素
print(type(dropdown1))#dropdown1是WebElement类型
#WebElement这个类中,只有click和send_keys这样的方法,没有选择下拉框选项的方法
select1=Select(dropdown1)
print(type(select1))#select1是Select类型
#转换成select类型后,网页元素没有变,但是Select类中有选择选项的方法
select1.select_by_value("210000")#这时,我们就可以通过选项的值来定位
time.sleep(2)
select1.select_by_visible_text("吉林省")#也可以通过选项的文本信息进行定位
#因为是动态Id,所以不能通过id来进行定位市区
#因为class重复,所以我们也不能直接用class定位
#但是我们可以用find_elements的方法,先找到页面中所有class=add-new-area-select     的元素
#然后通过下标的方式选择第n个页面元素,类似与javascript方法
time.sleep(2)
dropdown2=driver.find_elements_by_class_name("add-new-area-select")[1]
Select(dropdown2).select_by_visible_text("长春市")
time.sleep(2)
#dropdown3=driver.find_elements_by_class_name("add-new-area-select")[2]
#tag_name()方法,大多数情况都能找到一堆元素
#所以.find_element_by_tag_name()这个方法很少用
#但是find_elements_by_tag_name()[]这个方法比较常用
dropdown3=driver.find_elements_by_tag_name("select")[2]
Select(dropdown3).select_by_visible_text("宽城区")

time.sleep(3)
driver.find_element_by_name("address[address]").send_keys("详细地址啦")
time.sleep(3)
driver.find_element_by_name("address[zipcode]").send_keys("100102")
time.sleep(3)
#点击确定
driver.find_element_by_class_name("aui_state_highlight").click()