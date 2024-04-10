from src.models.weather_stats_model import Weather, TemperatureData, HumidityData, TVOCData, CO2Data, AQIData
from src.models.main_model import ResponseModel
import json
from flask import request
import datetime

   

def post_weather_data(data):
 
    try:
        # Get the current time in UTC
        utc_time = datetime.datetime.utcnow()

        # Create a timezone object for GMT+2
        gmt_plus_2 = datetime.timezone(datetime.timedelta(hours=4))

        # Convert the UTC time to GMT+2
        gmt_plus_2_time = utc_time.astimezone(gmt_plus_2)

        # Convert the GMT+2 time to timestamp
        _timestamp = gmt_plus_2_time.timestamp()
        weather = Weather(

            timestamp= _timestamp,
            temperature=TemperatureData(
                value=data["temperature"]["value"],
                unit=data["temperature"]["unit"]
            ),
            humidity=HumidityData(
                value=data["humidity"]["value"],
                unit=data["humidity"]["unit"]
            ),
            tvoc=TVOCData(
                value=data["tvoc"]["value"],
                unit=data["tvoc"]["unit"]
            ),
            co2=CO2Data(
                value=data["co2"]["value"],
                unit=data["co2"]["unit"]
            ),
            aqi=AQIData(
                value=data["aqi"]["value"],
                unit=data["aqi"]["unit"]
            )
            
        )

        weather.save()
           
    except Exception as e:
        print("Error in post_weather_data:", str(e))
        return False
    

def weather_stats():
    """###
    
    Parameters
    ----------
    none

    Returns
    -------
    json
        user list
        
    Exceptions
    ----------
    Bad request response if the request is not valid
    ResponseModel.get_bad_request_response()
    """

    if request.method == "GET":
        try:
            q_set = Weather.objects()
            json_data = q_set.to_json()
            dicts = json.loads(json_data)
            response = ResponseModel(dicts)
            return response.get_success_response()
        except Exception as e:
            response = ResponseModel()
            return response.get_bad_request_response(str(e))
    elif request.method == "POST":
        try:
            data = request.get_json()
  
            post_weather_data(data)
            response = ResponseModel(data='Data saved successfully')
            return response.get_success_response()
        except Exception as e:
            response = ResponseModel()
            return response.get_bad_request_response(str(e))
