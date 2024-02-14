from selenium.webdriver.common.by import By                            # Используем для работы с элементами "By"
from selenium.webdriver.support.ui import WebDriverWait                # Используем для работы с явными ожиданиями
from selenium.webdriver.support import expected_conditions as EC       # Используем еще один инструмент для работы с явными ожиданиями
from selenium import webdriver                                         # Используем для работы с Selenium                     
import time                                                            # Скачиваем библиотеку для работы со временем и датами
import math                                                            # Скачиваем математическую библиотеку

# Переменные
link = "http://suninjuly.github.io/explicit_wait2.html"

try:     
    browser = webdriver.Chrome()                                                                                # Открываем браузер     
    browser.get(link)                                                                                           # Переходим по ссылке(В данном случае по переменной)                                                   
    summa = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))        # Говорим Selenium проверять в течение 12 секунд, пока не появится нужная нам сумма                                                                      
    button = browser.find_element(By.ID, "book").click()                                                        # Находим "Book" и кликаем по ней
    def calc(x):return str(math.log(abs(12*math.sin(int(x)))))                                                  # Выполняем математическое выражение
    x_element = browser.find_element(By.ID, "input_value").text                                                 # Находим поле элемент на странице
    x = x_element                                                                                               # Извлекаем текстовое содержимое найденного элемента и сохраняем его в переменной "x"
    print(x)                                                                                                    # Выводим значение в переменной "x" на экран
    y = calc(x)                                                                                                 # Принимаем аргумент "x" и выполняем вычисления над ним, результат которых сохраняем в переменной "y"
    print(y)                                                                                                    # Выводим значение в переменной "y" на экран
    input1 = browser.find_element(By.ID, "answer")                                                              # Находим поле для ввода ответа
    input1.send_keys(y)                                                                                         # Вводим в поле для ввода ответа, ответ записанный в переменной "y"

    button = browser.find_element(By.ID, 'solve')                                                               # Находим кнопку "Submit"
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)                                 # Передаем аргумент JavaScript и скроллим кнопку "Submit"
    button.click()                                                                                              # Кликаем по кнопке "Submit"

finally:
    time.sleep(10)                                                       # Устанавливаем задержку 30 сек перед закрытием браузера
    browser.quit()                                                       # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!