import urllib.request
import json
import urllib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Resource():
    def __init__(self, id, link):
        self.id = id

    def get_understanding(self, level) -> int:
        # Logic for getting a rating based on a level
        return 78

    def get_usefulness(self, level) -> int:
        # Logic for getting a usefulness on a level
        return 3

    ## def get_user_tags() 

class Video(Resource):
    def __init__(self, *args):
        super(Video, self).__init__(*args)
        self.thumbnail = None
        self.title = None

    def get_thumbnail(self):
        # Logic to set thumbnail if not in the database
        # extract video_id
        video_id = '8nzRXxPnlPQ'
        return f'http://img.youtube.com/vi/{video_id}/maxresdefault.jpg'

    def get_title(self):
        # Logic to get the title

        # need to obtain video_id from the link or just replace the url with the video link
        video_id = "8nzRXxPnlPQ" 
        params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % video_id}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
        return data['title']