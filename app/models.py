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

# def print_friends(tx, name):
#     for record in tx.run("MATCH (a:Person) WHERE a.name STARTS WITH $name RETURN a", name=name): 
#         print(record.data())

# def update_birth_year(tx, name, year):
#     tx.run("MATCH (p:Person {name: $name}) SET p.born = $birth_date RETURN p", name=name, birth_date=year)


        
# def print_movie(tx, name):
#     for record in tx.run("MATCH (a:Movie) WHERE a.title STARTS WITH $name RETURN a", name=name): 
#         print(record.data())

# Use for add relationship
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







# Constrains for labels
def create_constrain_person(tx):
    tx.run("CREATE CONSTRAINT ON (n:Person) ASSERT n.name IS UNIQUE")

def create_constrain_resources(tx):
    tx.run("CREATE CONSTRAINT ON (n:Resources) ASSERT n.title IS UNIQUE")
    
        
with driver.session() as session:

    # Please do not run this again, already exist in database. 
    
    
    
    # session.read_transaction(add_user, "Arthur Kingman")
    # session.read_transaction(add_resources, 'https://www.youtube.com/watch?v=NNamZZsggM4', "English", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(create_relationship_ADD, "Arthur Kingman", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(create_relationship_HAS, "Arthur Kingman", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(add_comment, "I love this video, I learned a lot of words from it.")
    # session.read_transaction(create_relationship_COMMENT, "Arthur Kingman", "I love this video, I learned a lot of words from it.")
    # session.read_transaction(create_relationship_COMMENT_DIRECTED_TO, "I love this video, I learned a lot of words from it.", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(add_rating, 5)
    # session.read_transaction(create_relationship_RATE, "Arthur Kingman", 5)
    # session.read_transaction(create_relationship_RATE_DIRECTED_TO, 5, '2 Hours of English Conversation Practice - Improve Speaking Skills')


    # session.read_transaction(add_user, "Leon Wu")
    # session.read_transaction(create_relationship_HAS, "Leon Wu", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(add_comment, "This video is not really for me, its too simple.")
    # session.read_transaction(create_relationship_COMMENT, "Leon Wu", "This video is not really for me, its too simple.")
    # session.read_transaction(create_relationship_COMMENT_DIRECTED_TO, "This video is not really for me, its too simple.", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(add_rating, 1)
    # session.read_transaction(create_relationship_RATE, "Leon Wu", 1)
    # session.read_transaction(create_relationship_RATE_DIRECTED_TO, 1, '2 Hours of English Conversation Practice - Improve Speaking Skills')

    # session.read_transaction(add_user, "Sandon Lai")
    # session.read_transaction(add_resources, 'https://www.youtube.com/watch?v=unmu4yKfBg0', "French", 'The French Describe Their Weekend | Easy French 116')
    # session.read_transaction(create_relationship_ADD, "Sandon Lai", 'The French Describe Their Weekend | Easy French 116')
    # session.read_transaction(create_relationship_HAS, "Sandon Lai", 'The French Describe Their Weekend | Easy French 116')
    # session.read_transaction(add_comment, "This video is not really for me, its too hard.")
    # session.read_transaction(create_relationship_COMMENT, "Sandon Lai", "This video is not really for me, its too hard.")
    # session.read_transaction(create_relationship_COMMENT_DIRECTED_TO, "This video is not really for me, its too hard.", 'The French Describe Their Weekend | Easy French 116')
    # session.read_transaction(add_rating, 2)
    # session.read_transaction(create_relationship_RATE, "Sandon Lai", 2)
    # session.read_transaction(create_relationship_RATE_DIRECTED_TO, 2, 'The French Describe Their Weekend | Easy French 116')
    
    # session.read_transaction(add_user, "Jero Someone")
    # session.read_transaction(create_relationship_HAS, "Jero Someone", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(create_relationship_HAS, "Jero Someone", 'The French Describe Their Weekend | Easy French 116')

    # session.read_transaction(add_language, "French")

    # session.read_transaction(add_understanding_level, "Intermediate 1")
    # session.read_transaction(add_understanding_level, "Intermediate 2")
    # session.read_transaction(add_understanding_level, "Intermediate 3")

    # session.read_transaction(create_relationship_LANGUAGE, '2 Hours of English Conversation Practice - Improve Speaking Skills', 'French')
    # session.read_transaction(create_relationship_LANGUAGE, 'The French Describe Their Weekend | Easy French 116', 'French')

    # session.read_transaction(add_tag, "Native")

    # session.read_transaction(create_relationship_TAGGED, 'The French Describe Their Weekend | Easy French 116', 'Native')


driver.close()


