import requests
import os

prices_endpoint = "SHEETY_PRICES_ENDPOINT"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=os.getenv(prices_endpoint))
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data
