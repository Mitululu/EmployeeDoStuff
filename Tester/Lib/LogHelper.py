__author__ = 'jordi.terns'

import os
import sys
import logging
import datetime

class LogHelper(object):

    def __init__(self, OutDirectory, LoggerId):
        try:
            if not os.path.exists(OutDirectory):
                os.makedirs(OutDirectory)

            DateAux = (datetime.date.today()).strftime("%Y-%m-%d")
            CurrentTime = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
            LogFile = OutDirectory + "/" + DateAux + "-" + LoggerId + ".log"

            self.logger = logging.getLogger(LoggerId)
            hdlr = logging.FileHandler(LogFile)
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            hdlr.setFormatter(formatter)
            self.logger.addHandler(hdlr)
            self.logger.setLevel(logging.INFO)

            self.logger.info("---------------------------------------------------------------------------")
            self.logger.info("|" + '{:^73}'.format(CurrentTime) + "|")
            self.logger.info("---------------------------------------------------------------------------")
            self.logger.info("")

        except Exception as e:
            print("Error: LogHelper >> Constructor > " + str(e))
            sys.exit(99)


    def Error(self, msg, display=False):
        try:
            self.logger.error(msg)
            if display: print(self.__getTimeStamp() + " > " + msg)

        except Exception as e:
            print("LogHelper >> Error > " + str(e))


    def Info(self, msg, display=False):
        try:
            self.logger.info(msg)
            if display: print(self.__getTimeStamp() + " > " + msg)

        except Exception as e:
            print("LogHelper >> Info > " + str(e))


    def __getTimeStamp(self):
        try:
            return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        except Exception as e:
            print("LogHelper >> __getTimeStamp > " + str(e))