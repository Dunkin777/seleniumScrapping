# -*- coding: utf-8 -*-
import time
from selenium import webdriver

URL = 'https://xn--90adear.xn--p1ai/r/65/news'

driver = webdriver.Chrome(executable_path="chromedriver/chromedriver.exe")

urls = []
try:
    driver.get(url=URL)
    time.sleep(5)
    arrayOfElements = driver.find_elements_by_class_name("sl-item-title")
    for elem in arrayOfElements:
        urls.append(elem.find_element_by_tag_name("a").get_attribute("href"))

    for i in range(2, 207):
        element = driver.find_element_by_class_name("paginator").find_element_by_link_text(f"{i}")
        element.click()
        time.sleep(10)
        arrayOfElements = driver.find_elements_by_class_name("sl-item-title")
        for elem in arrayOfElements:
            urls.append(elem.find_element_by_tag_name("a").get_attribute("href"))

    with open("Texts/text.txt", "a") as file:
        for url in urls:
            driver.get(url=url)
            time.sleep(5)
            h2 = driver.find_element_by_tag_name("h2").text
            p = driver.find_element_by_class_name("article-text").text
            file.write(h2)
            file.write('\n')
            file.write(p)
            file.write('\n' * 3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
