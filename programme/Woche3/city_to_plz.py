# Function to load the postal code data from a file
def load_postal_code_data(file_path):
    postal_code_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            plz, city = line.strip().split('=')
            if city not in postal_code_dict:
                postal_code_dict[city] = []
            postal_code_dict[city].append(plz)
    return postal_code_dict

# Function to get postal codes for a given city
def get_postal_codes_for_city(city, postal_code_dict):
    return postal_code_dict.get(city, [])

# Main script
if __name__ == "__main__":
    # Path to the postal code data file
    file_path = "./programme/Woche3/postal_codes_updated.data"
    
    # Load the data
    postal_code_dict = load_postal_code_data(file_path)
    
    # User input for city
    city = input("Geben Sie eine Stadt ein: ")
    
    # Get and display postal codes
    postal_codes = get_postal_codes_for_city(city, postal_code_dict)
    if postal_codes:
        print(f"Die Postleitzahlen für {city} sind: {', '.join(postal_codes)}")
    else:
        print(f"Keine Postleitzahlen für {city} gefunden.")
