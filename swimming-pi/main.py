import logging
import logging.handlers
import time
from time import gmtime, strftime
from sensors import ds18b20
from displays import i2c1602


def main():
    logging.basicConfig(level=logging.DEBUG)
    root = logging.getLogger()
    # application log
    h = logging.handlers.RotatingFileHandler('swimming-pi.log', 'a', (1024 * 1024 * 2), 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)
    logging.info('Started')

    sensor = ds18b20()
    display = i2c1602()

    max_temp = -2000.0
    min_temp = 2000.0

    while True:

        temp = sensor.read()
        max_temp = max(max_temp,temp)
        min_temp = min(min_temp,temp)
        curr_time = strftime("%H:%M:%S", gmtime())

        with open('temperature_log.txt', 'a') as the_file:
            line = '%s  %.2f\n' % (curr_time, temp)
            the_file.write(line)

        currentTemp = "Temp:{: 10.2f}c".format(temp)
        display.lcd_stringL1(currentTemp)
        display.lcd_stringL2(curr_time)

        time.sleep(1)
  
        temp = sensor.read()
        max_temp = max(max_temp,temp)
        min_temp = min(min_temp,temp)
        curr_time = strftime("%H:%M:%S", gmtime())

        with open('temperature_log.txt', 'a') as the_file:
            line = '%s  %.2f\n' % (curr_time, temp)
            the_file.write(line)

        minMax = "L:{: 5.1f}  H:{: 5.1f}".format(min_temp, max_temp)
        display.lcd_stringL1(minMax)
        display.lcd_stringL2(curr_time)

        time.sleep(1)

    logging.info('Finished')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass