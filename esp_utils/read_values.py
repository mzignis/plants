import machine
import time


def read_values():
    adc = machine.ADC(0)
    pin = machine.Pin(5, machine.Pin.OUT)

    for i in range(100):
        adc_value = adc.read()
        print(adc_value)

        if adc_value >= 600:
            pin.value(1)
        else:
            pin.value(0)

        time.sleep(1)


if __name__ == '__main__':
    pass
