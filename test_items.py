import time
from selenium.webdriver.common.by import By

def test_item_page_contains_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button is not None, "Кнопка добавления в корзину не найдена"
    assert button.is_displayed(), "Кнопка добавления в корзину не видна на странице"
