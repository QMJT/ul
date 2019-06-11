from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
driver.get('http://192.168.60.146:8080/demo1.html')



if __name__ == '__main__':
    action_chains = ActionChains(driver)
    text_1= driver.find_element_by_link_text('当当')
    action_chains.key_down(Keys.CONTROL).click(text_1).key_up(Keys.CONTROL).perform()
    time.sleep(5)


    window_handles=driver.window_handles
    for i
