from flask.globals import current_app
from app.models import driver, search, process_add_resources_to_db
from app.models import process_add_insight, process_add_tag, process_assign_language, process_add_resources_to_own_repo
from app.models import process_display_repo, get_resource_from_id
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
            resources.append(Video(id=resource.id, link=resource.get("link")))

    driver.close()

    return resources


def add_function(username, language, like, understanding, level, tags, resource):
    title = resource.get_title()
    path = resource.link
    tags = tags.lower().replace(" ", "").split(",")

    current_app.logger.info(language)
    print(language)

    with driver.session() as session:
        process_add_resources_to_db(session, username, title, path, language)

        process_add_insight(session, username, title,
                            like, understanding, level)

        process_assign_language(session, title, language)
        for tag in tags:
            process_add_tag(session, tag, title)

        process_add_resources_to_own_repo(session, username, title)

    driver.close()


def add_single_resource(username, resource_id):
    with driver.session() as session:
        db_resource = get_resource_from_id(session, int(resource_id))
        for resource in db_resource:
            resource = Video(id=resource.id, link=resource.get("link"))
            print(resource)
            process_add_resources_to_own_repo(
                session, username, resource.get_title())

    driver.close()


def obtain_user_resources(username):
    resources = []
    with driver.session() as session:
        db_resources = process_display_repo(session, username)

        for resource in db_resources:
            print(resource.get("title"))
            print(resource.get("link"))
            print(resource.get("language"))
            resources.append(Video(id=resource.id, link=resource.get("link")))

    driver.close()
    return resources
