import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        # id канала
        self.__channel_id = channel_id

        # Выполняет запрос к API YouTube для получения информации о канале
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        # Название канала
        self.title = self.channel['items'][0]['snippet']['title']

        # Описание канала
        self.description = self.channel['items'][0]['snippet']['description']

        # Ссылка на канал
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']

        # Количество подписчиков
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']

        # Количество видео
        self.video_count = self.channel['items'][0]['statistics']['videoCount']

        # Общее количество просмотров
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.channel, indent=4, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Класс-метод, возвращающий объект для работы с YouTube API
        """

        youtube = build('youtube', 'v3', developerKey=cls.api_key)
        return youtube

    def to_json(self, file):
        """
        Метод, сохраняющий в файл значения атрибутов экземпляра Channel
        """

        attribute_values = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(attribute_values, f, indent=4, ensure_ascii=False)
