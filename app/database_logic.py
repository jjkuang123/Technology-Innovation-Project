from flask.globals import current_app
from app.models import add_comment, check_in_db, driver, find_resourcesID_with_link, get_comments, search, process_add_resources_to_db
from app.models import process_add_insight, process_add_tag, process_assign_language, process_add_resources_to_own_repo
from app.models import process_display_repo, get_resource_from_id, get_insight
from app.models import process_add_insight
from app.view_model import decode_url, Video


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


def obtain_resource_object(resource_id):
    with driver.session() as session:
        db_resource = get_resource_from_id(session, int(resource_id))
        for resource in db_resource:
            resource = Video(id=resource.id, link=resource.get("link"))
            print(f"OBTAIN_RESOURCE_OBJECT {resource}")

    driver.close()
    return resource


def calculate_understanding(id, level):
    understandings = []
    lvl = f'Intermediate {level}'
    with driver.session() as session:
        db_resource = get_insight(session, id, lvl)
        for relationship in db_resource:
            understanding = relationship.get('Comprehension')
            understandings.append(int(understanding))
    return sum(understandings) / len(understandings)


def obtain_resource_rating(link, level):
    with driver.session() as session:
        if check_in_db(session, link):
            # obtain id of resource from the db
            id = find_resourcesID_with_link(session, link).id
            print(id)
            return calculate_understanding(id, level)
        else:
            return None


def update_like_understanding(id, new_understanding, new_like, username, level):
    lvl = f'Intermediate {level}'
    with driver.session() as session:
        process_add_insight(session, username, id, new_like,
                            new_understanding, lvl)


def obtain_comments(id):
    with driver.session() as session:
        comments = get_comments(session, int(id))
        current_app.logger.info(type(comments))
        current_app.logger.info(comments)
    return comments


def post_comments(comment, user, id):
    with driver.session() as session:
        add_comment(session, id, user, comment)
    driver.close()
