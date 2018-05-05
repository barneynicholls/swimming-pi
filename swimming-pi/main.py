import os
import sys
import traceback
import logging
import logging.handlers
import time
from time import gmtime, strftime
from sensors import ds18b20, gyneo6mv2, gpsReport
from displays import ssd1306


def main():
    logging.basicConfig(level=logging.ERROR)
    root = logging.getLogger()
    # application log
    h = logging.handlers.RotatingFileHandler('swimming-pi.log', 'a', (1024 * 1024 * 2), 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)
    logging.info('Started')

    sensor = ds18b20()
    gps_sensor = gyneo6mv2()
    display = ssd1306()

    while True:

        temp = 0
        report = gpsReport.gpsReport()

        try:
            temp = sensor.read()
        except:
            logging.error('ERROR temp read')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            logging.error(lines)
            pass

        try:
            report = gps_sensor.read()
        except:
            logging.error('ERROR gps read')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            logging.error(lines)
            pass

        try:
            display.update(
                "Swimming PI :)",
                strftime("%H:%M:%S", gmtime()),
                "TEMP:{: 4.2f}c".format(temp),
                "LT:{:3.3f}".format(report.lat),
                "LN:{:3.3f}".format(report.lon),
                "ALT:{:3.1f}m".format(report.alt),
                "SPD:{:3.1f}kmh".format(report.speed)
                )
        except:
            logging.error('ERROR display update')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            logging.error(lines)
            pass

        try:
            if report.lat != 0:
                with open('sensor_log.txt', 'a') as the_file:
                    line = '%s,%s,%s,%s,%s,%s\n' % (report.time, temp, report.lat, report.lon, report.speed, report.alt)
                    the_file.write(line)
        except:
            logging.error('ERROR log write')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            logging.error(lines)
            pass

    logging.info('Finished')

if __name__ == '__main__':
    try:
        main()
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()