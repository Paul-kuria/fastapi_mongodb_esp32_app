
def sensorEntity(item) -> dict:
    return {
        "sensor_id": str(item["_id"]),
        "timestamp" : item["timestamp"],
        "air_temp" :item["air_temp"],
        "air_hummid" : item["air_hummid"],
        "soi_temp" : item["soi_temp"],
        "soil_hummid" : item["soil_hummid"],
        "batt_level" : item["batt_level"],
        "coordinates" : item["coordinates"],
    }

def sensorData(item) -> dict:
    return {
        "id": str(item["_id"]),
        "timestamp" : item["timestamp"],
        "temperature_in_c" :item["temperature_in_c"],
        "humidity" : item["humidity"],
        "wifi_rssi" : item["wifi_rssi"],
    }

def sensorsList(entity) -> list:
    return [sensorData(item) for item in entity] 

def sensorsEntity(entity) -> list:
    return [sensorEntity(item) for item in entity]