import os
import sys
import traceback
import glob
import time
import logging

class ds18b20(object):
    """reads temperature from ds18b20 sensor"""

    base_dir = '/sys/bus/w1/devices/'
    device_folder = ''
    device_file = device_folder + '/w1_slave'

    def __init__(self):
        try:
            os.system('modprobe w1-gpio')
            os.system('modprobe w1-therm')
            self.device_folder = glob.glob(self.base_dir + '28*')[0]
            logging.info("device_folder: %s",self.device_folder)
            self.device_file = self.device_folder + '/w1_slave'
            logging.info("device_file: %s",self.device_file)
        except:
            logging.warn("failed to initialise as expected. assuming in test mode")
            self.device_file ="sensors/ds18b20_sample_output.txt"

    def read_temp_raw(self):
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
        return temp_c

    def read(self):
        """returns the temperature in degrees centigrade as a float, returns -1000 on exception"""
        try:
            logging.info("reading temperature")
            temp = self.read_temp()
            logging.info("temperature %f", temp)
            return temp
        except:
            logging.warn("failed to read temperature")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            logging.warn(lines)
            return -1000