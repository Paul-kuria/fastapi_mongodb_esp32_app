from pymongo.mongo_client import MongoClient 
from pymongo.server_api import ServerApi

from config.config import DevelopmentConfig

uri = DevelopmentConfig.MONGO_URI

client = MongoClient(uri, server_api=ServerApi('1'))

# db = client.IoT_wdb
db = client.todo_db
collection_name = db["sensor_readings"]


## Test
try:
    client.admin.command('ping')
    print(uri)
    print("Pinged your deployment. you successfully connnected to mongodb!")
except Exception as e:
    print(e)
