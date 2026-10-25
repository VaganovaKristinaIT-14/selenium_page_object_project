import pytest
from pages.product_page import ProductPage


class TestAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = "Best book created by robot"
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        yield
        self.product = None

    @pytest.mark.add_to_basket
    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()