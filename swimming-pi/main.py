import logging
import logging.handlers
from sensors import ds18b20


def main():
    logging.basicConfig(level=logging.DEBUG)
    root = logging.getLogger()
    h = logging.handlers.RotatingFileHandler('swimming-pi.log', 'a', (1024 * 1024 * 2), 10)
    f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
    h.setFormatter(f)
    root.addHandler(h)
    logging.info('Started')

    sensor = ds18b20()
    temp = sensor.read()
    print(temp)

    logging.info('Finished')

if __name__ == '__main__':
    main()