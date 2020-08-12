from umqtt.simple import MQTTClient
import machine
import time

CLIENT_ID = 'plants'
SERVER = '192.168.0.101'
SUBSCRIPTION = b'request'
TOPIC = b'humi-value'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()


adc = machine.ADC(0)
engine = machine.Pin(5, machine.Pin.OUT)
engine.value(0)


def on_message(topic, msg):
    msg = msg.decode()
    print(msg)

    if msg == 'adc':
        adc_value = adc.read()
        client.publish(TOPIC, str(adc_value))

    elif msg.split('-')[0] == 'watering':
        action = msg.split('-')[1]
        if action == 'start':
            print('start')
            engine.value(1)
        elif action == 'stop':
            print('stop')
            engine.value(0)
        else:
            pass

    else:
        pass


client.set_callback(on_message)
client.subscribe(SUBSCRIPTION)

while True:
    client.wait_msg()
