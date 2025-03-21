import sys
import requests
import json


directions_api = "https://api.openrouteservice.org/v2/directions/driving-car"
geocode_api = "https://api.openrouteservice.org/geocode/search?"
key = "5b3ce3597851110001cf6248ac54a82d61cd4d6db7afd18fc207821f" 


def geocode_address(address):
    """Geocodifica una dirección y devuelve sus coordenadas."""
    url = f"{geocode_api}api_key={key}&text={address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        if json_data["features"]:
            coords = json_data["features"][0]["geometry"]["coordinates"]
            return coords  
    
    return None


if len(sys.argv) != 3:
    print("Error: Debes proporcionar una ubicación de origen y destino.")
    sys.exit(1)

orig = sys.argv[1]
dest = sys.argv[2]


orig_coords = geocode_address(orig)
dest_coords = geocode_address(dest)

if not orig_coords or not dest_coords:
    print("Error: No se pudieron geocodificar una o ambas direcciones.")
    sys.exit(1)


body = {
    "coordinates": [orig_coords, dest_coords]
}

headers = {
    "Authorization": key,
    "Content-Type": "application/json"
}

response = requests.post(directions_api, headers=headers, json=body)
json_data = response.json()

if response.status_code == 200 and 'routes' in json_data and json_data['routes']:
    route = json_data['routes'][0]
    if 'segments' in route and route['segments']:
        segment = route['segments'][0]
        

        duration = segment.get('duration', 'N/A')
        distance = segment.get('distance', 'N/A')

   
        print(f"Ruta desde {orig} hasta {dest}:")
        print(f"Duración estimada: {duration / 60:.2f} minutos")
        print(f"Distancia: {distance / 1000:.2f} km")
        print("\nIndicaciones paso a paso:\n")

        if 'steps' in segment:
            for step in segment['steps']:
                instruction = step.get('instruction', 'N/A')
                step_distance = step.get('distance', 'N/A')
                print(f"- {instruction} ({step_distance:.2f} m)")
        else:
            print("No hay instrucciones detalladas disponibles.")

    else:
        print("Error: No se encontraron segmentos en la ruta.")
else:
    print(f"Error: {response.status_code} - {response.text}")
