from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
  
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()