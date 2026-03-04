import requests

TOKEN = "789632145"
USERNAME = "ahmet11"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

# Add entry for 11 July 2025
pixel_data_11 = {
    "date": "20250809",
    "quantity": input("How many hours did you study on 09.08? "),
}
response_11 = requests.post(url=pixela_endpoint, json=pixel_data_11, headers=headers)
print("19 July response:", response_11.text)

