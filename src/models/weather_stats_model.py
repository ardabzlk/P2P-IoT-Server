from mongoengine import *

class TemperatureData(EmbeddedDocument):
    value = FloatField()
    unit = StringField()

class HumidityData(EmbeddedDocument):
    value = FloatField()
    unit = StringField()

class TVOCData(EmbeddedDocument):
    value = FloatField()
    unit = StringField()

class CO2Data(EmbeddedDocument):
    value = FloatField()
    unit = StringField()

class AQIData(EmbeddedDocument):
    value = FloatField()
    unit = StringField()

class Weather(Document):
    meta = {'collection': 'weather_data'}
    _id = StringField(required=True, primary_key=True)
    timestamp = DateTimeField(required=True)
    temperature = EmbeddedDocumentField(TemperatureData)
    humidity = EmbeddedDocumentField(HumidityData)
    tvoc = EmbeddedDocumentField(TVOCData)
    co2 = EmbeddedDocumentField(CO2Data)
    aqi = EmbeddedDocumentField(AQIData)


    

    def to_dict(self):
        # Convert the Weather object to a dictionary
        weather_dict = {           
            "timestamp": self.timestamp.isoformat(),
            "temperature": {
                "value": self.temperature_value,
                "unit": self.temperature_unit
            },
            "humidity": {
                "value": self.humidity_value,
                "unit": self.humidity_unit
            },
            "tvoc": {
                "value": self.tvoc_value,
                "unit": self.tvoc_unit
            },
            "co2": {
                "value": self.co2_value,
                "unit": self.co2_unit
            },
            "aqi": {
                "value": self.aqi_value,
                "unit": self.aqi_unit
            }

        }
        return weather_dict
    