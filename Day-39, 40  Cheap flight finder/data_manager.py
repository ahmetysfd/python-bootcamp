import requests

class DataManager:
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/db57bc1cb13229d3eee26c89e927b4b1/flightDealsDosyasınınKopyası/prices"

    def get_sheet_data(self):
        response = requests.get(self.sheety_endpoint)
        response.raise_for_status()
        data = response.json()
        return data["prices"]

    def update_iata_code(self, row_id, new_iata_code):
        update_url = f"{self.sheety_endpoint}/{row_id}"
        body = {
            "price": {
                "iataCode": new_iata_code
            }
        }
        response = requests.put(update_url, json=body)
        response.raise_for_status()
        print(f"✅ Updated row {row_id} with IATA code: {new_iata_code}")
