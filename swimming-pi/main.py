import logging
import logging.handlers
import time
from time import gmtime, strftime
from sensors import ds18b20, gyneo6mv2
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
    gps = gyneo6mv2()
    display = i2c1602()

    max_temp = -2000.0
    min_temp = 2000.0

    while True:

        temp = sensor.read()
        lat, lon = gps.read()

        display.lcd_line1("Lat:{: 5.1f}  Lon:{: 5.1f}".format(lat,lon))

        max_temp = max(max_temp,temp)
        min_temp = min(min_temp,temp)

        with open('temperature_log.txt', 'a') as the_file:
            line = '%s  %.2f\n' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), temp)
            the_file.write(line)

        currentTemp = "Temp:{: 10.2f}c".format(temp)
        display.lcd_line1(currentTemp)
        display.lcd_line2(strftime("%H:%M:%S", gmtime()))

        time.sleep(0.5)

        minMax = "L:{: 5.1f}  H:{: 5.1f}".format(min_temp, max_temp)
        display.lcd_line1(minMax)
        display.lcd_line2(strftime("%H:%M:%S", gmtime()))

        time.sleep(0.5)

    logging.info('Finished')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass