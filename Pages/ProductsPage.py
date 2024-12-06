from playwright.sync_api import Page

from utilities.ui_interactions import UiInteractions


class Products:
    def __init__(self):
        self.add_to_cart = "ADD TO CART"
        self.remove_cart = "REMOVE CART"
        self.shopping_cart_badge = ".shopping_cart_badge"

class ProductsPage(UiInteractions):
    def __init__(self, page: Page):
        super().__init__(page)
        self._products = Products()
        self._page = page

    def click_on_add_to_cart(self, add_to_cart_count):
        add_to_cart_btns=self.get_by_text(self._products.add_to_cart).count()
        if add_to_cart_btns > 0:
            for i in range(add_to_cart_count):
                self.get_by_text(self._products.add_to_cart).nth(i).click()
            assert self.get_element_text(self._products.shopping_cart_badge) == str(add_to_cart_count), \
                f"expected add to cart count {add_to_cart_count}, but got {self.get_element_text(self._products.shopping_cart_badge)}"
        else:
            assert False, f"expected add_to_cart button count>0, but found {add_to_cart_btns}"


    def click_on_remove_cart(self):
        remove_cart_btns=self.get_by_text(self._products.remove_cart).count()
        for i in range(remove_cart_btns):
            self.get_by_text(self._products.remove_cart).nth(i).click()






