from agno.knowledge.embedder.fastembed import FastEmbedEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb

vector_db = LanceDb(
    table_name="pdf_documents",
    uri="/tmp/lancedb",
    embedder=FastEmbedEmbedder(),
)

knowledge = Knowledge(vector_db=vector_db)
knowledge.insert(path="samples/A Brief Introduction to Artificial Intelligence - A_Brief_Introduction_To_AI.pdf")
