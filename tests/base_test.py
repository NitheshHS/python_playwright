import configparser
import os
import unittest
from configparser import ConfigParser

import pytest
from playwright.sync_api import sync_playwright, Page

from utilities.configs import Configs


class BaseTest:

    @pytest.fixture(scope="function")
    def setup_browser(self):
        with sync_playwright() as playwright:
            self.configs = Configs('data/config.ini')
            self.browser=playwright.chromium.launch(headless=self.configs.get_browser_headless)
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
            self.page.goto(self.configs.get_url)
            yield self.page, self.context, self.browser
            self.page.close()
            self.context.close()
            self.browser.close()



