import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_css_selector('#login-input').send_keys("test@test.com")
        time.sleep(2)

findbyid=DemoFindElementByID()
findbyid.locate_by_id_demo()
driver.close()