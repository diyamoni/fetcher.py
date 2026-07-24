import requests
import json
from datetime import datetime
print("1. Current Weather")
print("2. Currency Exchange Rate")
print("3. Save Result to JSON File")
print("4. View Previous Saved Data")
print("5. Exit")
def weather():
    city = input("Enter city name: ")

    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    data = response.json()

    current = data['current_condition'][0]

    print("\n----- Weather Report -----")
    print(f"City: {city}")
    print(f"Temperature: {current['temp_C']}°C")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind Speed: {current['windspeedKmph']} km/h")
    print(f"Condition: {current['weatherDesc'][0]['value']}")
    print(f"Fetched At: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")
    print("--------------------------\n")
def currency():
    from_currency = input("From Currency (ex: USD): ")
    to_currency = input("To Currency (ex: BDT): ")
    amount = float(input("Amount: "))

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    rate = data['rates'][to_currency]
    converted = amount * rate

    print("\n----- Currency Exchange -----")
    print(f" {amount} {from_currency} = {converted:.2f} {to_currency}")
    print("---------------------------")
def save_to_json():
    data = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "result": converted,
        "rate": rate
    }
    with open("data.json", "w") as f:
        json.dump(data, f)
    print("Data saved to data.json")
        
choice = input("Enter your choice: ")
if choice == "1":
    weather()
elif choice == "2":
    currency()
elif choice == "3":
        save_to_json()
elif choice == "5":

    print("Exiting...")
    exit()
 
else:
    print("Coming Soon!")







