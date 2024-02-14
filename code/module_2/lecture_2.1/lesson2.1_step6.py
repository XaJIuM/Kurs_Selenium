import time                                                              # Скачиваем библиотеку для работы со временем и датами
from selenium import webdriver                                           # Используем для работы с Selenium
from selenium.webdriver.common.by import By                              # Используем для работы с элементами "By"


# Переменные
link = "http://suninjuly.github.io/math.html"

try:                                                             
    browser = webdriver.Chrome()                                                     # Открываем браузер
    browser.get(link)                                                                # Переходим по ссылке(В данном случае по переменной)

    #проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element(By.ID, "peopleRule")                         # Находим радиокнопку "People rule" и записываем ее в переменную "people_radio"
    people_checked = people_radio.get_attribute("checked")                           # Получаем атрибут "checked" и записываем его в переменную "people_checked"
    print("value of people radio: ", people_checked)                                 # Выводим значение атрибута "checked" элемента на экран                              
    assert people_checked is not None, "People radio is not selected by default"     # Проверяем что значение атрибута "checked" не равно None. Если значение None, то будет выведено сообщение "People radio is not selected by default", что указывает на то, что радиокнопка для "people" не выбрана по умолчанию.

    #проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element(By.ID, "robotsRule")                         # Находим радиокнопку "Robots rule" и записываем ее в переменную "robots_radio"
    robots_checked = robots_radio.get_attribute("checked")                           # Получаем атрибут "checked" и записываем его в переменную "robots_checked"
    print("value of robots_radio: ", robots_checked)                                 # Выводим значение атрибута "checked" элемента на экран
    assert robots_checked is None                                                    # Проверяем что значение атрибута "checked" равно None.

    #проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element(By.CSS_SELECTOR, '.btn')                            # Находим кнопку "Submit" и записываем ее в переменную "button"
    button_disabled = button.get_attribute("disabled")                               # Получаем атрибут "disables" и записываем его в переменную "button_disabled"
    print("value of button Submit: ", button_disabled)                               # Выводим значение атрибута "disables" элемента на экран
    assert button_disabled is None                                                   # Проверяем что значение атрибута "disables" равно None.   

    #проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)                                                                   # Устанавливаем задержку 10 сек перед проверкой
    button_disabled = button.get_attribute("disabled")                               # Получаем атрибут "disables" и записываем его в переменную "button_disabled"
    print("value of button Submit after 10sec: ", button_disabled)                   # Выводим значение атрибута "disables" элемента на экран
    assert button_disabled is not None                                               # Проверяем что значение атрибута "disables" НЕ равно None.                          

finally:
    time.sleep(10)                                                                   # Устанавливаем задержку 10 сек перед закрытием браузера
    browser.quit()                                                                   # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!