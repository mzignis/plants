import paho.mqtt.client as mqtt



class MyClient(mqtt.Client):

    def __init__(self, client_id):
        super().__init__(client_id)

        self.adc_value = None

    def on_msg(self, client, userdata, message):
        self.adc_value = str(message.payload.decode("utf-8"))


    def main(self):
        self.on_message = self.on_msg
        self.connect('192.168.0.101', 1883, 60)
        self.publish('request', 'adc')
        self.subscribe('humi-value')

        self.loop_start()

        while self.adc_value is None:
            pass

        self.loop_stop()
        self.disconnect()

        return self.adc_value



client = MyClient('mac')
client.main()
