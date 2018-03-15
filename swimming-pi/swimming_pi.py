#from sensors import ds18b20
#sensor = ds18b20()
#temp = sensor.read()
#print(temp)

from displays import i2c1602

display = i2c1602()

display.lcd_string("hello",1)




