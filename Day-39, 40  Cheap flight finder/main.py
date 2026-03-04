from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_sheet_data()

for row in sheet_data:
    if row["iataCode"] == "":
        city = row["city"]
        iata_code = flight_search.get_iata_code(city)
        row["iataCode"] = iata_code
        data_manager.update_iata_code(row["id"], iata_code)

# Final check
print("✅ Final sheet data after updates:")
pprint(sheet_data)
