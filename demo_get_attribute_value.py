from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class DemoGetAttributeValue():
    def demo_getvalue(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        attibute_value = driver.find_element_by_xpath("//div[@id='credit-shellBtnID']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(attibute_value)

attrobj=DemoGetAttributeValue()
attrobj.demo_getvalue()
driver.close()
