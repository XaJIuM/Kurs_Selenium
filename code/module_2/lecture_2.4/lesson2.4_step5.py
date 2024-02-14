import time                                                                  # Скачиваем библиотеку для работы со временем и датами
from selenium import webdriver                                               # Используем для работы с Selenium
from selenium.webdriver.common.by import By                                  # Используем для работы с элементами "By"

# Переменные
link = "http://suninjuly.github.io/wait1.html"

try:                                                             
    browser = webdriver.Chrome()                                       # Открываем браузер
    browser.implicitly_wait(5)                                         # Ожидание 5 сек для каждого шага
    browser.get(link)                                                  # Переходим по ссылке(В данном случае по переменной)                                                           
    button = browser.find_element(By.ID, 'verify').click()             # Находим кнопку "Verify" и кликаем на нее
    message = browser.find_element(By.ID, "verify_message")            # Находим появившийся текст и фиксируем в переменной "message"

    assert "successful" in message.text                                # Проверяем что в тексте переменной "message", присутствует слово "successful"

finally:
    time.sleep(10)                                                       # Устанавливаем задержку 30 сек перед закрытием браузера
    browser.quit()                                                       # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!