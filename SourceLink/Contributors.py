# Imports
import os
import requests


class ContributorsGen:
    def __init__(self, save_route) -> None:
        self.app_key = 'AIzaSyDY8oHNM5qFxip9mSiVxMO3hsvNEO5cGjk'
        self.save_route = save_route
        self.videos_id = []



    def contributror_file(self, playlist: list):
        # Converting url.
        playlist_ids = []
        for complete_url in playlist:
            complete_url = complete_url.split('playlist?list=')[-1]
            playlist_ids.append(complete_url)

        for pl_id in playlist_ids:
            consult_len = requests.get(f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={pl_id}&key={self.app_key}').json()['pageInfo']['totalResults']

            if consult_len > 50:
                range_consults = list(range(0, consult_len, 51))
                next_page = ''

                for step in range(len(range_consults)):
                    req_playlist = requests.get(f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&pageToken={next_page}&playlistId={pl_id}&key={self.app_key}').json()

                    if 'nextPageToken' in list(req_playlist.keys()):
                        next_page = req_playlist['nextPageToken']
                    else:
                        next_page = ''

                    for id in req_playlist['items']:
                        self.videos_id.append(id['contentDetails']['videoId'])
                


            else:
                req_playlist = requests.get(f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={pl_id}&key={self.app_key}')
                
                playlist = req_playlist.json()['items']
                for id in playlist:
                    self.videos_id.append(id['contentDetails']['videoId'])


        file_text = 'Thanks to:\n\n'
        for id in self.videos_id:
            file_text = f'{file_text}- https://www.youtube.com/watch?v={id}\n'

        if os.path.isdir(self.save_route):
            with open(f'{self.save_route}/thanks to them!!.txt', 'w') as f:
                f.write(file_text)
            print('Archive of generated content sources/acknowledgements.')


        else:
            print('Your route is wrong.')
