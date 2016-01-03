try:
    import ConfigParser as configparser
except ImportError:
    import configparser
import os


class ConstantsManager():
    def __init__(self, config_file_name='constants.ini', constants_name='ENV'):
        self.config = configparser.RawConfigParser()
        self.config.optionxform = str
        self.config.read(config_file_name)
        self.environment = 'DEFAULT'
        if constants_name in os.environ:
            self.environment = os.environ[constants_name]

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        return self.config.get(self.environment, key)
