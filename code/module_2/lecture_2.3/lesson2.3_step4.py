import time                                                              # Скачиваем библиотеку для работы со временем и датами
import math                                                              # Скачиваем математическую библиотеку
from selenium import webdriver                                           # Используем для работы с Selenium
from selenium.webdriver.common.by import By                              # Используем для работы с элементами "By"
 

# Переменные
link = "http://suninjuly.github.io/alert_accept.html"

try:                                                             
    browser = webdriver.Chrome()                                                 # Открываем браузер
    browser.get(link)                                                            # Переходим по ссылке(В данном случае по переменной)

    button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()             # Находим кнопку "Submit" и кликаем на нее
    confirm = browser.switch_to.alert                                                                 # Находим кнопку "ОК" в модальном окне
    confirm.accept()                                                                                  # Нажимаем кнопку "ОК" в модальном окне
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))                                        # Выполняем математическое выражение
    x_element = browser.find_element(By.ID, "input_value").text                                       # Находим поле элемент на странице
    x = x_element                                                                                     # Извлекаем текстовое содержимое найденного элемента и сохраняем его в переменной "x"
    print(x)                                                                                          # Выводим значение в переменной "x" на экран
    y = calc(x)                                                                                       # Принимаем аргумент "x" и выполняем вычисления над ним, результат которых сохраняем в переменной "y"
    print(y)                                                                                          # Выводим значение в переменной "y" на экран
    input1 = browser.find_element(By.ID, "answer")                                                    # Находим поле для ввода ответа
    input1.send_keys(y)                                                                               # Вводим в поле для ввода ответа, ответ записанный в переменной "y"
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()             # Находим кнопку "Submit" и кликаем по ней
      
finally:
    time.sleep(10)                                                       # Устанавливаем задержку 30 сек перед закрытием браузера
    browser.quit()                                                       # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!