import requests
import numpy as np

from src._version import __version__
from src.SenseBox import SenseBox
from src.SenseBoxMonitor import SenseBoxMonitor

def collect_data(endpoint : str):
    """Tries to collect data from given endpoint"""

    data_collected = False
    tries = 0
    while not data_collected or tries>3:
        tries += 1
        try:
            data = requests.get("http://127.0.0.1:8000/" + endpoint, timeout=30).json()
            data_collected = True
            print("Data successfully collected")
        except requests.exceptions.ReadTimeout:
            print("Request has timed out, retrying...")
        except requests.exceptions.JSONDecodeError:
            print("Decoding failed, retrying...")
        
    if not data_collected:
        print("Request has timed out too many times, No data gathered")

    return data


class TestSenseBox:
    """This class regroups the testing function for the SenseBox class"""
    l_sense_box = [
            SenseBox("5eba5fbad46fb8001b799786"),
            SenseBox("5ade1acf223bd80019a1011c"),
            SenseBox("5c21ff8f919bf8001adf2488")
        ]
    monitor = SenseBoxMonitor()

    def test_endpoint_temperature(self):
        """This test ensure that the temperature returned by the endpoint is the same as the one calculated"""
        
        # Test
        self.monitor.run(self.l_sense_box)
        remote_temp = collect_data("temperature")
        assert np.around(self.monitor.average_temperature, decimals=0) == np.around(remote_temp, decimals=0)

    def test_endpoint_version(self):
        """This test ensure that the version returned by the endpoint is the same as the one of the software"""
        remote_version = collect_data("version")
        assert __version__ == remote_version