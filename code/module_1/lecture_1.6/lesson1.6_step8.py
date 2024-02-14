import time                                                              # Скачиваем библиотеку для работы со временем и датами
from selenium import webdriver                                           # Используем для работы с Selenium
from selenium.webdriver.common.by import By                              # Используем для работы с элементами "By"
 

# Переменные
link = "http://suninjuly.github.io/find_xpath_form"

try:                                                             
    browser = webdriver.Chrome()                                                          # Открываем браузер
    browser.get(link)                                                                     # Переходим по ссылке(В данном случае по переменной)

    input1 = browser.find_element(By.XPATH, '//input')                                    # Находим поле "first_name"
    input1.send_keys("Ivan")                                                              # Вводим в поле "first_name" имя "Ivan"
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')                 # Находим поле "last_name"
    input2.send_keys("Petrov")                                                            # Вводим в поле "last_name" фамилию "Petrov"
    input3 = browser.find_element(By.XPATH, '//input[@class="form-control city"]')        # Находим поле "city"
    input3.send_keys("Smolensk")                                                          # Вводим в поле "city" город "Smolensk"
    input4 = browser.find_element(By.XPATH, '//input[@id="country"]')                     # Находим поле "country"
    input4.send_keys("Russia")                                                            # Вводим в поле "country" страну "Russia"
    button = browser.find_element(By.XPATH, '//form/div/button[text()="Submit"]')         # Находим кнопку "Submit"
    button.click()                                                                        # Кликаем по кнопке "Submit"

finally:
    time.sleep(30)                                                       # Устанавливаем задержку 30 сек перед закрытием браузера
    browser.quit()                                                       # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!