import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

class DemoDropdownSingleSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/form/signup/freetrial-elf-v2/?d=70130000000EqoP")
        dropdown=driver.find_element_by_name("CompanyCountry")
        dd=Select(dropdown)

        dd.select_by_index(1)

        dd.select_by_value("GH")

        dd.select_by_visible_text("Ghana")

dddemo=DemoDropdownSingleSelect()
dddemo.demo_dropdown()









