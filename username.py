# Function to handle username recognition
import requests

def penguin():
    response = requests.get("https://api.getpenguin.com/check/services/details")
    data = response.json()
    print(data)



def recognize_username(username):
    # Implement username recognition and social network check logic here
    # Sample logic:
    penguin()

    social_networks = {
        "Facebook": "yes",
        "Twitter": "yes",
        "Linkedin": "yes",
        "Instagram": "no",
        "Skype": "yes",
    }
    return social_networks