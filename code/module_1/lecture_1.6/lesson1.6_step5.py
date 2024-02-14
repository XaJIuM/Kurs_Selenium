import math                                    # Скачиваем библиотеку для работы с математическими функциями
import time                                    # Скачиваем библиотеку для работы со временем и датами
from selenium import webdriver                 # Используем для работы с Selenium
from selenium.webdriver.common.by import By    # Используем для работы с элементами "By"

# Переменные
link = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()                                         # Открываем браузер
    browser.get(link)                                                    # Переходим по ссылке(В данном случае это переменная)

    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))    #Находим элемент ссылки на странице
    link.click()                                                         # Кликаем по ссылке

    input2 = browser.find_element(By.TAG_NAME, "input")                  # Находим поле "first_name"
    input2.send_keys("Ivan")                                             # Вводим в поле "first_name" имя "Ivan"
    input3 = browser.find_element(By.NAME, "last_name")                  # Находим поле "last_name"
    input3.send_keys("Petrov")                                           # Вводим в поле "last_name" фамилию "Petrov"
    input4 = browser.find_element(By.CLASS_NAME, "form-control.city")    # Находим поле "city"
    input4.send_keys("Smolensk")                                         # Вводим в поле "city" город "Smolensk"
    input5 = browser.find_element(By.ID, "country")                      # Находим поле "country"
    input5.send_keys("Russia")                                           # Вводим в поле "country" страну "Russia"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")         # Находим кнопку "Submit"
    button.click()                                                       # Кликаем по кнопке "Submit"

finally:
    time.sleep(30)                                                       # Устанавливаем задержку 30 сек перед закрытием браузера
    browser.quit()                                                       # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!