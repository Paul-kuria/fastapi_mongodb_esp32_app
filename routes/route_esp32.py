from fastapi import APIRouter 
from datetime import datetime
from models.model_sensor import SensorData, SensorTest
from config.db import collection_name 

from schemas.schemas_sensor import sensorEntity, sensorsEntity, sensorData, sensorsList
from bson import ObjectId 

esp_route = APIRouter(prefix="/sensors", tags=["ESP32_testing"])



# POST Request Method
"""
sensor_reading: SensorReading automatically parses and validates the incoming JSON data. The attributes temperature_in_c, temperature_in_f, humidity, heat_index_in_c, and heat_index_in_f are directly accessible from the sensor_reading object because they are defined in the SensorReading Pydantic model.
"""
@esp_route.post("/")
async def post_sensor_data(sensor_reading: SensorTest):
    sensor_data = sensor_reading.model_dump()
    
    # Populate entries in the document
    sensor_data["tiemstamp"] = datetime.now()
    sensor_data["metadata"] = {"sensor_id": sensor_reading.sensor_id}
    ...
    # collection_name.insert_one(dict(item))