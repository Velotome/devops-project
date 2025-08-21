import numpy as np


class SenseBoxMonitor:

    def __init__(self):
        self.average_temperature = "N/A"

    def run(self, l_sense_box):
        for sense_box in l_sense_box:
            sense_box.run()
        self.compute_average_temp(l_sense_box)
        print(self.average_temperature)

    def compute_average_temp(self, l_sense_box: list):
        self.average_temperature = np.mean(
            [sense_box.temperature for sense_box in l_sense_box]
        )
