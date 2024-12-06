import logging


class UiLogger(object):
    def __init__(self):
        self.logger = logging.getLogger('UiInteractions')
        self.logger.setLevel(logging.DEBUG)
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.console_handler)

    @property
    def get_logger(self):
        return self.logger