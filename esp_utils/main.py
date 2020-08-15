import machine
import time
import bme

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
bme280 = bme.BME280(i2c=i2c)
adc_pins = ['36', '39', '34', '35']
adcs = {x: machine.ADC(machine.Pin(int(x))) for x in adc_pins}


while True:
    for key, adc in adcs.items():
        print(key, adc.read())
        time.sleep(0.5)
    print(bme280.read_compensated_data())
    print()
    time.sleep(3)
