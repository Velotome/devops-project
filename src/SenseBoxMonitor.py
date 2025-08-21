import numpy as np


class SenseBoxMonitor:

    def __init__(self):
        self.average_temperature = "N/A"
        self.status = "N/A"

    def run(self, l_sense_box):
        for sense_box in l_sense_box:
            sense_box.run()
        self.compute_average_temp(l_sense_box)
        self.set_status()

    def compute_average_temp(self, l_sense_box: list):
        self.average_temperature = np.mean(
            [sense_box.temperature for sense_box in l_sense_box]
        )

    def set_status(self):
        if self.average_temperature < 10:
            self.status = "Too Cold"
        elif self.average_temperature > 37:
            self.status = "Too Hot"
        else:
            self.status = "Good"
