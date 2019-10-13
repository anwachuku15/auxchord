import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username from terminal
username = sys.argv[1]
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
# User ID: chuku9

# Erase cache and promt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']
followers = user['followers']['total']

while True:
    print()
    print('>>> Welcome to Spotipy ' + displayName + '!')
    print('>>> You have ' + str(followers) + ' followers.')
    print()
    print('0 - Search for an artist')
    print('1 - exit')
    print()
    choice = input("Your choice: ")

    # Search for the artist
    if choice == '0':
        print()
        searchQuery = input("Ok, what's their name? ")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery,1,0,'artist')


        # Artist Details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][3])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        # Album & Track Details
        trackURIs = []
        trackArt = []
        i = 0

        # Extract album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("ALBUM " + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print(str(i) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                i += 1
            print()
        # See album art
        while True:
            songSelection = input('Enter a song number to see its album art (press x to exit): ')
            if songSelection == "x":
                break
            webbrowser.open(trackArt[int(songSelection)])

    # End the program
    if choice == '1':
        break

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
