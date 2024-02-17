import os
import isodate
from googleapiclient.discovery import build
from datetime import timedelta


class PlayList:
    """

    """

    def __init__(self, id_playlist):
        """
        Инициализирует информацию о плейлисте
        """

        # id плейлиста
        self.__id_playlist = id_playlist
        self.playlist_videos = self.get_object_service().playlistItems().list(playlistId=self.__id_playlist,
                                                                              part='contentDetails, snippet',
                                                                              maxResults=50).execute()
        self.channel_id = self.playlist_videos['items'][0]['snippet']['channelId']
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.get_object_service().videos().list(part='contentDetails,statistics',
                                                                      id=','.join(self.video_ids)
                                                                      ).execute()

        self.title = self.get_playlist_title()
        self.url = f'https://www.youtube.com/playlist?list={self.__id_playlist}'

    @classmethod
    def get_object_service(cls):
        api_key = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    @property
    def total_duration(self):
        total = timedelta()
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total += duration

        return total

    def show_best_video(self):
        count = 0
        url = ''
        for video in self.video_response['items']:
            if int(video['statistics']['likeCount']) > count:
                count = int(video['statistics']['likeCount'])
                url = f'https://youtu.be/{video['id']}'

        return url

    def get_playlist_title(self):
        playlists = self.get_object_service().playlists().list(channelId=self.channel_id,
                                                               part='contentDetails,snippet',
                                                               maxResults=50).execute()
        for playlist in playlists['items']:
            if playlist['id'] == self.__id_playlist:
                return playlist['snippet']['title']
