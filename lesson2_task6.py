from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

input1 = browser.find_element_by_class_name("form-control")
input1.send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option1 = browser.find_element_by_id("robotsRule")
option1.click()

button = browser.find_element_by_class_name("btn.btn-primary")
button.click()

time.sleep(30)
browser.quit()