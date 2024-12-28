import pytest

from page.product_page import ProductsPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
from page.login_page import LoginPage
from tests.base_test import BaseTest


class TestCheckoutPage(BaseTest):

    def test_checkout_product(self, setup_browser):
        page, _, _ = setup_browser
        login_page = LoginPage(page)
        login_page.login(self.configs.get_username, self.configs.get_password, "Swag Labs")
        product_page = ProductsPage(page)
        product_page.click_on_add_to_cart(1)
        product_page.click_on_shopping_cart_icon()
        cart_page = CartPage(page)
        cart_page.click_on_checkout()
        checkout_page = CheckoutPage(page)
        checkout_page.enter_checkout_details("Nithesh", "Gowda", "10001")
        checkout_page.click_on_finish()
        checkout_page.verify_order_confirm()

if __name__ == '__main__':
    pytest.main()


