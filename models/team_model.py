from pydantic import BaseModel

class TeamModel(BaseModel):
    topic: str
    draft: str
    review: str
    final_output: str
