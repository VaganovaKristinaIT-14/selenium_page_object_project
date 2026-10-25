from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_basket_total_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text

    def should_be_success_message_with_product_name(self):
        message_name = self.get_success_message_product_name()
        product_name = self.get_product_name()
        assert message_name == product_name, \
            f"Имя товара в сообщении '{message_name}' не совпадает с '{product_name}'"

    def should_be_basket_total_with_correct_price(self):
        basket_total = self.get_basket_total_message()
        product_price = self.get_product_price()
        assert basket_total == product_price, \
            f"Стоимость корзины '{basket_total}' не совпадает с ценой товара '{product_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_BLOCK), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_BLOCK), \
            "Success message is not disappeared, but should be"