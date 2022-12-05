import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class DemoCheckboxes():
    def demo_checkbox(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.find_element_by_xpath("//a[normalize-space()='Non Stop Flights']").click()
        driver.find_element_by_xpath("//a[normalize-space()='Student Fare']").click()
        var_1=driver.find_element_by_xpath("//a[normalize-space()='Non Stop Flights']").is_selected()
        print(var_1)
        driver.find_element_by_xpath("//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
        time.sleep(2)

findbycheck=DemoCheckboxes()
findbycheck.demo_checkbox()
driver.close()






