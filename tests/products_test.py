import pytest

from Pages.ProductsPage import ProductsPage
from Pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestProducts(BaseTest):

    def test_add_to_cart_remove_button(self, setup_browser):
        page, _, _=setup_browser
        login = LoginPage(page)
        login.login(self.configs.get_username, self.configs.get_password, "Swag Labs")
        product = ProductsPage(page)
        product.click_on_add_to_cart(2)
        product.click_on_remove_cart()

if __name__ == '__main__':
    pytest.main()