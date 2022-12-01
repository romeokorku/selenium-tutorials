import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class DemoHiddenElements():
    def demo_is_displayed(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        displayed=driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(displayed)
        driver.find_element_by_xpath("//button[normalize-space()='Toggle Hide and Show']").click()
        displayed_2=driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(displayed_2)

demohidden=DemoHiddenElements()
demohidden.demo_is_displayed()
driver.close()
#//input[@id='login_button']