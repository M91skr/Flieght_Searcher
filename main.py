"""---------------------------------------- Flight Searcher ----------------------------------------
In this code, the user's city of residence, a list of the user's favorite cities for travel, and
the maximum ticket price that the user is willing to pay for each city are received.
Then the flight price API is called, and if a flight is found for each city with a price lower than
the user's desired price, a notification SMS is sent to the user.

Note:
Please:
1. Enter a google sheet of your favorite cities, the IATA code of each city and the maximum flight price to travel
from your city to that city.
2. Sign up at https://dashboard.sheety.co/login and create an api from your Google Sheet.
3. Sign up at https://tequila.kiwi.com/portal/login and get the free flight inquiry api.
4. Sign up at https://console.twilio.com and get up to a virtual number to send SMS or WhatsApp notifications.

You can run this code in the cloud, defined for that daily task, and enjoy your reminder.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

import os
from datetime import datetime, timedelta

from twilio.rest import Client

from data_manager import DataManager
from flight_search import FlightSearch

# ---------------------------------------- Add Parameters ----------------------------------------

ORIGIN_CITY_IATA = "BER"
sid = "TWILIO_SID"
auth_token = "TWILIO_AUTH_TOKEN"
virtual_number = "TWILIO_VIRTUAL_NUMBER"
verified_number = "TWILIO_VERIFIED_NUMBER"

# ---------------------------------------- Classes Calling ----------------------------------------

data_manager = DataManager()
flight_search = FlightSearch()

""" ---------------------------------------- Main application ----------------------------------------
Get the list of cities
"""

sheet_data = data_manager.get_destination_data()

# ---------------------------------------- Search Time Period Specification ----------------------------------------

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

# ---------------------------------------- Flight Search ----------------------------------------

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # ---------------------------------------- Filtering available flight prices --------------------------------------

    if flight and flight["price"] < destination["maxPrice(euro)"]:
        client = Client(os.getenv(sid), os.getenv(auth_token))
        message = client.messages.create(
            body=f"Low price alert! Only £{flight['price']} to fly from {flight['cityFrom']} to {flight['cityTo']} by "
                 f"airline {flight['airlines']} from {flight['local_departure']} and link {flight['deep_link']}",
            from_=os.getenv(virtual_number),
            to=os.getenv(verified_number)
        )
        print(message.status)
