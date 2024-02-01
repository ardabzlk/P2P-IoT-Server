from src.models.weather_stats_model import Weather
from src.models.main_model import ResponseModel
import json

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


    try:
        q_set = Weather.objects()
        json_data = q_set.to_json()
        dicts = json.loads(json_data)
        response = ResponseModel(dicts)

        return response.get_success_response()
    except:
        response = ResponseModel()
        return response.get_bad_request_response()