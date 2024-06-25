# def sensorEntity(item) -> dict:
#     return {
#         "sensor_id": str(item["_id"]),
#         "timestamp": item["timestamp"],
#         "air_temp_in_c": item["air_temp_in_c"],
#         "air_humidity": item["air_humidity"],
#         "soil_temp_in_c": item["soil_temp_in_c"],
#         "soil_humidity": item["soil_humidity"],
#         "gsm_rssi": item["gsm_rssi"],
#         "batt_level": item["batt_level"],
#         "ipAddress": item["ipAddress"],
#         "coordinates": item["coordinates"],
#     }


# def sensorData(item) -> dict:
#     return {
#         "id": str(item["_id"]),
#         "timestamp": item["timestamp"],
#         "air_temp_in_c": item["air_temp_in_c"],
#         "air_humidity": item["air_humidity"],
#         "soil_temp_in_c": item["soil_temp_in_c"],
#         "soil_humidity": item["soil_humidity"],
#         "gsm_rssi": item["gsm_rssi"],
#         "ipAddress": item["ipAddress"],
#     }
def sensorEntity(item) -> dict:
    return {
        "sensor_id": str(item["_id"]),
        "timestamp": item.get("timestamp"),  # Handle potential absence of timestamp
        "air_temp_in_c": item.get("air_temp_in_c"),  # Handle potential absence
        "air_humidity": item.get("air_humidity"),  # Handle potential absence
        "soil_temp_in_c": item.get("soil_temp_in_c"),  # Handle potential absence
        "soil_humidity": item.get("soil_humidity"),  # Handle potential absence
        "gsm_rssi": item["gsm_rssi"],
        "batt_level": item.get("batt_level"),  # Handle potential absence
        "ipAddress": item.get("ipAddress"),  # Handle potential absence
        "coordinates": item.get("coordinates"),  # Handle potential absence
    }


def sensorData(item) -> dict:
    return {
        "id": str(item["_id"]),
        "timestamp": item.get("timestamp"),  # Handle potential absence of timestamp
        "air_temp_in_c": item.get("air_temp_in_c"),  # Handle potential absence
        "air_humidity": item.get("air_humidity"),  # Handle potential absence
        "gsm_rssi": item["gsm_rssi"],
    }


def sensorsList(entity) -> list:
    return [sensorData(item) for item in entity]


def sensorsEntity(entity) -> list:
    return [sensorEntity(item) for item in entity]
