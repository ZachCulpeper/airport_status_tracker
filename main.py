airport = input("Please enter an airport code: ")
airport = airport.upper().strip()

airports = {
    "JFK": "Ground Stop",
    "BOS": "Ground Delay",
    "ORD": "Normal"
}

if airport in airports:
    print(airports[airport])
else:
    print("Airport not found. Please try again.")

