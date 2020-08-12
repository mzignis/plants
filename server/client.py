import paho.mqtt.client as mqtt
import time


class MyClient(mqtt.Client):

    def __init__(self, client_id):
        super().__init__(client_id)

        self.adc_value = None
        self.ADC_MAX = 1024

        self.on_message = self.on_msg
        self.connect('192.168.0.101', 1883, 60)

    def on_msg(self, client, userdata, message):
        self.adc_value = ((self.ADC_MAX - float(message.payload.decode("utf-8")))/ self.ADC_MAX ) * 100


    def read_humidity(self):
        self.publish('request', 'adc')
        self.subscribe('humi-value')

        self.loop_start()

        while self.adc_value is None:
            pass

        self.loop_stop()
        self.disconnect()

        return self.adc_value

    def start_watering(self):
        self.connect('192.168.0.101', 1883, 60)
        self.publish('request', 'watering-start')
        self.disconnect()

    def stop_watering(self):
        self.connect('192.168.0.101', 1883, 60)
        self.publish('request', 'watering-stop')
        self.disconnect()
