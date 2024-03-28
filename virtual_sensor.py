import random


class VirtualSensor:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.co2 = 0
        self.uid = random.randint(1, 1000)

    def generate_sensor_values(self):
        self.temperature = random.uniform(-50, 50)
        self.humidity = random.uniform(0, 100)
        self.co2 = random.uniform(300, 2000)

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_co2(self):
        return self.co2
