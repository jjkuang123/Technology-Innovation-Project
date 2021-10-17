from app.models import *
from app.view_model import * 

def search_function(query):
    q = decode_url(query)
    searchResult = q.searchResult
    level = q.level
    language = q.language

    # Splits the tags by commas
    tag_array = searchResult.split(",")

    with driver.session() as session:

        resources = search(session, language, level, tag_array)
        for resource in resources: 
            print(resource.get("title"))

    driver.close()

    

