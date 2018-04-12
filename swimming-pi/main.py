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
    gps_sensor = gyneo6mv2()
    display = i2c1602()

    while True:

        temp = sensor.read()
        lat, lon, speed, alt, curr_time = gps_sensor.read()

        #display.lcd_line1("POS:{: 5.2f}, {: 5.2f}".format(lat,lon))
        #display.lcd_line1("SWIMMING-PI")
        #display.lcd_line2("{:}{: 7.2f}c".format(strftime("%H:%M:%S", curr_time) , temp))

        with open('sensor_log.txt', 'a') as the_file:
            line = '%s,%s,%s,%s,%s,%s\n' % (curr_time, temp, lat, lon, speed, alt)
            # line = '%s,%.2f,%.5f,%.5f\n' % (strftime("%Y-%m-%d %H:%M:%S",curr_time), temp, lat, lon)
            the_file.write(line)

    logging.info('Finished')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass