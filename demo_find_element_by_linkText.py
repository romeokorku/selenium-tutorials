import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.find_element_by_link_text('Yatra for Business').click()
        time.sleep(2)

findbyid=DemoFindElementByID()
findbyid.locate_by_id_demo()
driver.close()