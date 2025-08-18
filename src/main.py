from fastapi import FastAPI
from _version import __version__

from senseBox import SenseBox


app = FastAPI()

print("Starting devops-project v", __version__, " ...", sep="")

senseBoxes = [
    SenseBox("5eba5fbad46fb8001b799786"),
    SenseBox("5ade1acf223bd80019a1011c"),
    SenseBox("5c21ff8f919bf8001adf2488")
]

for box in senseBoxes :
    box.gather_data()

print(str(senseBoxes[0]))
print(str(senseBoxes[1]))
print(str(senseBoxes[2]))

@app.get("/")
async def root():
    return {"message" : "Hello World"}