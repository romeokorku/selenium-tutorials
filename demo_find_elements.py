import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        romeo=driver.find_elements_by_tag_name('a')
        print(len(romeo))

    #print list associate with each tag name#
        for i in romeo:
            print(i.text)


        time.sleep(2)

#even though there are multiple tags,it uses the first tag it identifies.

findbyid=DemoFindElementByID()
findbyid.locate_by_id_demo()
driver.close()