import logging
from datetime import datetime


def log(className):
    logger = logging.getLogger(className)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "{'time':'%(asctime)s', 'class name': '%(name)s','function name':'%(funcName)s','level': '%(levelname)s', 'message': '%(message)s'}","%Y-%m-%d %H:%M:%S"
    )
    date=datetime.today().strftime('%Y-%m-%d')

    file_handler = logging.FileHandler('sample-'+date+'.log')
    # file_handler = logging.FileHandler(date+'.log')
    file_handler.setFormatter(formatter)

    # stream_handler = logging.StreamHandler() #to see log on the console
    # stream_handler.setFormatter(formatter) #to see log on the console

    logger.addHandler(file_handler)
    # logger.addHandler(stream_handler) #to see log on the console
    return logger


class MyclassA:
    def method1(self):
        log(self.__class__.__name__).error("error from test class A")

# if multiple methods in a class then will be convinient
class MyclassB:
    def __init__(self):
        self.logger=log(self.__class__.__name__)
    def methodB1(self):
        self.logger.info("info message from test class B")
    def methodB2(self):
        self.logger.debug("debug message from test class B")
class MyclassC:
    def method3(self):
        log(self.__class__.__name__).warning("Warning from test class C")


A=MyclassA()
B=MyclassB()
C=MyclassC()
A.method1()
B.methodB1()
B.methodB2()
C.method3()

