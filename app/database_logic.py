from app.models import *
from app.view_model import *


def search_function(query):
    resources = []

    q = decode_url(query)
    searchResult = q.searchResult
    level = q.level
    language = q.language

    print(searchResult)
    print(level)
    print(language)

    # Splits the tags by commas
    tag_array = searchResult.split(",")

    with driver.session() as session:
        db_resources = search(session, language, level, tag_array)
        for resource in db_resources:
            print(resource.get("title"))
            print(resource.get("link"))
            print(resource.get("language"))
            resources.append(Video(resource.get("id"), resource.get("link")))

    driver.close()

    return resources
