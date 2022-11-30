import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get("https://training.rcvacademy.com")
#driver.current_url
#driver.back()
#driver.forward()
#driver.refresh()
#driver.title
#driver.maximize_window()
#driver.minimize_window()
#driver.fullscreen_window()
#driver.close()
#driver.quit()



class DemoSeleniumLearning():
    def demo_browser_methods(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://web.facebook.com/?_rdc=1&_rdr")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        time.sleep(4)
        driver.minimize_window()
        driver.refresh()
time.sleep(4)

demobrowser=DemoSeleniumLearning()
demobrowser.demo_browser_methods()
driver.close()
