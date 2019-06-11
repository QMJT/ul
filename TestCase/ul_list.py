from selenium import webdriver
import time
from selenium.webdriver.support.select import Select



if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.get('http://192.168.60.146:8080/demo1.html')
    time.sleep(3)

    list_1 = driver.find_element_by_xpath('//input[@type="text"]').send_keys('我是傻吊')

    time.sleep(2)

    list_2 = driver.find_element_by_id('file1').send_keys('C:/Users/Administrator/Desktop/搜狗截图20190610162557.png')
    time.sleep(2)

    list_3 = driver.find_elements_by_class_name('radio')
    time.sleep(2)
    list_3[0].click()
    time.sleep(2)
    list_3[1].click()
    time.sleep(2)

    driver

    #关闭 浏览器
    driver.quit()