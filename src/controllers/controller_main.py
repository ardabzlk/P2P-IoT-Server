from src.models.weather_stats_model import Weather, TemperatureData, HumidityData, LocationData
from src.models.main_model import ResponseModel
import json
from flask import jsonify, request, make_response

   

def post_weather_data(data):
    try:
        from datetime import datetime  # Import the datetime module

        weather = Weather(
            _id=data["_id"],
            sensor=data["sensor"],
            timestamp=datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S"),  # Convert timestamp to datetime object
            temperature=TemperatureData(
                value=data["temperature"]["value"],
                unit=data["temperature"]["unit"]
            ),
            humidity=HumidityData(
                value=data["humidity"]["value"],
                unit=data["humidity"]["unit"]
            ),
            location=LocationData(
                city=data["location"]["city"],
                country=data["location"]["country"],
                latitude=data["location"]["latitude"],
                longitude=data["location"]["longitude"]
            )
        )
        weather.save()
        return True
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
            return "arda"
        except:
            response = ResponseModel()
            return response.get_bad_request_response()
    elif request.method == "POST":
        try:
            data = request.get_json()
            post_weather_data(data)
            response = ResponseModel(data=data)
            return response.get_success_response()
        except:
            response = ResponseModel()
            return response.get_bad_request_response()
