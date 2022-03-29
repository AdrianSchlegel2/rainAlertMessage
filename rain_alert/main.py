import os
import requests
from twilio.rest import Client

API_KEY = os.environ["API_KEY_EV"]
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
parameters = {
    "lat": os.environ["MY_LAT"],
    "lon": os.environ["MY_LONG"],
    "appid": os.environ["OWM_API_KEY"],
    "exclude": "current,minutely,daily"
}

response = requests.get(
    OWM_ENDPOINT,
    params=parameters,
)

weather_data = response.json()
response.raise_for_status()

for i in range(12):
    hourly_precipitation = weather_data["hourly"][i]["weather"][0]["id"]
    if hourly_precipitation > 700:
        client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
        message = client.messages.create(
            body="Don't forget an umbrella!",
            from_=os.environ["TWILIO_NUMBER"],
            to=os.environ["MY_PHONE_NUMBER"]
        )


        print(message.status)
        break

