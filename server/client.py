import time
import paho.mqtt.client as paho



def on_message(client, userdata, message):
    print("received message = ", str(message.payload.decode("utf-8")))


client= paho.Client("client-001")
client.on_message = on_message


print("connecting to broker")
client.connect('localhost', 1883, 60)
client.subscribe('humi-value')

client.loop_start()

print("publishing")
client.publish("request", "adc")
time.sleep(1)


client.disconnect()
client.loop_stop()
