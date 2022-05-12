import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket(browser):
    try:
        browser.get(link)
        time.sleep(5)
        button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    finally:
        assert button, "Cелектор кнопки не найден" # assert True/False, if False -> 'message'