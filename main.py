import requests
from datetime import datetime

API_KEY = "-"
APP_ID = "-"
TOKEN = "-"

EXCERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/ef759fee6bd4cbaa47451ecacc177e48/myWorkouts/workouts"

## input
excercise = input("Tell me which excercise you did: ")


headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    "Authorization": f"Bearer {TOKEN}"
}

excercise_params = {
    "query": excercise,
    "weight_kg": 47,
    "height_cm": 169,
    "age": 18 
}

response = requests.post(url=EXCERCISE_ENDPOINT, headers=headers, json=excercise_params)
# print(response.text)
exercises = response.json()['exercises']
print(exercises[0]['name'])
print(exercises[1]['name'])





## sheety

# response = requests.get(url=f"{SHEETY_ENDPOINT}/2")
# print(response.text)

today = datetime.now()
day_formatted = today.strftime("%Y/%m/%d")
time_formatted = today.strftime("%H:%M:%S")


for exercise in exercises : 
    # data for n-excercise
    workout_data = {
        "workout": {
            "date": day_formatted,
            "time": time_formatted,
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
    # posting
    response = requests.post(url=SHEETY_ENDPOINT, json=workout_data, headers=headers)
