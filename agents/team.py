from agno.agent import Agent
from agno.team import Team
from agno.models.openrouter import OpenRouter

from utils.settings import settings
from models.team_model import TeamModel


writer = Agent(
    name="Writer Agent",
    description="A content writer that drafts articles on any given topic",
    instructions="""
        You are a skilled content writer. When given a topic, write a concise,
        well-structured draft covering the key points. Keep it factual, clear,
        and engaging. Aim for 2-3 short paragraphs.
    """,
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
)

reviewer = Agent(
    name="Reviewer Agent",
    description="A content reviewer that critiques drafts and suggests improvements",
    instructions="""
        You are a sharp content reviewer. When given a draft, assess its clarity,
        accuracy, and structure. Provide concise, actionable feedback on what works
        well and what could be improved. Be constructive and specific.
    """,
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
)

content_team = Team(
    name="Content Team",
    description="A two-agent team that drafts and reviews content on any topic",
    mode="coordinate",
    model=OpenRouter(
        id="google/gemini-2.5-flash",
        api_key=settings.OPENROUTER_API_KEY
    ),
    members=[writer, reviewer],
    instructions="""
        You are the orchestrator of a content creation team. When given a topic:
        1. Ask the Writer Agent to produce a draft on that topic.
        2. Pass the draft to the Reviewer Agent for feedback.
        3. Synthesize the draft and review into a final structured output.

        Make sure to follow the following schema while returning the final response
        topic: str
        draft: str
        review: str
        final_output: str
    """,
    output_schema=TeamModel,
)
