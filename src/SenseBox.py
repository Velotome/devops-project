import requests
import numpy as np

class SenseBox:
    """Class representing a senseBox"""

    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.name = "N/A"
        self.location = "N/A"
        self.max_measurements = 20
        self.l_measurements = []
        self.temperature = "N/A"
        self.last_update = "N/A"

    def __str__(self):
        ret = f"""
          Sensebox {self.name} :
          - unique_id = {self.unique_id}
          - location = {self.location}
          - number of measurements = {len(self.l_measurements)}
          - last measurements = {self.l_measurements[len(self.l_measurements)-1]}"""
        return ret

    def run(self):
        """Run this SenseBox"""
        self.gather_data()

    def gather_data(self):
        """Method to gather sensorBox data using an http GET request to opensensemap"""

        print(f"{self.unique_id} | Gathering data from opensense.com ... ", end="", flush=True)
        url = f"https://api.opensensemap.org/boxes/{self.unique_id}?format=json"
        data_collected = False
        tries = 0

        while not data_collected or tries>3:
            tries += 1
            try:
                data = requests.get(url, timeout=30).json()
                
                self.name = data["name"]
                self.location = data["currentLocation"]["coordinates"]
                for sensor in data["sensors"]:
                    if sensor["title"] == "Temperatur":
                        if len(self.l_measurements) >= self.max_measurements:
                            self.l_measurements.pop(0)
                        
                        self.l_measurements.append({
                            "timestamp": sensor["lastMeasurement"]["createdAt"],
                            "temperature": float(sensor["lastMeasurement"]["value"])
                            })
                        
                        self.last_update = sensor["lastMeasurement"]["createdAt"]
                        self.temperature = float(sensor["lastMeasurement"]["value"])


                data_collected = True
                print("Data successfully collected")
            except requests.exceptions.ReadTimeout:
                print("Request has timed out, retrying...")
            except requests.exceptions.JSONDecodeError:
                print("Decoding failed, retrying...")
        
        if not data_collected:
            print("Request has timed out too many times, No data gathered")