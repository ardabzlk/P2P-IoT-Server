from mongoengine import *

class TemperatureData(EmbeddedDocument):
    value = FloatField()
    unit = StringField()

class HumidityData(EmbeddedDocument):
    value = FloatField()
    unit = StringField()

class LocationData(EmbeddedDocument):
    city = StringField()
    country = StringField()
    latitude = FloatField()
    longitude = FloatField()

class Weather(Document):
    meta = {'collection': 'weather_data'}
    _id = StringField(required=True, primary_key=True)
    sensor = StringField(required=True)
    timestamp = DateTimeField(required=True)
    temperature = EmbeddedDocumentField(TemperatureData)
    humidity = EmbeddedDocumentField(HumidityData)
    location = EmbeddedDocumentField(LocationData)

    def to_dict(self):
        # Convert the Weather object to a dictionary
        weather_dict = {
            "sensor": self.sensor,
            "timestamp": self.timestamp.isoformat(),
            "temperature": {
                "value": self.temperature_value,
                "unit": self.temperature_unit
            },
            "humidity": {
                "value": self.humidity_value,
                "unit": self.humidity_unit
            },
            "location": {
                "city": self.location_city,
                "country": self.location_country,
                "latitude": self.location_latitude,
                "longitude": self.location_longitude
            }
        }
        return weather_dict
    
# write post method for Weather document
def post_weather_data(data):
    try:
        weather = Weather(
            _id=data["_id"],
            sensor=data["sensor"],
            timestamp=data["timestamp"],
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