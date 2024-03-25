## **Flight Details Extraction and Sorting Script**

### **Overview**
This script processes flight offer data retrieved from the Amadeus Flight Offers Search API. It parses the JSON response from a file, extracts detailed information about each flight offer, and sorts the data by price in ascending order for easy analysis and readability.

### **API Request**
To retrieve flight offers data, the script is designed to work with data obtained from the following API request:
```
GET https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=BKK&destinationLocationCode=FRA&departureDate=2024-04-26&adults=1
```
This request fetches flight offers for a specific route (from Bangkok (BKK) to Frankfurt (FRA)), on a specific departure date (April 26, 2024) for one adult.

### **Description**
Before running the script, you should first retrieve the flight offers using the Amadeus API. The script then parses the obtained JSON data, which includes details of various flight offers corresponding to the given criteria (origin, destination, date, number of passengers).

### **Module Composition**

1. **Imported Libraries**
   - `json`: Used for parsing JSON data.

2. **Data Mappings**
   - `aircraft_mapping`: Maps aircraft codes to their names.
   - `carrier_mapping`: Maps carrier codes to their names.

3. **Main Data Processing Steps**
   - **File Reading**: Opens and reads a JSON file containing flight offers.
   - **JSON Parsing**: Converts the JSON string into Python data structures.
   - **Data Extraction**: Iterates over each flight offer to extract necessary details.
   - **Data Sorting**: Sorts the extracted flight details by price in ascending order.
   - **File Writing**: Writes the sorted flight details to a text file.

4. **Key Variables**
   - `file_path`: Path to the JSON file containing flight offers.
   - `flight_details`: Dictionary storing extracted data for each flight.

5. **Functions and Loops**
   - The script primarily uses a series of nested loops to process the JSON data and extract required information.

### **Usage**

1. **Setting Up**
   - Ensure the JSON file with flight data is placed in the specified path.
   - Update the `file_path` variable if necessary.

2. **Running the Script**
   - Execute the script in a Python environment. The script will process the data and create an output file named `flight_details.txt` with sorted flight information.

3. **Output**
   - The output file (`flight_details.txt`) will contain detailed information about each flight offer, sorted by price. Each flight's details are separated for readability.

### **Examples**

```python
# Define a mapping for aircraft codes to names
aircraft_mapping = {"320": "AIRBUS A320", "789": "BOEING 787-9", ...}

# Define a mapping for carrier codes to names
carrier_mapping = {"QR": "QATAR AIRWAYS", "LH": "LUFTHANSA", ...}

# Rest of the script...
```

This script will output a file `flight_details.txt`, where each flight offer is detailed with identifiers, price, aircraft type, carrier, and segment information.

### **Flow Diagram**

The script flow can be visualized as follows:
1. Read JSON file → 2. Parse JSON → 3. Extract Data → 4. Sort Data → 5. Write to File


*Note: The documentation should be placed in a separate markdown file or as a header in the script file. It should be updated as changes are made to the script to ensure consistency and relevance.*

