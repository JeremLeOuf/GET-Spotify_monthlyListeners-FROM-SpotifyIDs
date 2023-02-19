# Import the libraries used:
import pandas as pd
import requests
import time
from datetime import date
from tkinter import filedialog as fd
import os


# Configure Soundcharts Sandbox credentials:
endpoint = "https://sandbox.api.soundcharts.com/api/v2" # Soundchart's Sandbox API URL
headers = { # Sets connection headers for Soundcharts endpoint
    "x-app-id" : 'soundcharts',
    "x-api-key" : 'soundcharts'
}

test_spotify_ids = ['6qqNVTkY8uBg9cP3Jd7DAH', '2NjfBq1NflQcKSeiDooVjY'] # Sandbox sample of SpotifyID artists (Billie Eilish, Tones & I)


# Filedialog module makes user choose `spotify_ids.csv` file:
try:
    spotify_ids_list = fd.askopenfilename(initialdir='input') # Opens popup to select file
    df = pd.read_csv(f'input/{os.path.split(spotify_ids_list)[1]}') # Returns a DataFrame from the `spotify_ids_list` variable created above
    print(f'File chosen: {os.path.split(spotify_ids_list)[1]}.\n') # Prints the file chosen
    print(f'File looks like:\n{df.head()}\n\n') # Prints the first rows of the `csv` DataFrame
except Exception as e: # Basic exception handling
    print(e)
    

# Define functions:    
def getSoundchartsUUID(spotify_id): # Returns `soundcharts_uuid` (11e81bcc-9c1c-ce38-b96b-a0369fe50396 [Billie Eilish]) as a string from the given `spotify_id`
    response = requests.get(f"{endpoint}/artist/by-platform/spotify/{spotify_id}", headers=headers) # Calls Soundchart's API
    json = response.json() # Turns it to JSON file for better readability
    return json['object']['uuid'] if response.status_code == 200 else f'Error. Response: {response.status_code}' # Returns `soundcharts_uuid` if successful, else return response code (for debug)


def getArtistName(spotify_id): # Returns `artist_name`'s slug [billie-eilish] as a string from the given `spotify_id`
    uuid = getSoundchartsUUID(spotify_id) # Gets the Soundcharts UUID from the Spotify ID
    response = requests.get(f"{endpoint}/artist/{uuid}", headers = headers) # Calls Soundchart's API
    json = response.json() # Turns it to JSON file for better readability
    return json["object"]["slug"] if response.status_code == 200 else f'Error. Response: {response.status_code}' # Returns `artist_name` if successful, else return response code (for debug)

def getMonthlyListeners(spotify_id): # Returns (spotify) `monthly_listeners` [1293871] as a string from the given `spotify_id`
    uuid = getSoundchartsUUID(spotify_id) # Gets the Soundcharts UUID from the Spotify ID
    response = requests.get(f"{endpoint}/artist/{uuid}/streaming/spotify/listeners", headers = headers) # Calls Soundchart's API
    json = response.json() # Turns it to JSON file for better readability
    return json['items'][0]['value'] if response.status_code == 200 else f'Error. Response: {response.status_code}' # Returns `monthly_listeners` if successful, else return response code (for debug)


# Loops through all `spotifyIDs` and appends the outputs in the `artist_names` and `monthly_listeners` lists
output_df = pd.DataFrame(columns=['artist_name', 'monthly_listeners']) # Prepares empty `output_df` DataFrame
artist_names, monthly_listeners = [], [] # Initiates empty lists

for id in test_spotify_ids: # Fills `artist_name` and `monthly_listeners` lists with `artist_name` and `monthly_listeners` rows
    artist_names.append(getArtistName(id)), monthly_listeners.append(getMonthlyListeners(id))
    

# Formats the DataFrame from the above lists:
try:
    output_df['artist_name'], output_df['monthly_listeners'] = artist_names, monthly_listeners # Sends the lists created above to the relevant DataFrame columns
    print(f'Output DataFrame looks like: \n{output_df}\n') # If successful, prints correct DataFrame, then prints success message
except Exception as e: # Basic exception handling
    print(e) # Else, prints Exception and stops
time.sleep(2)


# Prints it to 'output/amuzed/{filename}.csv'
try:
    output_df.to_csv(f'output/results-{date.today()}.csv', index=False) # Prints to 'output/amuzed/{filename}.csv
    print(f"File successfully saved to 'output/results-{date.today()}.csv!\nExiting now.") # Confirmation message
except Exception as e: # Basic exception handling
    print(e)
