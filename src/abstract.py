import json
import os
from abc import ABC

from googleapiclient.discovery import build


class YouTubeAPI(ABC):

    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id):
        self.__id = id

