#!/usr/bin/env python
from crewship_quickstart.crew import CrewshipQuickstartCrew


def run():
    """Run the research crew."""
    inputs = {"topic": "AI agents in production"}
    CrewshipQuickstartCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
