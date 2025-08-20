from fastapi import FastAPI
from _version import __version__

from SenseBox import SenseBox
from SenseBoxMonitor import SenseBoxMonitor

print("Starting devops-project v", __version__, " ...", sep="")

app = FastAPI()
monitor = SenseBoxMonitor()

l_sense_box = [
    SenseBox("5eba5fbad46fb8001b799786"),
    SenseBox("5ade1acf223bd80019a1011c"),
    SenseBox("5c21ff8f919bf8001adf2488")
    ]

monitor.run(l_sense_box)

@app.get("/temperature")
async def read_temperature():
    return monitor.average_temperature

@app.get("/version")
async def read_app_version():
    return __version__