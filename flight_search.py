import requests
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
api_key = "API_KEY"


class FlightSearch:
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": os.getenv(api_key)}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
            return data
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
