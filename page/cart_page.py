from utilities.ui_interactions import UiInteractions

class Cart:
    def __init__(self):
        self.continue_shopping = "Continue Shopping"
        self.btn_checkout = ".btn_action.checkout_button"
        self.btn_remove = "REMOVE"
        self.badge_shopping_cart=".shopping_cart_badge"

class CartPage(UiInteractions):

    def __init__(self, page):
        UiInteractions.__init__(self, page)
        self.cart = Cart()
        self.page = page

    def click_on_continue_shopping(self):
        self.get_by_text(self.cart.continue_shopping).click()
        assert self.get_page_title == 'Swag Labs'

    def click_on_remove(self):
        assert int(self.get_element_text(self.cart.badge_shopping_cart)) > 0
        self.find_element(self.cart.btn_remove).click()

    def click_on_checkout(self):
        assert 'cart.html' in self.get_current_page_url
        self.find_element(self.cart.btn_checkout).click()
