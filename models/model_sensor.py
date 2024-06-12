from datetime import datetime

from pydantic import BaseModel


# Define base class to share attributes
class SensorData(BaseModel):
    # __abstract__ = "True"

    sensor_name: str
    timestamp: str
    air_temp: str
    air_hummid: str
    soi_temp: str
    soil_hummid: str
    batt_level: str
    coordinates: str

    created_at: int = int(datetime.timestamp(datetime.now()))
    updated_at: int = int(datetime.timestamp(datetime.now()))


class SensorTest(BaseModel):
    # __abstract__ = "True"

    _id: str
    timestamp: str
    temperature_in_c: float
    humidity: float
    wifi_rssi: float
