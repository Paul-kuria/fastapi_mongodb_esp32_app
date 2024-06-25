from datetime import datetime

from pydantic import BaseModel
from typing import Optional


# Define base class to share attributes
class SensorData(BaseModel):
    # __abstract__ = "True"

    sensor_name: str
    timestamp: Optional[str]= None
    air_temp_in_c: Optional[str] = None
    air_humidity: Optional[str]= None
    soil_temp_in_c: Optional[str]= None
    soil_humidity: Optional[str]= None
    batt_level: Optional[str]= None
    gsm_rssi: str
    ipAddress: Optional[str]= None
    coordinates: Optional[str]= None

    # Automatically set created at and updated at during data creation
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class SensorTest(BaseModel):
    # __abstract__ = "True"

    _id: str
    # timestamp: str
    temperature_in_c: float
    humidity: float
    wifi_rssi: float
