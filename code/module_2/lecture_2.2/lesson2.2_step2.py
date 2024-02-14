import time                                                              # Скачиваем библиотеку для работы со временем и датами     
import math                                                              # Скачиваем математическую библиотеку
from selenium import webdriver                                           # Используем для работы с Selenium
from selenium.webdriver.common.by import By                              # Используем для работы с элементами "By"
from selenium.webdriver.support.ui import Select                         # Используем для работы с выпадающими списками

# Переменные
link = "https://suninjuly.github.io/selects1.html"

try:                                                             
    browser = webdriver.Chrome()                                               # Открываем браузер
    browser.get(link)                                                          # Переходим по ссылке(В данном случае по переменной)

    num1 = browser.find_element(By.ID, "num1").text                            # Находим элемент на странице
    num2 = browser.find_element(By.ID, "num2").text                            # Находим элемент на странице
    num3 = str(int(num1)+int(num2))                                            # Выполняем математическое действие с переменной "num1" и "num2" и заводим в переменную "num3"
    select = Select(browser.find_element(By.ID, "dropdown"))                   # Находим элемент с выпадающим списком 
    select.select_by_value(num3)                                               # Ищем элемент со значением из переменной "num3"
    
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-default"]').click()             # Находим кнопку "Submit" и кликаем по ней

finally:
    time.sleep(10)                                                             # Устанавливаем задержку 10 сек перед закрытием браузера
    browser.quit()                                                             # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!