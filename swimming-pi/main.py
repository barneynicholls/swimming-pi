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

        with open('temperature_log.txt', 'a') as the_file:
            line = '%s  %.2f\n' % (strftime("%H:%M:%S", gmtime()), temp)
            the_file.write(line)

        currentTemp = "Temp: %.2fc" % temp
        currentTime = strftime("%H:%M:%S", gmtime()) 
        display.lcd_string(currentTemp,1)
        display.lcd_string(currentTime,2)

        time.sleep(1)
  
        temp = sensor.read()
        max_temp = max(max_temp,temp)
        min_temp = min(min_temp,temp)

        with open('temperature_log.txt', 'a') as the_file:
            line = '%s  %.2f\n' % (strftime("%H:%M:%S", gmtime()), temp)
            the_file.write(line)

        currentTemp = "Min: %.2f Max: %.2f" % (min_temp, max_temp)
        currentTime = strftime("%H:%M:%S", gmtime()) 
        display.lcd_string(currentTemp,1)
        display.lcd_string(currentTime,2)

        time.sleep(1)

    logging.info('Finished')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass