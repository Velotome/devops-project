from fastapi import FastAPI
from _version import __version__

from senseBox import SenseBox

print("Starting devops-project v", __version__, " ...", sep="")

app = FastAPI()

l_sense_boxes = [
    SenseBox("5eba5fbad46fb8001b799786"),
    SenseBox("5ade1acf223bd80019a1011c"),
    SenseBox("5c21ff8f919bf8001adf2488")
    ]

@app.get("/sensebox/{sensebox_id}/temperature")
async def read_temperature(sensebox_id: int):
    return l_sense_boxes[sensebox_id].average_temp

@app.get("/sensebox/{sensebox_id}/lastupdate")
async def read_lastUpdate(sensebox_id: int):
    return l_sense_boxes[sensebox_id].last_update