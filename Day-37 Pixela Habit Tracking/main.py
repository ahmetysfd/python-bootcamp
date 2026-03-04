import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "789632145"
USERNAME = "ahmet11"

user_params = {
    "token": TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
   "name": "Coding Graph",
   "unit": "Hours",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


postpixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()


post_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Hours did you study today? "),
}

response = requests.post(url=postpixel_endpoint, json=post_pixel, headers=headers)
print(response.text)



#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)


