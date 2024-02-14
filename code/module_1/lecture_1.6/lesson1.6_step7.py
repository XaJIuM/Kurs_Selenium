import time                                                       # Скачиваем библиотеку для работы со временем и датами
from selenium import webdriver                                    # Используем для работы с Selenium
from selenium.webdriver.common.by import By                       # Используем для работы с элементами "By"

try:
    browser = webdriver.Chrome()                                  # Открываем браузер
    browser.get("http://suninjuly.github.io/huge_form.html")      # Переходим по ссылке
    elements = browser.find_elements(By.TAG_NAME, "input")        # Ищем полЯ по локатору с одинаковыми значениями 
    for element in elements:
        element.send_keys("Человейник")                           # Заполняем найденые поля

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")  # Находим кнопку "Submit"
    button.click()                                                # Кликаем по кнопке "Submit"

finally:
    time.sleep(30)                                                # Устанавливаем задержку 30 сек перед закрытием браузера
    browser.quit()                                                # Закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!