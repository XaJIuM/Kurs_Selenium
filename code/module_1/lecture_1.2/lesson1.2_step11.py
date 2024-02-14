import time                                                                  # Скачиваем библиотеку для работы со временем и датами
from selenium import webdriver                                               # Используем для работы с Selenium
from selenium.webdriver.common.by import By                                  # Используем для работы с элементами "By"

browser = webdriver.Chrome()                                                 # Открываем браузер

time.sleep(5)                                                                # Устанавливаем задержку 5 сек, чтобы мы успели увидеть, что происходит в браузере

driver.get("https://stepik.org/lesson/25969/step/12")                        # Переходим по ссылке(В данном случае по)
time.sleep(5)                                                                # Устанавливаем задержку 5 сек

textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")                 # Ищем поле по локатору и значению

textarea.send_keys("get()")                                                  # Напишем текст ответа в найденное поле
time.sleep(5)                                                                # Устанавливаем задержку 5 сек

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")   # Найдем кнопку, которая отправляет введенное решение

submit_button.click()                                                        # Скажем драйверу, что нужно нажать на кнопку для отправки решения
time.sleep(5)                                                                # Устанавливаем задержку 5 сек

browser.quit()                                                               # Закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла