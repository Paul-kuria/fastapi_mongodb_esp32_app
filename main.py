from fastapi import FastAPI
from routes.route_sensor import sensor_route
from routes.route_esp32 import esp_route

app = FastAPI()

app.include_router(sensor_route)
app.include_router(esp_route)

@app.get("/")
async def homepage():
    return {"Project": "IoT mongodb API"}
