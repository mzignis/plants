import sqlite3
# import pandas as pd
import datetime
import paho.mqtt.client as mqtt

TABLE_NAME = 'humi0'

conn = sqlite3.connect('../humi.db')
cursor = conn.cursor()


def on_connect(client, userdata, flags, rc):
    print('Connected with result code {0}'.format(rc))
    client.subscribe('humi0-value')


def on_message(client, userdata, msg):
    print('receive: {}'.format(msg.payload.decode("utf-8")))
    adc_value = msg.payload.decode("utf-8")
    dt = datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')
    query = "insert into {} values ('{}', '{}')".format(TABLE_NAME, dt, adc_value)
    cursor.execute(query)
    conn.commit()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('localhost', 1883, 60)

client.loop_forever()
conn.close()
