from soundcloud import playlist

playlist_keys = playlist.keys()
time_in_milliseconds = 0
number_of_tracks = 0

for playlist in playlist['tracks']:
    # print(playlist)

    time_in_milliseconds += playlist['duration_in_milliseconds']
    number_of_tracks += 1

        
print(f'{time_in_milliseconds} milliseconds')

print(f'{number_of_tracks} tracks')
