from src.models.weather_stats_model import Weather, TemperatureData, HumidityData, LocationData
from src.models.main_model import ResponseModel
import json
from flask import request

   

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
        # check if the data is already present in the database
        if Weather.objects(_id=data["_id"]).count() > 0:
            return False
        else:
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
            return response.get_success_response()
        except:
            response = ResponseModel()
            return response.get_bad_request_response()
    elif request.method == "POST":
        try:
            data = request.get_json()
            # if post weather turns False throw bad request
            if not post_weather_data(data):
                response = ResponseModel()
                return response.get_bad_request_response("Data already exists")
            else:
                post_weather_data(data)
                response = ResponseModel(data=data)
                return response.get_success_response()
        except:
            response = ResponseModel()
            return response.get_bad_request_response()
