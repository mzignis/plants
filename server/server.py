import sqlite3
import pandas as pd
import datetime
import time
import paho.mqtt.client as mqtt
import json


DB_NAME = 'plants.db'
TABLE_NAME = 'soil_humidity'
TOPIC = 'measurement'
BROKER_IP = '192.168.0.102'


def server_main_loop():

    def on_connect(client, userdata, flags, rc):
        print('Connected with result code {0}'.format(rc))
        client.subscribe(TOPIC)

    def on_message(client, userdata, msg):
        msg = msg.payload.decode("utf-8")
        msg = json.loads(msg)
        print('receive: {}'.format(msg))

        adc1 = msg['soil_sensor_1']
        adc2 = msg['soil_sensor_2']
        temperature = msg['temperature']
        pressure = msg['pressure']
        humidity = msg['humidity']
        rain = msg['rain_sensor']
        light = msg['light_sensor']

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # soil_humidity = '{:.2f} %'.format(((1024. - float(adc_value)) /  1024.) * 100)

        dt = datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')
        query1 = "insert into {}" \
                 "(plant_id, adc_value, air_temperature, air_pressure, air_humidity, rain, light, datetime) " \
                 "values " \
                 "('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(TABLE_NAME, 1, adc1, temperature, pressure,
                                                                           humidity, rain, light, dt)
        query2 = "insert into {}" \
                 "(plant_id, adc_value, air_temperature, air_pressure, air_humidity, rain, light, datetime) " \
                 "values " \
                 "('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(TABLE_NAME, 2, adc2, temperature, pressure,
                                                                           humidity, rain, light, dt)
        try:
            cursor.execute(query1)
            conn.commit()

            cursor.execute(query2)
            conn.commit()

            conn.close()
        except Exception as exception:
            print(type(exception))
            print(exception)


    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_IP, 1883, 60)

    client.loop_forever()
    # client.loop_start()
    # while True:
    #     try:
    #         client.publish('request', 'adc')
    #         time.sleep(10)
    #     except:
    #         client.loop_stop()


if __name__ == '__main__':
    server_main_loop()
