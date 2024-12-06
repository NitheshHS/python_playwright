import configparser
import os.path


class Configs:
    def __init__(self, path):
        self._parser = configparser.ConfigParser()
        print(os.path.abspath(path))
        self._parser.read(os.path.abspath(path))
        self._url = self._parser['SWAG_LAB']['url']
        self._username = self._parser['SWAG_LAB']['username']
        self._password = self._parser['SWAG_LAB']['password']
        self._headless = self._parser.getboolean('BROWSER','headless', fallback=False)


    @property
    def get_browser_headless(self):
        return self._headless

    @property
    def get_url(self):
        return self._url

    @property
    def get_username(self):
        return self._username

    @property
    def get_password(self):
        return self._password




