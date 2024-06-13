#vector.py
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from graph.integrations.llm import embeddings

neo4jvector = Neo4jVector.from_existing_index(
    embeddings,
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
    index_name="product_index_new",
    node_label="product",
    text_node_property="notes",
    embedding_node_property="embedding",
    retrieval_query="""
        RETURN
            node.notes AS text,
            score,
            {
                name: node.name,
                notes: node.notes,
                related_nodes: [
                    (node)-[r]-(relatedNode) | 
                    {
                        name: relatedNode.name, 
                        notes: relatedNode.notes,
                        relationship: type(r)
                    }
                ]
            } AS metadata
    """
)

def vector(query):
    # Perform similarity search using Neo4j vector index
    docs = neo4jvector.similarity_search(query, k=3)
    # Extract the relevant information from the retrieved document
    #if docs:
    #    doc = docs[0]
    #    result = f"Name: {doc.metadata['name']}\nNotes: {doc.metadata['notes']}"
    #else:
    #    result = "No relevant information found in the database."
    
    return {"result": docs}
