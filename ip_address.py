import requests

# Function to handle IP address recognition
def recognize_ip_address(ip_address):
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    isp = data.get("isp")
    city = data.get("city")
    region = data.get("region")
    country = data.get("country")
    longitude = data.get("lon")
    latitude = data.get("lat")
    info = f"City: {city}\nRegion: {region}\nCountry: {country}\nLongitude: {longitude}\nLatitude: {latitude}\nISP: {isp}\n"
    return info