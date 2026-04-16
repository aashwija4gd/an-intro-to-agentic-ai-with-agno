from agno.agent import Agent
from agno.models.openrouter import OpenRouter

from utils.settings import settings
from models.chatbot_model import ChatbotModel
from agno.db.in_memory import InMemoryDb


db = InMemoryDb()

chatbot = Agent(
    name="Chatbot Agent",
    description="A chatbot system backed by user session memory",
    # instructions='''
    #     You are an expert chat assistant. Your goal is to assist the
    #     user with any and all questions that they have. Make sure to
    #     keep your responses professional and precise. Do not provide
    #     more information than what is asked. Also ensure that you are
    #     polite and respectful in your tone, even when disagreeing.
    # ''',
    instructions='''
        You are a dedicated AI chat assistant. Your goal is to assist
        the human user with any and every question that they may ask you. Your responses
        must be polite, concise, and professionally precise. Keep your answers limited to 
        what has been asked from you. Ensure that your tone is always respectful, even
        if the user uses harsh language or is impolite or if you disagree with them.
    ''',
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
    output_schema=ChatbotModel,
    db=db,
    update_memory_on_run=True
)