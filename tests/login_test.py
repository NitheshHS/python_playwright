import pytest

from Pages.login_page import LoginPage

from tests.base_test import BaseTest


class TestLoginPage(BaseTest):

    @pytest.mark.parametrize("username, password, expected",[
        ("standard_user", "secret_sauce", "Swag Labs"),
        ("locked_out_user", "secret_sauce", "Swag Labs"),
    ])
    def test_login_page(self, username, password, expected, setup_browser):
        page, _, _ =  setup_browser
        login_page = LoginPage(page)
        login_page.login(username, password, expected)

    def test_login(self, setup_browser):
        page, _, _ = setup_browser
        login_page = LoginPage(page)
        login_page.login(self.configs.get_username, self.configs.get_password, "Swag Labs")

    def test_stored_session(self, setup_browser):
        page, context, _ = setup_browser
        login_page = LoginPage(page)
        login_page.login(self.configs.get_username, self.configs.get_password, "Swag Labs")
        context.storage_state(path="../login_session.json")

    def test_use_stored_session(self, setup_browser):
        page, context, browser = setup_browser
        context = browser.new_context(storage_state="../login_session.json")
        page = context.new_page()
        print(f"Page title: {page.url}")

if __name__ == '__main__':
    pytest.main()
