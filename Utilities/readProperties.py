import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadconfigFile:
    @staticmethod
    def Read_username():
        Username=config.get('login data','username')
        return Username

    @staticmethod
    def Read_password():
        Password = config.get('login data', 'password')
        return Password