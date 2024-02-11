import os
from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video):
        self.__id_video = id_video
        self.video = self.youtube.videos().list(id=self.__id_video, part='snippet,statistics').execute()
        self.video_title = self.video['items'][0]['snippet']['title']
        self.video_url = self.video['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count = self.video['items'][0]['statistics']['viewCount']
        self.view_count = self.video['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_title


class PLVideo(Video):
    def __init__(self, id_video, id_plvideo):
        super().__init__(id_video)
        self.id_plvideo = id_plvideo
