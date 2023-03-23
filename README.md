## Pick up the Umbrella Reminder

## Description
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


## How to run
run following:
```bash
python -m venv env
. env/bin/activate
pip install -r requirements.txt
python main.py
```