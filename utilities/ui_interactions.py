import os.path
from venv import logger
from xml.sax.xmlreader import Locator

from playwright.sync_api import Page

from utilities.ui_logger import UiLogger


class UiInteractions(object):

    def __init__(self, page: Page):
        self.page = page
        self.logger = UiLogger().get_logger

    def navigate(self, url: str):
        self.logger.info(f'Navigating to {url}')
        self.page.goto(url)

    def navigate_back(self):
        self.logger.info(f'Navigating back to {self.page.url}')
        self.page.go_back()

    def navigate_forward(self):
        self.logger.info(f'Navigating to {self.page.url}')
        self.page.go_forward()

    def find_element(self, selector: str):
        # self.logger.info(f'Finding element {selector}')
        try:
            self.page.wait_for_selector(selector)
            return self.page.locator(selector)
        except Exception as e:
            return e

    def click_on(self, selector: str):
        self.logger.info(f'Clicking element {selector}')
        self.find_element(selector).click()

    def double_click(self, selector: str):
        self.logger.info(f'Double-clicking element {selector}')
        self.find_element(selector).dblclick()

    def fill_text(self, selector: str, text: str):
        self.logger.info(f'Filling element {selector} with {text}')
        self.find_element(selector).clear()
        self.find_element(selector).fill(text)

    def select_option(self, selector: str, option: str=None, label:str = None):
        if option:
            self.logger.info(f'Selecting option {option} in element {selector}')
            self.find_element(selector).select_option(option)
        elif label:
            self.logger.info(f'Selecting label {label} in element {selector}')
            self.find_element(selector).select_option(label)
        elif isinstance(option, list):
            self.logger.info(f'Selecting option {option} in element {selector}')
            self.find_element(selector).select_option(*option)

    def press_key(self, selector: str, key: str):
        self.logger.info(f'Pressing key {key} in element {selector}')
        self.find_element(selector).press(key)

    def drag_and_drop(self, selector: str, target: str):
        self.logger.info(f'Dragging and dropping element {selector} to {target}')
        self.find_element(selector).drag_to(self.find_element(target))

    def get_by_text(self, text: str):
        self.logger.info(f'Getting element by text {text}')
        return self.page.get_by_text(text)

    def get_element_text(self, selector: str):
        return self.find_element(selector).inner_text()

    def is_visible(self, selector: str)-> bool:
        self.wait_for_element(selector)
        self.logger.info(f'Checking visibility of element {selector}')
        return self.page.is_visible(selector)

    def wait_for_element(self, selector: str, timeout: int=0)->None:
        self.logger.info(f'Waiting for element {selector}')
        self.page.wait_for_selector(selector, timeout=timeout)

    def screenshot(self, screenshot_name):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(current_dir, '..', 'screenshots')
        self.page.screenshot(path=f"{config_path}/{screenshot_name}.png")

    @property
    def get_page_title(self):
        self.logger.info(f'Getting page title')
        return self.page.title

    @property
    def get_current_page_url(self):
        self.logger.info(f'Getting page url')
        return self.page.url





