import time                                                              # Скачиваем библиотеку для работы со временем и датами
import os                                                                # Скачиваем библиотеку для работы с файлами
from selenium import webdriver                                           # Используем для работы с Selenium
from selenium.webdriver.common.by import By                              # Используем для работы с элементами "By"
 

# Переменные
link = "https://suninjuly.github.io/file_input.html"

try:                                                             
    browser = webdriver.Chrome()                                                 # Открываем браузер
    browser.get(link)                                                            # Переходим по ссылке(В данном случае по переменной)

    input1 = browser.find_element(By.NAME, 'firstname')                          # Находим поле "first_name"
    input1.send_keys("Ivan")                                                     # Вводим в поле "first_name" имя "Ivan"
    input2 = browser.find_element(By.NAME, 'lastname')                           # Находим поле "last_name"
    input2.send_keys("Petrov")                                                   # Вводим в поле "last_name" фамилию "Petrov"
    input3 = browser.find_element(By.NAME, 'email')                              # Находим поле "email"
    input3.send_keys("email@mail.ru")                                            # Вводим в поле "email" домен "email@mail.ru"
    input4 = browser.find_element(By.CSS_SELECTOR, "[type='file']")              # Находим кнопку "Выберите файл" и кликаем по ней 
    current_dir = os.path.abspath(os.path.dirname(__file__))                     # Указываем путь до файла в папке где лежит скрипт и возводим в переменную "current_dir"
    file_name = "file.txt"                                                       # Название файла возводим в переменную "file_name"
    file_path = os.path.join(current_dir, 'file.txt')                            # Указываем путь и имя файла   
    input4.send_keys(file_path)                                                  # Вкладываем файл, записанный в переменной "file_path"        
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()       # Находим кнопку "Submit" и кликаем на нее
    
finally:
    time.sleep(10)                                                       # Устанавливаем задержку 30 сек перед закрытием браузера
    browser.quit()                                                       # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!