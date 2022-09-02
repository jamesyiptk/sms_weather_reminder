import requests
from twilio.rest import Client

owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "28f31b8bd6d4c52a475f36c25bb893c7"
account_sid = "ACb17f468004383c3b745ea23377564942"
auth_token = "c65301d4b342826ce717954d78885e49"


weather_params = {
    "lat": 37.566536,
    "lon": 126.977966,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
twelve_hour_data = weather_data['hourly'][:12]
bring_umbrella = False
for i in twelve_hour_data:
    weather_id = i['weather'][0]['id']
    if weather_id < 700:
        bring_umbrella = True
if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an umbrella",
                from_='+19787055278',
                to='+85261902129')
    print(message.status)
