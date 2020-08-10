from umqtt.simple import MQTTClient
from m_utils import do_connect
import time
import machine


CLIENT_ID = 'humi0'
SERVER = '192.168.0.101'
TOPIC = 'humi0-value'

def send_humi_value():
    do_connect()
    client = MQTTClient(CLIENT_ID, SERVER)
    client.connect()
    adc = machine.ADC(0)
    pin = machine.Pin(5, machine.Pin.OUT)

    while True:
        humi0_value = adc.read()
        print(humi0_value)

        if humi0_value >= 600:
            pin.value(1)
        else:
            pin.value(0)

        client.publish(TOPIC, '{}'.format(humi0_value))

        time.sleep(30)

