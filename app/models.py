from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j+s://f2137041.databases.neo4j.io", auth=("neo4j", "K41pkgUv2aYfHzpczs1JSrpCVeR9BDCyBG9yodgzDmc"))

# Add new users or new resourse
def add_user(tx, name):
    tx.run("CREATE (p:Person { name: $name}) ", name=name)

def add_resourse(tx, link, language, title):
    tx.run("CREATE (p:Resourse { link: $link, language: $language, title:$title}) ", link=link, language=language, title=title)

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
    tx.run("MATCH (a:Person), (m:Resourse) WHERE a.name = $person AND m.title = $title CREATE (a)-[:ADD]->(m) RETURN a, m", person=person, title=title)

def create_relationship_RATE(tx, person, title):
    tx.run("MATCH (a:Person), (m:Resourse) WHERE a.name = $person AND m.title = $title CREATE (a)-[:RATE]->(m) RETURN a, m", person=person, title=title)

def create_relationship_COMMENT(tx, person, title):
    tx.run("MATCH (a:Person), (m:Resourse) WHERE a.name = $person AND m.title = $title CREATE (a)-[:COMMENT]->(m) RETURN a, m", person=person, title=title)

def create_relationship_HAS(tx, person, title):
    tx.run("MATCH (a:Person), (m:Resourse) WHERE a.name = $person AND m.title = $title CREATE (a)-[:HAS]->(m) RETURN a, m", person=person, title=title)

# Constrains for labels
def create_constrain_person(tx):
    tx.run("CREATE CONSTRAINT ON (n:Person) ASSERT n.name IS UNIQUE")

def create_constrain_resources(tx):
    tx.run("CREATE CONSTRAINT ON (n:Resourse) ASSERT n.title IS UNIQUE")
    
        
with driver.session() as session:

    # Please do not run this again, already exist in database. 
    # session.read_transaction(create_relationship_ADD, "Arthur Kingman", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(create_relationship_RATE, "Arthur Kingman", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(create_relationship_COMMENT, "Arthur Kingman", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    # session.read_transaction(create_relationship_HAS, "Arthur Kingman", '2 Hours of English Conversation Practice - Improve Speaking Skills')
    



driver.close()


