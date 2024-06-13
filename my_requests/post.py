import requests 
import json 

base_url = "https://fastapi-mongodb-esp32-app-2.onrender.com"


def post_one_sensor_document():
    post_url = f"{base_url}/sensors"

    document = {
        "timestamp": "string",
        "temperature_in_c": 21.54,
        "humidity": 70.1,
        "wifi_rssi": 65
    }

    try:
        res = requests.post(
            url=post_url,
            json = document,
        )

        status_code = res.status_code
        res.raise_for_status()

        print(status_code)
    
    except Exception as e:
        print(e)


if __name__ == "__main__":
    post_one_sensor_document()