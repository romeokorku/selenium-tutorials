import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class DemoMultipleWindow():
    def demo_window(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        parent_handle=driver.current_window_handle
        print(parent_handle)
        driver.find_element_by_xpath("//a[@title='Niyo Global HP']//img[@class='conta iner large-banner']").click()
        all_handles=driver.current_window_handles
        print(all_handles)

        handle: object
        for handle in all_handles:
            if handle !=parent_handle:
                driver.switch_to.window(handle)
                driver.find_element_by_xpath("//a[normalize-space()='Know about Niyo Global']")
                break


findbycheck=DemoMultipleWindow()
findbycheck.demo_window()
driver.close()






