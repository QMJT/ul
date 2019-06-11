from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

def driver_uu():
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.get('http://192.168.60.146:8080/demo1.html')

    time.sleep(3)
    input_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    input_el.send_keys('啦啦啦啦啦啦拉拉拉拉啦')
    time.sleep(3)
    #清除
    input_el.clear()
    time.sleep(3)
    #关闭浏览器
    driver.quit()


def  kiki_l():
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.get('http://192.168.60.146:8080/demo1.html')
    time.sleep(3)
    #
    input_el = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/input')
    input_el.send_keys('啦啦啦啦啦啦拉拉拉拉啦')
    time.sleep(3)

    #
    input_id = driver.find_element_by_id('file1')
    input_id.send_keys('C:/Users/Administrator/Desktop/搜狗截图20190610162557.png')
    time.sleep(2)
    # 关闭浏览器
    driver.quit()
    #
    radio_els = driver.find_elements_by_name('radio')
    print(type(radio_els))
    radio_els[0].click()
    time.sleep(2)
    radio_els[1].click()
    time.sleep(2)
    # 关闭浏览器
    driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.get('http://192.168.60.146:8080/demo1.html')
    time.sleep(3)


    # checkbox_els = driver.find_elements_by_class_name('checkbox')
    # print(checkbox_els)
    # checkbox_els[0].click()
    # time.sleep(3)
    # checkbox_els[1].click()
    # time.sleep(3)
    # checkbox_els[2].click()
    # time.sleep(3)

    # typr_els = driver.find_element_by_xpath('/html/body/table/tbody/tr[7]/td[2]/input').send_keys(1478542)
    # time.sleep(3)
    #
    #
    # typr_els.clear()
    # time.sleep(3)

    # select_els = driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select')
    # time.sleep(3)
    # c = Select(select_els)
    #
    # c.select_by_value('z1')
    # time.sleep(2)
    # c.select_by_value('z2')
    # time.sleep(2)
    # c.select_by_value('z0')
    # time.sleep(2)

    driver.find_element_by_link_text('当当').click()
    time.sleep(2)
    #还回
    driver.back()
    time.sleep(2)
    driver.find_element_by_link_text('问问度娘').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)


    # 关闭浏览器
    driver.quit()


