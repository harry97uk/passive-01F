from social_media.instagram_search import advanced_lookup
from social_media.facebook_search import facebook_search
from social_media.linkedin_search import linkedin_search
from social_media.twitter_search import twitter_search_by_full_name, twitter_search_by_username
from social_media.skype_search import skype_search
from social_media.youtube_search import youtube_search

instagram_found = False
facebook_found = False
twitter_found = False

def search_with_full_name(first_name,last_name,full_name,username):
    global facebook_found
    global twitter_found
    facebook_data = facebook_search(last_name, first_name)
    facebook_found = facebook_data.__contains__(full_name)

    twitter_data = twitter_search_by_full_name(last_name, first_name)
    twitter_found = twitter_data.__contains__(username)

    #print(skype_search(last_name, first_name))

def recognize_username(username):
    # Implement username recognition and social network check logic here
    # Sample logic:
    instagram_data = advanced_lookup(username)
    instagram_found = True if instagram_data.get("user").get("message") != "No users found" else False
    full_name = instagram_data.get("user", {}).get("user", {}).get("full_name")
    youtube_found = youtube_search(username)

    twitter_data = twitter_search_by_username(username)
    twitter_found = twitter_data.__contains__(username)

    if full_name: 
        names = full_name.split(" ")
        if len(names) > 1:
            first_name = full_name.split(" ")[0]
            last_name = full_name.split(" ")[1]
            search_with_full_name(first_name, last_name, full_name, username)

                
    social_networks = {
        "Facebook": "yes" if facebook_found else "no",
        "Twitter": "yes" if twitter_found else "no",
        "Linkedin": "yes",
        "Instagram": "yes" if instagram_found else "no",
        "Youtube": "yes" if youtube_found else "no",
    }
    return social_networks