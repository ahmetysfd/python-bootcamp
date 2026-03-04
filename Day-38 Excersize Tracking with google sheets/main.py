import requests
from datetime import datetime

SHEETY_ENDPOINT = "https://api.sheety.co/db57bc1cb13229d3eee26c89e927b4b1/workoutTracking/workouts"

GENDER = "male"
WEIGHT_KG = "80"
HEIGHT_CM = "190"
AGE = "23"

api_id = "6d68acc0"
api_key = "cb812b929fb49163fc1b45b9a00dde1b"

user_input = input("Describe your exercise: ")


user_profile = {
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 190,
    "age": 23
}

nutritionix_headers = {
    "x-app-id": api_id,
    "x-app-key": api_key,
    "Content-Type": "application/json"
}

nutritionix_body = {
    "query": user_input,
    **user_profile
}

exercise_response = requests.post(
    "https://trackapi.nutritionix.com/v2/natural/exercise",
    headers=nutritionix_headers,
    json=nutritionix_body
)

exercises = exercise_response.json()["exercises"]

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for exercise in exercises:
    workout_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(
        SHEETY_ENDPOINT,
        json=workout_data
    )

    print(f"Logged: {workout_data['workout']['exercise']} — Status: {sheety_response.status_code}")
