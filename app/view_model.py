import urllib.request
import json
import urllib
import ssl
import re
from flask import current_app
from app.models import *
ssl._create_default_https_context = ssl._create_unverified_context


def calculate_understanding(id, level):
    understandings = []
    lvl = f'Intermediate {level}'
    with driver.session() as session:
        db_resource = get_insight(session, id, lvl)
        for relationship in db_resource:
            understanding = relationship.get('Comprehension')

            understandings.append(int(understanding))

    return sum(understandings) / len(understandings)


def calculate_like(id, level):
    likes = []
    lvl = f'Intermediate {level}'
    with driver.session() as session:
        db_resource = get_insight(session, id, lvl)
        for relationship in db_resource:
            usefulness = relationship.get('Usefulness')
            likes.append(int(usefulness))

    return sum(likes) / len(likes)


def obtain_videoid(url):
    video_id = re.search(r"\?v=.*", url).group().split('?v=')[1]
    return video_id


class Resource():
    def __init__(self, link=None, id=None):
        self.id = id
        self.link = link

    def get_title(self) -> str:
        return ""

    def get_understanding(self, level) -> int:
        # Logic for getting a rating based on a level
        understanding = calculate_understanding(self.id, level)
        return understanding

    def get_like(self, level) -> int:
        # Logic for getting a usefulness on a level
        likes = calculate_like(self.id, level)
        return likes

    def get_link(self) -> str:
        return self.link

    # def get_user_tags()


class Video(Resource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.thumbnail = None
        self.title = None

    def get_thumbnail(self) -> str:
        # Logic to set thumbnail if not in the database
        # extract video_id
        video_id = obtain_videoid(self.link)
        return f'http://img.youtube.com/vi/{video_id}/maxresdefault.jpg'

    def get_title(self) -> str:
        # Logic to get the title

        # need to obtain video_id from the link or just replace the url with the video link
        video_id = obtain_videoid(self.link)
        params = {"format": "json",
                  "url": "https://www.youtube.com/watch?v=%s" % video_id}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
        return data['title']

    def get_id(self):
        if self.id:
            return self.id


class Query():
    def __init__(self, searchResult, level, language):
        self.searchResult = searchResult
        self.level = level
        self.language = language

    def encode_url(self, searchResult, level, language):
        return f"{searchResult}?&={level}?&={language}"

    def get_my_query(self):
        return self.encode_url(self.searchResult, self.level, self.language)

    @staticmethod
    def get_level(query):
        p1 = query.split('?&=')[1]
        p2 = p1.split(' ')[1]
        return p2


def decode_url(url):
    decoder = url.split("?&=")
    searchResult = decoder[0]
    level = decoder[1]
    language = decoder[2]

    return Query(searchResult, level, language)
