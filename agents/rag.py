from agno.agent import Agent
from agno.models.openrouter import OpenRouter

from database.lancedb import knowledge
from utils.settings import settings


rag = Agent(
    name="RAG Agent",
    description="A simple agent that fetches data from a LanceDB vector store",
    instructions='''
        You will be given access to a pdf that has some information about AI. Your
        role is to understand the user's questions and answer them according to
        the information given to you by the PDF. Make sure you DO NOT invent information,
        just answer according to what is there in the PDF.
    ''',
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
    knowledge=knowledge, 
    search_knowledge=True
)