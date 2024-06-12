from fastapi import APIRouter 

from models.model_sensor import SensorData, SensorTest
from config.db import collection_name 

from schemas.schemas_sensor import sensorEntity, sensorsEntity, sensorData, sensorsList
from bson import ObjectId 

sensor_route = APIRouter(prefix="/data", tags=["QA testing"])

# GET Request Method 
@sensor_route.get('/')
async def find_all_sensors():
    all_data = sensorsList(collection_name.find( ))
    
    return all_data

# POST Request Method
@sensor_route.post("/")
async def post_sensor_data(item: SensorTest):
    collection_name.insert_one(dict(item))