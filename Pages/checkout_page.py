from utilities.ui_interactions import UiInteractions

class Checkout:

    def __init__(self):
        self.input_first_name = "[data-test='firstName']"
        self.input_last_name = "[data-test='lastName']"
        self.input_postal_code = "[data-test='postalCode']"
        self.btn_continue = "CONTINUE"
        self.btn_cancel = "CANCEL"
        self.btn_finish = "FINISH"
        self.text_confirm_order = ".complete-header"

class CheckoutPage(UiInteractions):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.checkout = Checkout()

    def enter_checkout_details(self, first_name, last_name, postal_code):
        self.fill_text(self.checkout.input_first_name, first_name)
        self.fill_text(self.checkout.input_last_name, last_name)
        self.fill_text(self.checkout.input_postal_code, postal_code)
        self.click_on_continue()

    def click_on_continue(self):
        assert 'checkout-step-one.html' in self.get_current_page_url
        self.get_by_text(self.checkout.btn_continue).click()

    def click_on_cancel(self):
        self.get_by_text(self.checkout.btn_cancel).click()

    def click_on_finish(self):
        assert 'checkout-step-two.html' in self.get_current_page_url
        self.get_by_text(self.checkout.btn_finish).click()

    def verify_order_confirm(self):
        assert 'checkout-complete.html' in self.get_current_page_url
        assert self.get_element_text(self.checkout.text_confirm_order) == 'THANK YOU FOR YOUR ORDER'



