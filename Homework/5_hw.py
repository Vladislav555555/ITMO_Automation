

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


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def check_elements(driver, selectors):

    try:
        for selector in selectors:
            driver.find_element(By.CSS_SELECTOR, selector)
        return True
    except NoSuchElementException:
        return False

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

selectors = ['#user-name', '#password', '#login-button']

if check_elements(driver, selectors):
    print("Все поля успешно найдены!")
else:
    print("Не удалось найти одно из полей.")