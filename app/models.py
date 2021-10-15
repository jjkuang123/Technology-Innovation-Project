from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j+s://f2137041.databases.neo4j.io", auth=("neo4j", "K41pkgUv2aYfHzpczs1JSrpCVeR9BDCyBG9yodgzDmc"))

# Add new users or new resourse
def add_user(tx, name):
    tx.run("CREATE (p:User { name: $name}) ", name=name)

def add_resources(tx, link, language, title):
    tx.run("CREATE (p:Resources { link: $link, language: $language, title:$title}) ", link=link, language=language, title=title)

def add_comment(tx, content):
    tx.run("CREATE (p:Comment { content: $content}) ", content=content)

def add_rating(tx, rate):
    tx.run("CREATE (p:Rating { rate: $rate}) ", rate=rate)

def add_understanding_level(tx, level):
    tx.run("CREATE (p:Understanding_level { level: $level}) ", level = level)

def add_language(tx, language):
    tx.run("CREATE (l:Language { language: $language}) ", language = language)

def add_tag(tx, tag):
    tx.run("CREATE (t:Tag { tag: $tag}) ", tag = tag)

def create_relationship_ADD(tx, person, title):
    tx.run("MATCH (a:User), (m:Resources) WHERE a.name = $person AND m.title = $title CREATE (a)-[:ADD]->(m) RETURN a, m", person=person, title=title)

def create_relationship_HAS(tx, person, title):
    tx.run("MATCH (a:User), (m:Resources) WHERE a.name = $person AND m.title = $title CREATE (a)-[:HAS]->(m) RETURN a, m", person=person, title=title)

def create_relationship_RATE(tx, person, rate):
    tx.run("MATCH (a:User), (m:Rating) WHERE a.name = $person AND m.rate = $rate CREATE (a)-[:RATE]->(m) RETURN a, m", person=person, rate=rate)

def create_relationship_RATE_DIRECTED_TO(tx, rate, title):
    tx.run("MATCH (a:Rating), (m:Resources) WHERE a.rate = $rate AND m.title = $title CREATE (a)-[:DIRECTED]->(m) RETURN a, m", rate=rate, title=title)

def create_relationship_COMMENT(tx, person, content):
    tx.run("MATCH (a:User), (m:Comment) WHERE a.name = $person AND m.content = $content CREATE (a)-[:COMMENT]->(m) RETURN a, m", person=person, content=content)

def create_relationship_COMMENT_DIRECTED_TO(tx, content, title):
    tx.run("MATCH (a:Comment), (m:Resources) WHERE a.content = $content AND m.title = $title CREATE (a)-[:DIRECTED]->(m) RETURN a, m", content=content, title=title)

def create_relationship_LANGUAGE(tx, title, language):
    tx.run("MATCH (l:Language), (r:Resources) WHERE l.language= $language AND r.title = $title CREATE (l)-[:LANGUAGE]->(r) RETURN r, l", title=title, language=language)

def create_relationship_TAGGED(tx, title, tag):
    tx.run("MATCH (t:Tag), (r:Resources) WHERE t.tag= $tag AND r.title = $title CREATE (t)-[:TAGGED]->(r) RETURN r, t", title=title, tag=tag)

def create_relationship_LEVEL(tx, title, level):
    tx.run("MATCH (l:Understanding_level), (r:Resources) WHERE l.level= $level AND r.title = $title CREATE (l)-[:LEVEL]->(r) RETURN r, l", title=title, level=level) 

def create_constrain_person(tx):
    tx.run("CREATE CONSTRAINT ON (n:Person) ASSERT n.name IS UNIQUE")

def create_constrain_resources(tx):
    tx.run("CREATE CONSTRAINT ON (n:Resources) ASSERT n.title IS UNIQUE")

def find_user(tx, person):
    result = tx.run("MATCH (n:User) WHERE n.name = $person RETURN n.name", person = person)
    return result.value()

def find_resources(tx, title):
    result = tx.run("MATCH (n:Resources) WHERE n.title = $title RETURN n.title", title = title)
    return result.value()


def find_relationship(tx, action=None, person=None, title=None, rate=0, content=None, language=None, tag=None, level=None):
    result = ''
    
    if action == 'HAS':
        result = tx.run("MATCH (a:User), (m:Resources) WHERE a.name = $person AND m.title = $title MATCH (a)-[:HAS]->(m) RETURN a.name, m.title", person=person, title=title)
    elif action == 'RATE':
        result = tx.run("MATCH (a:User), (m:Rating) WHERE a.name = $person AND m.rate = $rate MATCH (a)-[:RATE]->(m) RETURN a.name, m.rate", person=person, rate=rate)
    elif action == 'COMMENT':
        result = tx.run("MATCH (a:User), (m:Comment) WHERE a.name = $person AND m.content = $content MATCH (a)-[:COMMENT]->(m) RETURN a.name, m.content", person=person, content=content)
    elif action == 'DIRECTED_COMMENT':
        result = tx.run("MATCH (a:Comment), (m:Resources) WHERE a.content = $content AND m.title = $title MATCH (a)-[:DIRECTED]->(m) RETURN a.content, m.title", content=content, title=title)
    elif action == 'LANGUAGE':
        result = tx.run("MATCH (l:Language), (r:Resources) WHERE l.language= $language AND r.title = $title MATCH (l)-[:LANGUAGE]->(r) RETURN r.title, l.language", title=title, language=language)
    elif action == 'TAG':
        result = tx.run("MATCH (t:Tag), (r:Resources) WHERE t.tag= $tag AND r.title = $title MATCH (t)-[:TAGGED]->(r) RETURN r.title, t.tag", title=title, tag=tag)
    elif action == 'LEVEL':
        result = tx.run("MATCH (l:Understanding_level), (r:Resources) WHERE l.level= $level AND r.title = $title MATCH (l)-[:LEVEL]->(r) RETURN r.title, l.level", title=title, level=level) 
    return result.value()

def find_comment(tx, content):
    result = tx.run("MATCH (n:Comment) WHERE n.content = $content RETURN n.content", content = content)
    return result.value()


#-------------------------------------------------------------- Process API Request ---------------------------------------------------------------------------------#
def init_db(session):

    try:
        # Initialize constrains.
        session.read_transaction(create_constrain_person)
        session.read_transaction(create_constrain_resources)
    except:
        pass

    # Initialize pre-defined language in the system.
    session.read_transaction(add_language, "French")
    session.read_transaction(add_language, "English")
    session.read_transaction(add_language, "Spanish")

    # Initialize pre-defined rating in the system. 
    session.read_transaction(add_rating, 1)
    session.read_transaction(add_rating, 2)
    session.read_transaction(add_rating, 3)
    session.read_transaction(add_rating, 4)
    session.read_transaction(add_rating, 5)

    # Initialize pre-defined understanding levle in teh system. 
    session.read_transaction(add_understanding_level, "Intermediate 1")
    session.read_transaction(add_understanding_level, "Intermediate 2")
    session.read_transaction(add_understanding_level, "Intermediate 3")


def process_add_user(session, username):
    user_exist_in_db = find_user(session, username)
    if len(user_exist_in_db) == 0:
        session.read_transaction(add_user, username)
        print("User " + username + " added to db.")
        
    else:
        print("User " + username + " already exist in databse.")

def process_add_resources_to_db(session, username, title, path, language):
    resources_exist_in_db = find_resources(session, title)
    if len(resources_exist_in_db) == 0:
        session.read_transaction(add_resources, path, language, title)
        session.read_transaction(create_relationship_ADD, username, title)
        print("Resources " + title + " added to db.")
        
    else:
        print("Resources " + title + " already exist in databse.")
    
# find_relationship(tx, action=None, person=None, title=None, rate=0, content=None)
def process_add_resources_to_own_repo(session, username, title):
    resources_exist_in_repo = find_relationship(tx=session, action="HAS", person=username, title=title)
    if len(resources_exist_in_repo) == 0:
        session.read_transaction(create_relationship_HAS, username, title)
        print("Resources " + title + " added to own repo.")
        
    else:
        print("Resources " + title + " already exist in repo.")

def process_comment(session, username, content, title):
    comment_already_from_user = find_relationship(tx=session, action="COMMENT", person=username, title=title, content=content)
    already_directed_to_resources = find_relationship(tx=session, action="DIRECTED_COMMENT", person=username, title=title, content=content)
    

    if len(comment_already_from_user) == 0 and len(already_directed_to_resources) == 0:
        session.read_transaction(add_comment, content)
        session.read_transaction(create_relationship_COMMENT, username, content)
        session.read_transaction(create_relationship_COMMENT_DIRECTED_TO, content, title)
    else:
        print('You already made comment: ' + content + 'to resources: ' + title)

def process_rate(session, username, rate, title):
    session.read_transaction(create_relationship_RATE, username, rate)
    session.read_transaction(create_relationship_RATE_DIRECTED_TO, rate, title)

def process_assign_language(session, title, language):
    language_assign_to_re = find_relationship(tx=session, language=language, title=title, action='LANGUAGE')
    if len(language_assign_to_re) ==0:
        session.read_transaction(create_relationship_LANGUAGE, title, language)
    else:
        print('Language ' + language + ' already assigned to ' + title )

def process_add_tag(session, tag, title):
    tag_assign_to_re = find_relationship(tx=session, title=title, action='TAG', tag = tag)
    if len(tag_assign_to_re) ==0:
        session.read_transaction(add_tag, tag)
        session.read_transaction(create_relationship_TAGGED, title, tag)
    else:
        print('Tag ' + tag + ' already assigned to ' + title )

def process_add_level(session, level, title):
    level_assign_to_re = find_relationship(tx=session, title=title, action='LEVEL', level = level)
    if len(level_assign_to_re) ==0:
        session.read_transaction(create_relationship_LEVEL, title, level)
    else:
        print('Tag ' + level + ' already assigned to ' + title )



    
        
with driver.session() as session:

    # Only need to run once to initialize database
    init_db(session)
    
    process_add_user(session, "Jacky Kuang")
    process_add_user(session, "Sandon Lai")
    process_add_user(session, "Leon Wu")
    process_add_user(session, "Jero Someone")
    

    process_add_resources_to_db(session, "Jacky Kuang", '2 Hours of English Conversation Practice - Improve Speaking Skills', 'https://www.youtube.com/watch?v=NNamZZsggM4', "English")
    process_add_resources_to_db(session, "Sandon Lai", 'The French Describe Their Weekend | Easy French 116', 'https://www.youtube.com/watch?v=unmu4yKfBg0', "French")
    
    process_add_resources_to_own_repo(session, "Jacky Kuang", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    process_add_resources_to_own_repo(session, "Sandon Lai", 'The French Describe Their Weekend | Easy French 116')
    process_add_resources_to_own_repo(session, "Sandon Lai", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    process_add_resources_to_own_repo(session, "Leon Wu", 'The French Describe Their Weekend | Easy French 116')
    process_add_resources_to_own_repo(session, "Jero Someone", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    
    process_comment(session, "Jacky Kuang", "I love this video, I learned a lot of words from it.", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    process_comment(session, "Sandon Lai", "This video is not really for me, its too simple.", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    process_comment(session, "Jacky Kuang", "This video is not really for me, its too hard.", 'The French Describe Their Weekend | Easy French 116')
    process_comment(session, "Leon Wu", "Great video", 'The French Describe Their Weekend | Easy French 116')

    process_assign_language(session, '2 Hours of English Conversation Practice - Improve Speaking Skills', 'English')
    process_assign_language(session, 'The French Describe Their Weekend | Easy French 116', 'French')

    process_add_level(session, "Intermediate 1", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    process_add_level(session, "Intermediate 2", 'The French Describe Their Weekend | Easy French 116')
    


driver.close()


