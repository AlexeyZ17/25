# python -m pytest -v --driver Chrome --driver-path C:\Windows\chromedriver.exe

# настройка библиотек
import pytest
import time
from selenium import webdriver #подключение библиотеки
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# настройки работы веб-драйвера
driver = webdriver.Chrome()
driver.implicitly_wait(10)


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # Для визуального контроля
    time.sleep(3)

    yield pytest.driver

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('luckin.alexej@yandex.ru')
    # Вводим пароль
    pytest.driver.find_element(By.ID,'pass').send_keys('Lav123456')
    # Для визуального контроля
    time.sleep(3)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
    # Для визуального контроля
    time.sleep(3)
    # Нажимаем на кнопку мои питомцы
    pytest.driver.find_element(By.XPATH, '//a[contains(text(), "Мои питомцы")]').click()
    # Ожидание псевдодинамического элемента
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="navbar-brand header2"]')))
    all_my_pets = pytest.driver.find_element(By.CSS_SELECTOR, 'h2')
    all_my_pets_num = pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]')

    print(len('all_my_pets'))
    print('all_my_pets_num')


# Проверка неявных ожиданий:

# images = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-img-top')
# names = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-img-top')
# descriptions = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-img-top')
#
# def test_only_my_pets():
#
# wait = WebDriverWait(driver, 10)
#
# for i in range(len(names)):
#     assert images[i].get_attribute('src') != ''
#     assert names[i].text != ''
#     assert descriptions[i].text != ''
#     assert ', ' in descriptions[i]
#     parts = descriptions[i].text.split(", ")
#     assert len(parts[0]) > 0
#     assert len(parts[1]) > 0

    driver.quit()


    # # Находим локатор на профиль статистики и извлекаем текст:
    # all_my = pytest.driver.find_element(By.XPATH,'//div[@class=".col-sm-4 left"]').get_attribute("innerText")
    # # извлекаем текст до слова "Друзей"
    # find_pets = all_my[0:all_my.find("Друзей: 0")]
    # # извлекаем числа из текста find_pets
    # value1 = int("".join(filter(str.isdigit, find_pets)))
    # value2 = int(driver.find_element(By.XPATH, '').text.split()[2])

    # print('\nall_my_pets_number ->', value1, '||', value2)





# myDynamicElement = driver.find_element(By.XPATH, $x('//div[@class="app"]')