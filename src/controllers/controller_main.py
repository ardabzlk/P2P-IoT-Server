from src.models.weather_stats_model import Weather
from src.models.main_model import ResponseModel
import json
from flask import jsonify, request, make_response

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
    


def process_data():
    try:
        # Assuming the incoming data is in JSON format
        data = request.get_json()

        # Process the data as needed (you can replace this with your actual processing logic)

        # Print the processed data to the console
        print("Processed Data:", data)

        # Return a response (you can customize this based on your requirements)
        response_data = {"message": "Data processed successfully", "data": data}
        return jsonify(response_data), 200

    except Exception as e:
        # Handle any exceptions that may occur during processing
        error_message = {"error": str(e)}
        return jsonify(error_message), 500