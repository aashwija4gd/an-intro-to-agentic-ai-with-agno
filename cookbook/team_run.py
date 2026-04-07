from agents.team import content_team

def run_team_workflow():
    response = content_team.run(
        input="Write a short article about the benefits of drinking water"
    )
    print(response.content)

run_team_workflow()
