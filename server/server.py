import sqlite3
import pandas as pd
import datetime
import time
import paho.mqtt.client as mqtt


TABLE_NAME = 'humi0'
TOPIC = 'humi-value'
BROKER_IP = '192.168.0.101'


def server_main_loop():

    def on_connect(client, userdata, flags, rc):
        print('Connected with result code {0}'.format(rc))
        client.subscribe(TOPIC)


    def on_message(client, userdata, msg):
        print('receive: {}'.format(msg.payload.decode("utf-8")))
        conn = sqlite3.connect('humi.db')
        cursor = conn.cursor()
        adc_value = msg.payload.decode("utf-8")
        dt = datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')
        query = "insert into {} values ('{}', '{}')".format(TABLE_NAME, dt, adc_value)
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
        except Exception as exception:
            print(type(exception))
            print(exception)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_IP, 1883, 60)

    client.loop_start()
    while True:
        try:
            client.publish('request', 'adc')
            time.sleep(10)
        except:
            client.loop_stop()


if __name__ == '__main__':
    server_main_loop()
