from neo4j import GraphDatabase

# Connect to databse.
driver = GraphDatabase.driver("neo4j+ssc://f2137041.databases.neo4j.io",
                              auth=("neo4j", "K41pkgUv2aYfHzpczs1JSrpCVeR9BDCyBG9yodgzDmc"))

# Add new users


def add_user(tx, name):
    tx.run("CREATE (p:User { name: $name}) ", name=name)

# Add new resourse


def add_resources(tx, link, language, title):
    tx.run("CREATE (p:Resources { link: $link, language: $language, title:$title}) ",
           link=link, language=language, title=title)

# Add new comment


def add_comment(tx, id, person, content):
    tx.run(
        "MATCH (a:User), (m:Resources) WHERE a.name = $person AND id(m) = $id CREATE (a)-[:COMMENT {content: $content}]->(m) RETURN a, m", person=person, id=id, content=content)

# Add new rating


def add_rating(tx, rate):
    tx.run("CREATE (p:Rating { rate: $rate}) ", rate=rate)


# Add new comprehension level
def add_comprehension(tx, title, person, comprehension):
    tx.run(
        "MATCH (a:User), (m:Resources) WHERE a.name = $person AND m.title = $title CREATE (a)-[:COMPREHENSION {Comprehension: $comprehension}]->(m) RETURN a, m", person=person, title=title, comprehension=comprehension)

# Add new understanding level. (Should be pre-defined in the db when db is created)


def add_understanding_level(tx, level):
    tx.run("CREATE (p:Understanding_level { level: $level}) ", level=level)


def add_insight(tx, username, rating, understanding_level, comprehension, title):
    tx.run("MATCH (a:User), (m:Resources) WHERE a.name = $username AND m.title = $title CREATE (a)-[:INSIGHT {Understanding_level: $level, Usefulness: $rating, Comprehension: $comprehension}]->(m) RETURN a, m",
           username=username, title=title, comprehension=comprehension, rating=rating, level=understanding_level)


# Add new language. (Should be pre-defined in the db when db is created)
def add_language(tx, language):
    tx.run("CREATE (l:Language { language: $language}) ", language=language)

# Add new tag


def add_tag(tx, tag):
    tx.run("CREATE (t:Tag { tag: $tag}) ", tag=tag)

# Add new relationships


def create_relationship_ADD(tx, person, title):
    tx.run(
        "MATCH (a:User), (m:Resources) WHERE a.name = $person AND m.title = $title CREATE (a)-[:ADD]->(m) RETURN a, m", person=person, title=title)


def create_relationship_HAS(tx, person, title):
    tx.run(
        "MATCH (a:User), (m:Resources) WHERE a.name = $person AND m.title = $title CREATE (a)-[:HAS]->(m) RETURN a, m", person=person, title=title)


def create_relationship_RATE(tx, person, rate):
    tx.run(
        "MATCH (a:User), (m:Rating) WHERE a.name = $person AND m.rate = $rate CREATE (a)-[:RATE]->(m) RETURN a, m", person=person, rate=rate)


def create_relationship_RATE_DIRECTED_TO(tx, rate, title):
    tx.run(
        "MATCH (a:Rating), (m:Resources) WHERE a.rate = $rate AND m.title = $title CREATE (a)-[:DIRECTED]->(m) RETURN a, m", rate=rate, title=title)


def create_relationship_COMMENT(tx, person, content):
    tx.run(
        "MATCH (a:User), (m:Comment) WHERE a.name = $person AND m.content = $content CREATE (a)-[:COMMENT]->(m) RETURN a, m", person=person, content=content)


def create_relationship_COMMENT_DIRECTED_TO(tx, content, title):
    tx.run(
        "MATCH (a:Comment), (m:Resources) WHERE a.content = $content AND m.title = $title CREATE (a)-[:DIRECTED]->(m) RETURN a, m", content=content, title=title)


def create_relationship_LANGUAGE(tx, title, language):
    tx.run(
        "MATCH (l:Language), (r:Resources) WHERE l.language= $language AND r.title = $title CREATE (l)-[:LANGUAGE]->(r) RETURN r, l", title=title, language=language)


def create_relationship_TAGGED(tx, title, tag):
    tx.run(
        "MATCH (t:Tag), (r:Resources) WHERE t.tag= $tag AND r.title = $title CREATE (t)-[:TAGGED]->(r) RETURN r, t", title=title, tag=tag)


def create_relationship_LEVEL(tx, title, level):
    tx.run(
        "MATCH (l:Understanding_level), (r:Resources) WHERE l.level= $level AND r.title = $title CREATE (l)-[:LEVEL]->(r) RETURN r, l", title=title, level=level)

# Constraisn of the db. (Should be pre-defined in the db when db is created)


def create_constrain_person(tx):
    tx.run("CREATE CONSTRAINT ON (n:Person) ASSERT n.name IS UNIQUE")


def create_constrain_resources(tx):
    tx.run("CREATE CONSTRAINT ON (n:Resources) ASSERT n.title IS UNIQUE")

# Find a user in the db.


def find_user(tx, person):
    result = tx.run(
        "MATCH (n:User) WHERE n.name = $person RETURN n.name", person=person)
    return result.value()

# Find a resources in the db.


def find_resources(tx, title):
    result = tx.run(
        "MATCH (n:Resources) WHERE n.title = $title RETURN n.title", title=title)
    return result.value()

# Find a understanding level in the db.


def find_understanding_level(tx, level):
    result = tx.run(
        "MATCH (p:Understanding_level { level: $level}) RETURN p.level", level=level)
    return result.value()

# Find a language in the db.


def find_language(tx, language):
    result = tx.run(
        "MATCH (p:Language { language: $language}) RETURN p.language", language=language)
    return result.value()

# Find relationships in the db.


def find_relationship(tx, action=None, person=None, title=None, rate=0, content=None, language=None, tag=None, level=None):
    result = ''
    if action == 'HAS':
        result = tx.run(
            "MATCH (a:User), (m:Resources) WHERE a.name = $person AND m.title = $title MATCH (a)-[:HAS]->(m) RETURN a.name, m.title", person=person, title=title)
    elif action == 'RATE':
        result = tx.run(
            "MATCH (a:User), (m:Rating) WHERE a.name = $person AND m.rate = $rate MATCH (a)-[:RATE]->(m) RETURN a.name, m.rate", person=person, rate=rate)
    elif action == 'COMMENT':
        result = tx.run(
            "MATCH (a:User), (m:Comment) WHERE a.name = $person AND m.content = $content MATCH (a)-[:COMMENT]->(m) RETURN a.name, m.content", person=person, content=content)
    elif action == 'DIRECTED_COMMENT':
        result = tx.run(
            "MATCH (a:Comment), (m:Resources) WHERE a.content = $content AND m.title = $title MATCH (a)-[:DIRECTED]->(m) RETURN a.content, m.title", content=content, title=title)
    elif action == 'DIRECTED_RATE':
        result = tx.run(
            "MATCH (a:Rating), (m:Resources) WHERE a.rate = $rate AND m.title = $title MATCH (a)-[:DIRECTED]->(m) RETURN a.rate, m.title", rate=rate, title=title)
    elif action == 'LANGUAGE':
        result = tx.run(
            "MATCH (l:Language), (r:Resources) WHERE l.language= $language AND r.title = $title MATCH (l)-[:LANGUAGE]->(r) RETURN r.title, l.language", title=title, language=language)
    elif action == 'TAG':
        result = tx.run(
            "MATCH (t:Tag), (r:Resources) WHERE t.tag= $tag AND r.title = $title MATCH (t)-[:TAGGED]->(r) RETURN r.title, t.tag", title=title, tag=tag)
    elif action == 'LEVEL':
        result = tx.run(
            "MATCH (l:Understanding_level), (r:Resources) WHERE l.level= $level AND r.title = $title MATCH (l)-[:LEVEL]->(r) RETURN r.title, l.level", title=title, level=level)
    return result.value()

# Displays results relating to tags


def search(tx, language, level, tag):
    resources = []
    if len(tag) == 0:
        result = tx.run("MATCH (r:Resources)<-[:LANGUAGE]-(l:Language) "
                        "WHERE l.language= $language WITH r "
                        "MATCH (r:Resources)<-[i:INSIGHT]-(p:User) "
                        "WHERE i.Understanding_level = $level RETURN r AS resource", language=language, level=level)
        for i in result:
            add = True
            for j in resources:
                if (i["resource"].get("link") == j.get("link")):
                    add = False
            if (add == True):
                resources.append(i["resource"])
        return resources
    else:
        for a in tag:
            result = tx.run("MATCH (r:Resources)<-[:LANGUAGE]-(l:Language) "
                            "WHERE l.language= $language WITH r "
                            "MATCH (r:Resources)<-[i:INSIGHT]-(p:User) "
                            "WHERE i.Understanding_level = $level WITH r "
                            "MATCH (r:Resources)<-[:TAGGED]-(t:Tag) "
                            "WHERE t.tag CONTAINS $tag RETURN r AS resource", language=language, level=level, tag=a)
            for i in result:
                add = True
                for j in resources:
                    if (i["resource"].get("link") == j.get("link")):
                        add = False
                if (add == True):
                    resources.append(i["resource"])
        return resources

# returns the tags of a resource


def get_resource_from_id(session, id):
    results = session.run(
        "MATCH (r:Resources) where id(r) = $id RETURN r", id=id)
    return results.value()


def get_tags(tx, resource):
    results = tx.run(
        "MATCH (r:Resources {title: $resource}) <-[:TAGGED]-(tag) RETURN tag", resource=resource)
    return results.value()

# returns every "insight" relationship


def get_insight(tx, id, level):
    results = tx.run(
        "MATCH (p:User)-[a:INSIGHT {Understanding_level : $level}]->(r:Resources) WHERE id(r) = $id RETURN a", id=id, level=level)
    return results.value()


def get_comments(tx, id):
    results = tx.run(
        "MATCH (p:User)-[a:COMMENT]->(r:Resources) WHERE id(r) = $id RETURN a.content, p.name", id=id)
    return results.values()


''' TODO: add funtion to retrieve rating'''
''' TODO: add funtion to retrieve level'''

#-------------------------------------------------------------- Process API Request ---------------------------------------------------------------------------------#


def init_db(session):
    '''Add pre-defined language and understanding level to db at the start. 
    Also put constrains on some fields'''

    try:
        # Initialize constrains.
        session.read_transaction(create_constrain_person)
        session.read_transaction(create_constrain_resources)
    except:
        pass

    english = find_language(session, "English")
    french = find_language(session, "French")
    spanish = find_language(session, "Spanish")

    if len(english) == 0 and len(french) == 0 and len(spanish) == 0:
        # Initialize pre-defined language in the system.
        session.read_transaction(add_language, "French")
        session.read_transaction(add_language, "English")
        session.read_transaction(add_language, "Spanish")
        print('Language added to db')

    understand_level_1 = find_understanding_level(session, "Intermediate 1")
    understand_level_2 = find_understanding_level(session, "Intermediate 2")
    understand_level_3 = find_understanding_level(session, "Intermediate 3")

    if len(understand_level_1) == 0 and len(understand_level_2) == 0 and len(understand_level_3) == 0:
        # Initialize pre-defined understanding levle in teh system.
        session.read_transaction(add_understanding_level, "Intermediate 1")
        session.read_transaction(add_understanding_level, "Intermediate 2")
        session.read_transaction(add_understanding_level, "Intermediate 3")
        print('add_understanding_level added to db')


def check_in_db(tx, link):
    results = tx.run("MATCH (r:Resources{link: $link}) RETURN r", link=link)
    if len(results.value()) == 0:
        return False
    else:
        return True


def find_resourcesID_with_link(session, link):
    '''Process the add tag to resources request, check if the exact same tag has been directed to the same resources already.'''
    result = session.run(
        "MATCH (m:Resources) WHERE m.link = $link RETURN m", link=link).value()
    return result[0]


def process_add_user(session, username):
    '''Process the add user to db request, check if user already exist in the db'''
    user_exist_in_db = find_user(session, username)
    if len(user_exist_in_db) == 0:
        session.read_transaction(add_user, username)
        print("User " + username + " added to db.")

    else:
        print("User " + username + " already exist in databse.")


def process_add_resources_to_db(session, username, title, path, language):
    '''Process the add resources to db request, check if resources already exist in the db'''
    resources_exist_in_db = find_resources(session, title)
    if len(resources_exist_in_db) == 0:
        session.read_transaction(add_resources, path, language, title)
        session.read_transaction(create_relationship_ADD, username, title)
        print("Resources " + title + " added to db.")

    else:
        print("Resources " + title + " already exist in databse.")


def process_add_resources_to_own_repo(session, username, title):
    '''Process the add resources to repo request, check if resources already exist in the repo'''
    resources_exist_in_repo = find_relationship(
        tx=session, action="HAS", person=username, title=title)
    if len(resources_exist_in_repo) == 0:
        session.read_transaction(create_relationship_HAS, username, title)
        print("Resources " + title + " added to own repo.")

    else:
        print("Resources " + title + " already exist in repo.")


def process_display_repo(session, username):
    '''Process the add tag to resources request, check if the exact same tag has been directed to the same resources already.'''
    result = session.run(
        "MATCH (u:User{name: $username})-[a:HAS]->(r:Resources) RETURN r", username=username).value()
    return result


def process_comment(session, username, content, title):
    check_comment_in_db = session.run(
        "MATCH (p:User)-[a:COMMENT{content: $content}]->(r:Resources{title:$title}) RETURN p.name", content=content, title=title).value()
    if len(check_comment_in_db) == 0:

        session.read_transaction(add_comment, title, username, content)
    else:
        if check_comment_in_db[0] == username:
            print('You have already made that comment to the resources.')
        else:
            session.read_transaction(add_comment, title, username, content)


def process_add_insight(session, username, title, rate, comprehension, understanding_level):
    check_insight_in_db = session.run(
        "MATCH (p:User{name:$username})-[a:INSIGHT]->(r:Resources{title: $title}) RETURN a.Usefulness, a.Comprehension, a.Understanding_level", username=username, title=title).values()

    if len(check_insight_in_db) == 0:
        add_insight(session, username, rate,
                    understanding_level, comprehension, title)
    else:
        db_Usefulness = check_insight_in_db[0][0]
        db_Comprehension = check_insight_in_db[0][1]
        db_Understanding_level = check_insight_in_db[0][2]

        if db_Usefulness == rate and db_Comprehension == comprehension and db_Understanding_level == understanding_level:
            print('You have already made that insight to the resources.')
        if db_Usefulness != rate:
            session.run(
                "MATCH (:User {name: $username})-[insight:INSIGHT]-(:Resources {title: $title}) SET insight.Usefulness = $rate RETURN insight", username=username, title=title, rate=rate)
            print('changed made')
        if db_Comprehension != comprehension:
            session.run("MATCH (:User {name: $username})-[insight:INSIGHT]-(:Resources {title: $title}) SET insight.Comprehension = $comprehension RETURN insight",
                        username=username, title=title, comprehension=comprehension)
            print('changed made')
        if db_Understanding_level != understanding_level:
            session.run("MATCH (:User {name: $username})-[insight:INSIGHT]-(:Resources {title: $title}) SET insight.Understanding_level = $understanding_level RETURN insight",
                        username=username, title=title, understanding_level=understanding_level)
            print('changed made')


def process_assign_language(session, title, language):
    '''Process the add language to resources request, check if the exact same language has been directed to the same resources already.'''
    language_assign_to_re = find_relationship(
        tx=session, language=language, title=title, action='LANGUAGE')
    if len(language_assign_to_re) == 0:
        session.read_transaction(create_relationship_LANGUAGE, title, language)
    else:
        print('Language ' + language + ' already assigned to ' + title)


def process_add_tag(session, tag, title):
    '''Process the add tag to resources request, check if the exact same tag has been directed to the same resources already.'''
    tag_assign_to_re = find_relationship(
        tx=session, title=title, action='TAG', tag=tag)
    tag_already_exist = session.run(
        "MATCH (p:Tag{tag:$tag}) RETURN p.tag", tag=tag).value()
    if len(tag_assign_to_re) == 0:
        if len(tag_already_exist) > 0:
            session.read_transaction(create_relationship_TAGGED, title, tag)
            print('existing tag')
        else:
            session.read_transaction(add_tag, tag)
            session.read_transaction(create_relationship_TAGGED, title, tag)
            print('create new  tag')
    else:
        print('Tag ' + tag + ' already assigned to ' + title)


# Main loop to interact with db.
with driver.session() as session:

    # Only need to run once to initialize database
    # init_db(session)

    # process_add_user(session, "Jacky Kuang")
    # process_add_user(session, "Sandon Lai")
    # process_add_user(session, "Leon Wu")
    # process_add_user(session, "Jero Someone")

    # process_add_resources_to_db(session, "Jacky Kuang", '2 Hours of English Conversation Practice - Improve Speaking Skills', 'https://www.youtube.com/watch?v=NNamZZsggM4', "English")
    # process_add_resources_to_db(session, "Sandon Lai", 'The French Describe Their Weekend | Easy French 116', 'https://www.youtube.com/watch?v=unmu4yKfBg0', "French")

    # process_add_resources_to_own_repo(session, "Jacky Kuang", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # process_add_resources_to_own_repo(session, "Sandon Lai", 'The French Describe Their Weekend | Easy French 116')
    # process_add_resources_to_own_repo(session, "Sandon Lai", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # process_add_resources_to_own_repo(session, "Leon Wu", 'The French Describe Their Weekend | Easy French 116')
    # process_add_resources_to_own_repo(session, "Jero Someone", '2 Hours of English Conversation Practice - Improve Speaking Skills')

    # process_comment(session, "Jacky Kuang", "I love this video, I learned a lot of words from it.", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # process_comment(session, "Sandon Lai", "This video is not really for me, its too simple.", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # process_comment(session, "Jacky Kuang", "This video is not really for me, its too hard.", 'The French Describe Their Weekend | Easy French 116')
    # process_comment(session, "Leon Wu", "Great video", 'The French Describe Their Weekend | Easy French 116')

    # process_assign_language(session, '2 Hours of English Conversation Practice - Improve Speaking Skills', 'English')
    # process_assign_language(session, 'The French Describe Their Weekend | Easy French 116', 'French')

    # process_add_insight(session, "Leon Wu", 'The French Describe Their Weekend | Easy French 116', 3, 200, "Intermediate 3")

    # process_add_level(session, "Intermediate 1", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # process_add_level(session, "Intermediate 2", 'The French Describe Their Weekend | Easy French 116')

    # session.read_transaction(add_tag, "Native")

    tags = ["Native", "Funny", "Conversation"]
    resources = session.read_transaction(
        search, "French", "Intermediate 2", tags)

    for resource in resources:
        print(resource.get("title"))

    # print(session.read_transaction(get_comments, "The French Describe Their Weekend | Easy French 116"))

    # tags = session.read_transaction(get_tags, "The French Describe Their Weekend | Easy French 116")
    # for t in tags:
    #     print(t)

driver.close()
