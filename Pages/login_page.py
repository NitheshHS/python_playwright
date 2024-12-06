from utilities.ui_interactions import UiInteractions
from playwright.sync_api import Page, expect


class Login:
    def __init__(self):
        self.input_username = "[data-test=\"username\"]"
        self.input_password = "[data-test=\"password\"]"
        self.btn_login = "[id=\"login-button\"]"


class LoginPage(UiInteractions):

    def __init__(self, page:Page):
        UiInteractions.__init__(self, page)
        self._login = Login()
        self.page = page

    def login(self, username:str, password:str, expected_title) -> None:
        self.fill_text(self._login.input_username, username)
        self.fill_text(self._login.input_password, password)
        self.click_on(self._login.btn_login)
        expect(self.page).to_have_title(expected_title)

