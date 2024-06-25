from bson import ObjectId
from fastapi import APIRouter
from datetime import datetime 
from config.db import collection_name
from models.model_sensor import SensorData
from schemas.schemas_sensor import (sensorData, sensorEntity, sensorsEntity,
                                    sensorsList)

sensor_route = APIRouter(prefix="/data", tags=["QA testing"])


# GET Request Method
@sensor_route.get("/")
async def find_all_sensors():
    all_data = sensorsList(collection_name.find())

    return all_data


# POST Request Method
@sensor_route.post("/")
async def post_sensor_data(item: SensorData):
    sensor_data = item.model_dump()
    sensor_data["timestamp"] = datetime.now()
    collection_name.insert_one(dict(item))
