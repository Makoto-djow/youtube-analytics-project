import os
from googleapiclient.discovery import build


class Video:
    """
    Класс для видео
    """

    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, id_video):
        """
        Инициализирует информацию о видео
        """

        # id видео
        self.__id_video = id_video

        # Выполняет запрос к API YouTube для получения информации о видео
        self.video = self.youtube.videos().list(id=self.__id_video, part='snippet,statistics').execute()

        # Название видео
        self.video_title = self.video['items'][0]['snippet']['title']

        # Ссылка на видео
        self.video_url = self.video['items'][0]['snippet']['thumbnails']['default']['url']

        # Количество просмотров видео
        self.view_count = self.video['items'][0]['statistics']['viewCount']

        # Количество лайков видео
        self.like_count = self.video['items'][0]['statistics']['likeCount']

    def __str__(self):
        """
        Возвращает название видео
        """

        return self.video_title


class PLVideo(Video):
    """
    Класс для плейлиста, наследуемый от класса Video
    """

    def __init__(self, id_video, id_player_video):
        """
        Инициализирует информацию о плейлисте
        """

        super().__init__(id_video)
        self.id_player_video = id_player_video
