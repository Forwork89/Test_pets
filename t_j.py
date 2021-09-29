import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytest.driver = webdriver.Chrome()
pytest.driver.get('http://petfriends1.herokuapp.com/login')
element = WebDriverWait(pytest.driver, 10).until(
    EC.presence_of_element_located((By.ID, "pass"))
)


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('vasya@mail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    pytest.driver.find_element_by_class_name("navbar-nav").click()
    pytest.driver.implicitly_wait(10)
    all_my_pets = pytest.driver.find_element_by_id("all_my_pets")
    if len(str(all_my_pets)) < 0:
        assert all_my_pets == 66
        print("Все питомцы присутствуют")
    elif all_my_pets != 66:
        print("Не все питомцы присутствуют")