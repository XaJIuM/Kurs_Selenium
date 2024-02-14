import time                                                              # Скачиваем библиотеку для работы со временем и датами
import math                                                              # Скачиваем математическую библиотеку
from selenium import webdriver                                           # Используем для работы с Selenium
from selenium.webdriver.common.by import By                              # Используем для работы с элементами "By"


# Переменные
link = "http://suninjuly.github.io/get_attribute.html"

try:                                                             
    browser = webdriver.Chrome()                                               # Открываем браузер
    browser.get(link)                                                          # Переходим по ссылке(В данном случае по переменной)

    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))                 # Выполняем математическое выражение
    x_element = browser.find_element(By.ID, "treasure")                        # Находим поле элемент на странице
    x_valuex = x_element.get_attribute("valuex")                               # Получаем атрибут "591" который находится в "valuex" и записываем его в переменную "x_valuex"
    x = x_valuex                                                               # Извлекаем текстовое содержимое найденного элемента и сохраняем его в переменной "x"
    print(x)                                                                   # Выводим значение в переменной "x" на экран
    y = calc(x)                                                                # Принимаем аргумент "x" и выполняем вычисления над ним, результат которых сохраняем в переменной "y"
    print(y)                                                                   # Выводим значение в переменной "y" на экран
    input1 = browser.find_element(By.ID, "answer")                             # Находим поле для ввода ответа
    input1.send_keys(y)                                                        # Вводим в поле для ввода ответа, ответ записанный в переменной "y"
    input2 = browser.find_element(By.ID, "robotCheckbox")                      # Находим Checkbox под названием "I'm the robot"
    input2.click()                                                             # Вводим по Checkbox с названием "I'm the robot"
    input3 = browser.find_element(By.ID, "robotsRule")                         # Находим радиокнопку "Robots rule"
    input3.click()                                                             # Кликаем по радиокнопке "Robots rule"
    time.sleep(2)                                                              # Устанавливаем задержку 2 сек
    
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-default"]')             # Находим кнопку "Submit"
    button.click()                                                                            # Кликаем по кнопке "Submit"

finally:
    time.sleep(10)                                                             # Устанавливаем задержку 10 сек перед закрытием браузера
    browser.quit()                                                             # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!