

class Resource():
    def __init__(self, id, link):
        self.id = id

    def get_understanding(self, level) -> int:
        # Logic for getting a rating based on a level
        return 78

    def get_usefulness(self, level) -> int:
        # Logic for getting a usefulness on a level
        return 3


class Video(Resource):
    def __init__(self, *args):
        super(Video, self).__init__(*args)
        self.thumbnail = None
        self.title = None

    def get_thumbnail(self):
        # Logic to set thumbnail if not in the database
        return '/static/images/testthumbnail.jpeg'

    def get_title(self):
        # Logic to get the title
        return "Comment Merkel a rate la transition ecologique del'Allemagne "
