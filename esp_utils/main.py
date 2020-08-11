from umqtt.simple import MQTTClient


CLIENT_ID = 'plants'
SERVER = '192.168.0.101'
SUBSCRIPTION = b'request'
TOPIC = b'humi-value'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()


def on_message(topic, msg):
    print(topic, msg)
    client.publish(TOPIC, '1024')


client.set_callback(on_message)
client.subscribe(SUBSCRIPTION)


while True:
    client.wait_msg()

