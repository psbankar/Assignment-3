import paho.mqtt.client as mqtt

# import paho.mqtt.publish as publish

import requests
import random
import time

from virtual_sensor import VirtualSensor

# Thingspeak MQTT broker details
broker = "mqtt3.thingspeak.com"
port = 1883
username = "ATEwHzwNLxI1ODU7AgINLjw"
password = "SEsVHfFZjbjFY+umKUUX5bi3"
channel_id = "2488601"


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=username
)


client.username_pw_set(username, password)

client.connect(broker, port, 60)

client.loop_start()

sensor = VirtualSensor()
while True:
    sensor.generate_sensor_values()

    publish_topic = "channels/{}/publish/fields/field1".format(channel_id)
    payload = f"{sensor.get_temperature()}&field2={sensor.get_humidity()}&field3={sensor.get_co2()}"
    client.publish(publish_topic, payload)
    print(
        f"Sensor values: Temperature: {sensor.get_temperature()}, Humidity: {sensor.get_humidity()}, CO2: {sensor.get_co2()}"
    )

    time.sleep(10)
