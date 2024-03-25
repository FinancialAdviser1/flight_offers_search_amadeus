import json

# Path to your JSON file
file_path = r"Response.json"

# Define a mapping for aircraft codes to names
aircraft_mapping = {
        "221": "AIRBUS  A220-100",
        "223": "AIRBUS  A220-300",
        "290": "EMBRAER 190 E2",
        "319": "AIRBUS A319",
        "320": "AIRBUS A320",
        "321": "AIRBUS A321",
        "333": "AIRBUS A330-300",
        "343": "AIRBUS A340-300",
        "346": "AIRBUS A340-600",
        "359": "AIRBUS A350-900",
        "388": "AIRBUS A380-800",
        "744": "BOEING 747-400",
        "772": "BOEING 777-200/200ER",
        "781": "BOEING 787-10",
        "788": "BOEING 787-8",
        "789": "BOEING 787-9",
        "74H": "BOEING 747-8",
        "32N": "AIRBUS A320NEO",
        "E95": "EMBRAER 195",
        "E75": "EMBRAER 175",
        "AT7": "ATR 72",
        "CR9": "CANADAIR REGIONAL JET 900",
        "73H": "BOEING 737-800 (WINGLETS)",
        "73J": "BOEING 737-900",
        "77W": "BOEING 777-300ER"
      }

# Define a mapping for carrier codes to names
carrier_mapping = {
        "EE": "XFLY",
        "QR": "QATAR AIRWAYS",
        "KL": "KLM ROYAL DUTCH AIRLINES",
        "WX": "CITYJET",
        "LO": "LOT POLISH AIRLINES",
        "OS": "AUSTRIAN AIRLINES",
        "EK": "EMIRATES",
        "CL": "LUFTHANSA CITYLINE",
        "N7": "UNDEFINED",
        "LX": "SWISS INTERNATIONAL AIR LINES",
        "BR": "EVA AIR",
        "BT": "AIR BALTIC",
        "TG": "THAI AIRWAYS INTERNATIONAL",
        "TK": "TURKISH AIRLINES",
        "AY": "FINNAIR",
        "SK": "SCANDINAVIAN AIRLINES",
        "2L": "HELVETIC AIRWAYS",
        "NH": "ALL NIPPON AIRWAYS",
        "LH": "LUFTHANSA"
      }

# Open and read the JSON file
with open(file_path, 'r') as file:
    json_data = file.read()

# Load JSON data
data = json.loads(json_data)

# Initialize an empty dictionary to store flight ID, price, and aircraft information
flight_details = {}

# Iterate over each flight offer
for offer in data['data']:
    flight_id = offer['id']
    total_price = offer['price']['total']
    number_of_seats = offer['numberOfBookableSeats']  # Extract the number of bookable seats

    # Initialize a list to store detailed information for each segment
    segments_info = []

    # Iterate over each segment in the itineraries
    for itinerary in offer['itineraries']:
        for segment in itinerary['segments']:
            aircraft_code = segment['aircraft']['code']
            carrier_code = segment['carrierCode']
            # Remap the aircraft code and carrier code to their names
            aircraft_name = aircraft_mapping.get(aircraft_code, "Unknown Aircraft")
            # Remap the carrier code to its name
            carrier_code = segment.get('carrierCode', 'Unknown')  # Using .get to avoid KeyError
            carrier_name = carrier_mapping.get(carrier_code, "Unknown Carrier")

            # Extracting detailed segment information
            segment_detail = {
                'departure': segment['departure']['iataCode'],
                'departure_time': segment['departure']['at'],
                'arrival': segment['arrival']['iataCode'],
                'arrival_time': segment['arrival']['at'],
                'duration': segment['duration'],
                'aircraft': aircraft_name,
                'carrier': carrier_name,
                'flightNumber': segment['number'],
                'numberOfStops': segment['numberOfStops'],
                'blacklistedInEU': segment['blacklistedInEU']
            }
            segments_info.append(segment_detail)


    # Store the flight ID, price, segment details, and number of bookable seats in the dictionary
    flight_details[flight_id] = {
        'price': total_price, 
        'segments': segments_info,
        'numberOfBookableSeats': number_of_seats
    }

# Convert the flight_details dictionary to a list of tuples
flight_details_list = list(flight_details.items())

# Sort the list by price in ascending order
sorted_flight_details = sorted(flight_details_list, key=lambda x: float(x[1]['price']))

# Open a text file to write the output
with open('flight_details.txt', 'w') as file:
    # Loop through the flight_details dictionary
    for flight_id, details in flight_details.items():
        file.write(f"Flight ID: {flight_id}\n")
        file.write(f"Price: {details['price']}\n")
        file.write(f"Number of Bookable Seats: {details['numberOfBookableSeats']}\n")
        file.write("Segments:\n")
        for segment in details['segments']:
            file.write(f"  Departure: {segment['departure']} at {segment['departure_time']}\n")
            file.write(f"  Arrival: {segment['arrival']} at {segment['arrival_time']}\n")
            file.write(f"  Duration: {segment['duration']}\n")
            file.write(f"  Aircraft: {segment['aircraft']}\n")
            file.write(f"  Carrier: {segment['carrier']}, Flight Number: {segment['flightNumber']}\n")
            file.write(f"  Number of Stops: {segment['numberOfStops']}\n")
            file.write(f"  Blacklisted in EU: {segment['blacklistedInEU']}\n")
            file.write("  ---\n")
        file.write("-" * 30 + "\n")  # Just a separator for readability