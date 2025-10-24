import os

class ConfigReader:
    @staticmethod
    def get_browser():
        return os.getenv('BROWSER', 'chrome')
    
    @staticmethod
    def get_headless():
        return os.getenv('HEADLESS', 'false').lower() == 'true'
    
    @staticmethod
    def get_base_url():
        return os.getenv('BASE_URL', 'https://practice.automationtesting.in/')