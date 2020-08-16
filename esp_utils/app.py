from umqtt.simple import MQTTClient
import machine
import time
from constants import *
import bme
import json

def run_app():
    # -------- mqtt client --------
    client = MQTTClient(CLIENT_ID, SERVER_IP)

    # -------- adc sensors --------
    light_sensor = machine.ADC(machine.Pin(LIGHT_SENSOR_PIN))
    rain_sensor = machine.ADC(machine.Pin(RAIN_SENSOR_PIN))
    soil_sensor_1 = machine.ADC(machine.Pin(SOIL_SENSOR_1_PIN))
    soil_sensor_2 = machine.ADC(machine.Pin(SOIL_SENSOR_2_PIN))

    # -------- weather sensor --------
    bme280 = bme.BME280(i2c=machine.I2C(scl=machine.Pin(BME280_SCL_PIN), sda=machine.Pin(BME280_SDA_PIN)))

    # -------- output pins --------
    pump = machine.Pin(PUMP_PIN, machine.Pin.OUT)
    pump.value(0)

    # -------- measurement results container --------
    results = dict(light_sensor=None, rain_sensor=None, soil_sensor_1=None, soil_sensor_2=None,
                   temperature=None, pressure=None, humidity=None)


    def on_message(topic, msg):
        msg = msg.decode()
        print(msg)

        # if msg == 'adc':
        #     adc_value = adc.read()
        #     client.publish(TOPIC, str(adc_value))
        #     time.sleep(0.05)
        #
        # elif msg.split('-')[0] == 'watering':
        #     action = msg.split('-')[1]
        #     if action == 'start':
        #         print('start')
        #         engine.value(1)
        #     elif action == 'stop':
        #         print('stop')
        #         engine.value(0)
        #     else:
        #         pass
        #
        # else:
        #     pass


    client.set_callback(on_message)
    client.connect()
    client.subscribe(SUBSCRIPTION)


    while True:
        # -------- checking for msg --------
        client.check_msg()

        # -------- reading values --------
        print('reading values')
        temperature, pressure, humidity = bme280.read_compensated_data()

        results['light_sensor'] = light_sensor.read()
        results['rain_sensor'] = rain_sensor.read()
        results['soil_sensor_1'] = soil_sensor_1.read()
        results['soil_sensor_2'] = soil_sensor_2.read()
        results['temperature'] = temperature
        results['pressure'] = pressure
        results['humidity'] =  humidity

        print(results)
        client.publish('measurement', json.dumps(results))
        time.sleep(30)


if __name__ == '__main__':
    pass
