import requests 
import json 

base_url = "https://fastapi-mongodb-esp32-app-2.onrender.com"
thingspeak = "https://api.thingspeak.com/update"

def post_one_sensor_document():
    post_url = f"{base_url}/data"
    furl = "https://fastapi-mongodb-esp32-app-2.onrender.com/data/"
    document = {
        "air_temp_in_c":"26.012",
        "air_humidity":"55.1",
        "gsm_rssi":"-50",
        "soil_temp_in_c": "15.2",
        "soil_humidity": "43",
        "macAddress": "EB:5F:4G:2A:RZ",
        "ipAddress": "100.128.180.103",
        "sensor_name": "sensor_ttgo1",
        "batt_level": "4.05",

    }

    try:
        res = requests.post(
            url=furl,
            json = document,
        )

        status_code = res.status_code
        res.raise_for_status()

        print(status_code)
    
    except Exception as e:
        print(e)


def post_on_thingspeak():
    things_params = {
        "api_key":"L992JI6EJZXRG4ZY",
        "field1": 75,
        "field2": 65,
        "field3": 21.5,
        "field4": 80,
        "field5": 10,
        }
    try:
        res = requests.post(
            url=thingspeak,
            params=things_params,
            # json = document,
        )

        status_code = res.status_code
        res.raise_for_status()

        print(status_code)
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    post_one_sensor_document()