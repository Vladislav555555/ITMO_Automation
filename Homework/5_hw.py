'''from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

user_name= driver.find_element(By. CSS_SELECTOR,'#user-name' )
password = driver.find_element(By. CSS_SELECTOR,'#password' )
login_button = driver.find_element(By. CSS_SELECTOR,'#login-button' )


if user_name and password and login_button is None:
    print("Поле не найдено!")
else:
    print("Поле успешно найдено!")
'''

# Разбирался с try и except. Без них при отсутствии элемента код ломается

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

try:
    user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if user_name and password and login_button:
        print("Поле успешно найдено!")

except NoSuchElementException:
    print("Поле не найдено!")


