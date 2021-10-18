from app.models import driver, search, process_add_resources_to_db
from app.models import process_add_insight, process_add_tag, process_assign_language
from app.view_model import decode_url, Resource, Video


def search_function(query):
    resources = []

    q = decode_url(query)
    searchResult = q.searchResult
    level = q.level
    language = q.language

    # Splits the tags by commas
    tag_array = searchResult.lower().replace(" ", "").split(",")

    with driver.session() as session:
        db_resources = search(session, language, level, tag_array)
        for resource in db_resources:
            print(resource.get("title"))
            print(resource.get("link"))
            print(resource.get("language"))
            print(resource.get('<id>'))

            # TODO: To get the id and replace with 25
            resources.append(Video(id=resource.id, link=resource.get("link")))

    driver.close()

    return resources


def add_function(username, language, like, understanding, level, tags, resource):
    title = resource.get_title()
    path = resource.link
    tags = tags.lower().replace(" ", "").split(",")

    with driver.session() as session:
        process_add_resources_to_db(session, username, title, path, language)
        process_add_insight(session, username, title,
                            like, understanding, level)
        process_assign_language(session, title, language)
        for tag in tags:
            process_add_tag(session, tag, title)
    driver.close()
