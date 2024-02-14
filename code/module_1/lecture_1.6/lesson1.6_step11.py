import time                                                              # Скачиваем библиотеку для работы со временем и датами
from selenium import webdriver                                           # Используем для работы с Selenium
from selenium.webdriver.common.by import By                              # Используем для работы с элементами "By"
 

# Переменные
link = "http://suninjuly.github.io/registration2.html"

try:                                                             
    browser = webdriver.Chrome()                                                          # Открываем браузер
    browser.get(link)                                                                     # Переходим по ссылке(В данном случае по переменной)

    input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[@class="form-group first_class"]/input[@required]')       # Находим поле "first_name"
    input1.send_keys("Ivan")                                                                                                           # Вводим в поле "first_name" имя "Ivan"
    input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[@class="form-group second_class"]/input[@required]')      # Находим поле "last_name"
    input2.send_keys("Petrov")                                                                                                         # Вводим в поле "last_name" фамилию "Petrov"
    input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[@class="form-group third_class"]/input[@required]')       # Находим поле "Email"
    input3.send_keys("ivan.petrov@mail.ru")                                                                                            # Вводим в поле "Email" домен "ivan.petrov@mail.ru"
    input4 = browser.find_element(By.XPATH, '//div[@class="second_block"]/div[@class="form-group first_class"]/input')                 # Находим поле "Phone"
    input4.send_keys("+79059485746")                                                                                                   # Вводим в поле "Phone" номер телефона "+79059485746"
    input5 = browser.find_element(By.XPATH, '//div[@class="second_block"]/div[@class="form-group second_class"]/input')                # Находим поле "Address"
    input5.send_keys("г. Владимир, ул. Кузнецова, дом 5, квартира 7")                                                                  # Вводим в поле "Address" адрес "г. Владимир, ул. Кузнецова, дом 5, квартира 7"
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-default"]')                  # Находим кнопку "Submit"
    button.click()                                                                                 # Кликаем по кнопке "Submit"
    
    time.sleep(1)                                                                         # Устанавливаем задержку 1 сек, чтобы проверить что смогли зарегистрироваться 
    
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")                            # Находим элемент с текстом
    welcome_text = welcome_text_elt.text                                                  # Записываем в переменную welcome_text текст из элемента welcome_text_elt

    assert "Congratulations! You have successfully registered!" == welcome_text           # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

finally:
    time.sleep(10)                                                       # Устанавливаем задержку 10 сек перед закрытием браузера
    browser.quit()                                                       # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
# P.S Если в конструкции 'try' произойдет ошибка, то конструкция 'finallly' выполнится в любом случае!