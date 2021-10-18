import urllib.request
import json
import urllib
import ssl
import re
from flask import current_app
ssl._create_default_https_context = ssl._create_unverified_context


def obtain_videoid(url):
    current_app.logger.info(url)
    regex_exp = r'(?:(?:http(?:s?):\/\/)|(?:www\.)|(?:http(?:s?):\/\/www\.))(?:youtu\.?be(?:\.com)?\/(?!oembed))(?:(?:watch\?v(?:=|%3D))|(?:v\/))?([a-z0-9_-]+)'
    video_id = re.match(regex_exp, url)
    return video_id


class Resource():
    def __init__(self, id, link):
        self.id = id
        self.link = link

    def get_understanding(self, level) -> int:
        # Logic for getting a rating based on a level
        return 78

    def get_like(self, level) -> int:
        # Logic for getting a usefulness on a level
        return 3

    # def get_user_tags()


class Video(Resource):
    def __init__(self, *args):
        super().__init__(*args)
        self.thumbnail = None
        self.title = None

    def get_thumbnail(self):
        # Logic to set thumbnail if not in the database
        # extract video_id
        video_id = obtain_videoid(self.link)
        print(video_id)
        return f'http://img.youtube.com/vi/{video_id}/maxresdefault.jpg'

    def get_title(self):
        # Logic to get the title

        # need to obtain video_id from the link or just replace the url with the video link
        video_id = "8nzRXxPnlPQ"
        params = {"format": "json",
                  "url": "https://www.youtube.com/watch?v=%s" % video_id}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
        return data['title']


class Query():
    def __init__(self, searchResult, level, language):
        self.searchResult = searchResult
        self.level = level
        self.language = language

    def encode_url(self, searchResult, level, language):
        return f"{searchResult}?&={level}?&={language}"

    # def decode_url(self, url):
    #     decoder = url.split("?&=")
    #     searchResult = decoder[0]
    #     level = decoder[1]
    #     language = decoder[2]

    #     return Query(searchResult, level, language)

    def get_my_query(self):
        return self.encode_url(self.searchResult, self.level, self.language)


def decode_url(url):
    decoder = url.split("?&=")
    searchResult = decoder[0]
    level = decoder[1]
    language = decoder[2]

    return Query(searchResult, level, language)
