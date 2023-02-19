# Import two libraries used:
import pandas as pd
import requests
import time
from datetime import date
from tkinter import filedialog as fd
import os


# Configure Soundcharts Sandbox credentials:
endpoint = "https://sandbox.api.soundcharts.com/api/v2" # Sandbox API's url
headers = {
    "x-app-id" : 'soundcharts',
    "x-api-key" : 'soundcharts'
}

test_spotify_ids = ['6qqNVTkY8uBg9cP3Jd7DAH', '2NjfBq1NflQcKSeiDooVjY'] # Sandbox sample of SpotifyID artists


# User_input chooses `spotify_ids` file:
try:
    spotify_ids_list = fd.askopenfilename(initialdir='input')
    csv = pd.read_csv(f'input/{os.path.split(spotify_ids_list)[1]}')
    print(f'File chosen: {os.path.split(spotify_ids_list)[1]}.\n')
    print(f'File looks like:\n{csv}\n\n')
except Exception as e:
    print(e)
    

# Define functions:    
def getSoundchartsUUID(spotify_id):
    response = requests.get(f"{endpoint}/artist/by-platform/spotify/{spotify_id}", headers=headers)
    json = response.json()
    return json['object']['uuid'] if response.status_code == 200 else f'Error. Response: {response.status_code}'

def getArtistName(spotify_id): # Returns artist's name as a string
    uuid = getSoundchartsUUID(spotify_id)
    response = requests.get(f"{endpoint}/artist/{uuid}", headers = headers)
    json = response.json()
    return json["object"]["slug"] if response.status_code == 200 else f'Error. Response: {response.status_code}'

def getMonthlyListeners(spotify_id): 
    uuid = getSoundchartsUUID(spotify_id)
    response = requests.get(f"{endpoint}/artist/{uuid}/streaming/spotify/listeners", headers = headers)
    json = response.json()
    return json['items'][0]['value'] if response.status_code == 200 else f'Error. Response: {response.status_code}'


# Loops through all `spotifyIDs` and appends the outputs in the `artist_names` and `monthly_listeners` lists
output_df = pd.DataFrame(columns=['artist_name', 'monthly_listeners']) # Prepares empty `output_df` DataFrame
artist_names = []
monthly_listeners = []
for id in test_spotify_ids: # Fills `artist_name` and `monthly_listeners` lists with `artist_name` and `monthly_listeners` rows
    artist_names.append(getArtistName(id)), monthly_listeners.append(getMonthlyListeners(id))
    

# Formats the DF from the above lists:
try:
    output_df['artist_name'], output_df['monthly_listeners'] = artist_names, monthly_listeners # Sends the created lists above to the relevant columns
    print(f'Output DataFrame looks like: \n{output_df}\n') # If successfully prints correct DF, then prints success message
except Exception as e:
    print(e) # Else, prints error and stops
time.sleep(2)


# Prints it to 'output/amuzed/{filename}.csv'
try:
    output_df.to_csv(f'output/results-{date.today()}.csv', index=False) # Prints to 'output/amuzed/{filename}.csv
    print(f"File successfully saved to 'output/results-{date.today()}.csv!\nExiting now.") # Confirmation message
except Exception as e:
    print(e)