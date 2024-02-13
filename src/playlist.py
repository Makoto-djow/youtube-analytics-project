import os
from googleapiclient.discovery import build
from datetime import datetime

from src.channel import Channel


class PlayList(Channel):
    """

    """

    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_playlist):
        """
        Инициализирует информацию о плейлисте
        """

        # id плейлиста
        self.__id_playlist = id_playlist

        # Выполняет запрос к API YouTube для получения информации о плейлисте
        self.playlist = self.youtube.playlistItems().list(playlistId=self.__id_playlist,part='contentDetails', maxResults=50,).execute()

        # Название плейлиста
        self.title = self.playlist['items'][0]['snippet']['title']

        # Ссылка на плейлист
        self.url = self.playlist['items'][0]['snippet']['thumbnails']['default']['url']

    # @property
    # def total_duration(self):

# {
#     "kind": "youtube#playlistItemListResponse",
#     "etag": "KIpfSYLFDUJIRlsFAHCKSo29f0c",
#     "items": [
#         {
#             "kind": "youtube#playlistItem",
#             "etag": "Poczykou137XQAuZSPleKLV8ZHc",
#             "id": "UEx2X3pPR0tLeFZwai1uMnFMa0VNMkhqOTZMTzZ1cWdRdy41NkI0NEY2RDEwNTU3Q0M2",
#             "contentDetails": {
#                 "videoId": "feg3DYywNys",
#                 "videoPublishedAt": "2023-04-03T14:24:45Z"
#             }
#         },
#         {
#             "kind": "youtube#playlistItem",
#             "etag": "gUwzWYM6VWIrrkmxKVcmdZL9bNE",
#             "id": "UEx2X3pPR0tLeFZwai1uMnFMa0VNMkhqOTZMTzZ1cWdRdy4yODlGNEE0NkRGMEEzMEQy",
#             "contentDetails": {
#                 "videoId": "MtWXwMCAApY",
#                 "videoPublishedAt": "2023-04-03T14:24:45Z"
#             }
#         },
#         {
#             "kind": "youtube#playlistItem",
#             "etag": "6LiN_MofK5nqaJ_Q0Zntke6U9N8",
#             "id": "UEx2X3pPR0tLeFZwai1uMnFMa0VNMkhqOTZMTzZ1cWdRdy4wMTcyMDhGQUE4NTIzM0Y5",
#             "contentDetails": {
#                 "videoId": "nApYYXYL9qA",
#                 "videoPublishedAt": "2023-04-03T14:24:45Z"
#             }
#         },
#         {
#             "kind": "youtube#playlistItem",
#             "etag": "btyHRnZF4Z8EYcNd-XVP1N97mek",
#             "id": "UEx2X3pPR0tLeFZwai1uMnFMa0VNMkhqOTZMTzZ1cWdRdy41MjE1MkI0OTQ2QzJGNzNG",
#             "contentDetails": {
#                 "videoId": "cUGyMzWQcGM",
#                 "videoPublishedAt": "2023-04-03T14:24:45Z"
#             }
#         }
#     ],
#     "pageInfo": {
#         "totalResults": 4,
#         "resultsPerPage": 50
#     }
# }