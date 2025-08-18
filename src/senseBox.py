import requests

class SenseBox:
    """Class representing a senseBox"""

    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.name = "N/A"
        self.location = "N/A"
        self.version = "N/A"
        self.temperature = "N/A"
        self.last_mesurement = "N/A"

    def __str__(self):
        ret = f"""
          Sensebox {self.name} :
          - unique_id = {self.unique_id}
          - location = {self.location}
          - version = {self.version}
          - temperature = {self.temperature}
          - last Mesurement = {self.last_mesurement}
        """
        return ret

    def gather_data(self):
        """Method to gather sensorBox data using an http GET request to opensensmap"""

        url = f"https://api.opensensemap.org/boxes/{self.unique_id}?format=json"
        print(f"{self.unique_id} | Gathering data from opensense.com")

        data_collected = False
        tries = 0

        while not data_collected or tries>3:
            tries += 1
            try:
                data = requests.get(url, timeout=10).json()
                
                self.name = data["name"]
                self.location = data["currentLocation"]["coordinates"]
                for sensor in data["sensors"]:
                    if sensor["title"] == "Temperatur":
                        self.temperature = sensor["lastMeasurement"]["value"]
                        self.last_mesurement = sensor["lastMeasurement"]["createdAt"]

                data_collected = True
                print("Data successfully collected")
            except requests.exceptions.ReadTimeout:
                print(f"Request to {self.unique_id} has timed out, retrying...")
        
        if not data_collected:
            print(f"Request to {self.unique_id} has timed out too many times, No data gathered")
        
