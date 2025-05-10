# Neo4j client utility for ai_analytics_service
from neo4j import GraphDatabase
import os

class Neo4jClient:
    def __init__(self, uri=None, user=None, password=None):
        self.uri = uri or os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.user = user or os.getenv("NEO4J_USER", "neo4j")
        self.password = password or os.getenv("NEO4J_PASSWORD", "test")
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        self.driver.close()

    def create_entity_graph(self, entities, relationships=None):
        with self.driver.session() as session:
            for entity in entities:
                session.run(
                    "MERGE (e:%s {value: $value})" % entity["type"],
                    value=entity["value"]
                )
            # Relationships logic can be added here