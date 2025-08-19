from src.senseBox import SenseBox

class TestSenseBox:
    """This class regroups the testing function for the SenseBox class"""

    def test_average_temperature(self):
        """Test the function SenseBox.compute_average_temp()"""

        box = SenseBox("1")

        temps = ["2", "15", "20.5"]
        box.l_measurements.append({"timestamp" : "1","temperature": float(temps[0])})
        box.l_measurements.append({"timestamp" : "2","temperature": float(temps[1])})
        box.l_measurements.append({"timestamp" : "3","temperature": float(temps[2])})
        
        box.compute_average_temp()

        assert box.average_temp == 12.5, "value is not equal to 12.5 which is the average of 2, 15 and 20.5"