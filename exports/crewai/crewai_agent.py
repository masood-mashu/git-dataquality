from crewai import Agent
def create_agent():
    return Agent(role='GitDataQuality', goal='Autonomous Data Pipeline Drift, Null Rate Threshold & Distribution Anomaly Sentry Agent', backstory='Autonomous agent', verbose=True)
