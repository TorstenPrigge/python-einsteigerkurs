import requests

def get_city_info(postal_code, country_code="DE"):
    """
    Ruft Stadtinformationen für eine Postleitzahl aus der Zippopotam-API ab.
    
    :param postal_code: Die Postleitzahl
    :param country_code: Der Ländercode (Standard: "DE" für Deutschland)
    :return: Informationen zur Stadt oder eine Fehlermeldung
    """
    url = f"https://api.zippopotam.us/{country_code}/{postal_code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        return f"Keine Daten für die Postleitzahl '{postal_code}' gefunden."
    else:
        return f"Fehler beim Abrufen der Daten (Statuscode: {response.status_code})."

if __name__ == "__main__":
    postal_code = input("Geben Sie eine Postleitzahl ein: ").strip()
    result = get_city_info(postal_code)
    
    if isinstance(result, dict):
        print(f"Details für PLZ {postal_code}:")
        print(f"Ort: {result['places'][0]['place name']}")
        print(f"Bundesland: {result['places'][0]['state']}")
    else:
        print(result)