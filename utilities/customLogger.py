import inspect
import logging
import os
import sys


class LogGen:


    @staticmethod
    def loggen(logLevel=logging.DEBUG):
        # set class/method name from where it is calling
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        console = logging.StreamHandler(sys.stdout)   # for console printing
        # file location and set the log level W or a
        fh = logging.FileHandler(".\\Logs\\automation.log",mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        console.setFormatter(formatter)   # for console printing
        logging.getLogger(logger_name).addHandler(console)  # for console printing
        # add formatter to console or file handler
        fh.setFormatter(formatter)
        # add console handle to logger
        logger.addHandler(fh)
        return logger

    # delete the .png filed from Screenshots folder before running the script
    @staticmethod
    def deletScreenshortFiles():
        screenshorts_Path = ".\\Screenshots"
        fileNames = os.listdir(screenshorts_Path)
        for fileName in fileNames:
            if os.path.exists(".\\Screenshots\\" + fileName):
                os.remove(".\\Screenshots\\" + fileName)

    @staticmethod
    def deletHTMScreenshortFiles():
        htmlscreenshorts_Path = ".\\Reports"
        fileNames1 = os.listdir(htmlscreenshorts_Path)
        for fileName in fileNames1:
            if os.path.exists(".\\Reports\\" + fileName) and fileName.__contains__('.png'):
                os.remove(".\\Reports\\" + fileName)