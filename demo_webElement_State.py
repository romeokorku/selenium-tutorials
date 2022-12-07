import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class DemoElement_State():
    def demo_enable_disable(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        element_state_1 = driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(element_state_1)

        driver.find_element_by_name("user_name").send_keys("romeo")
        time.sleep(2)
        driver.find_element_by_name('user_pass').send_keys("avemegah")
        element_state_2=driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(element_state_2)

element_state_1=DemoElement_State()
element_state_1.demo_enable_disable()
driver.close()

#//input[@id='login_button']
