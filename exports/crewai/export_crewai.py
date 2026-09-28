"""
export_crewai.py - Export GitDataQuality to CrewAI Agent configuration.
"""
import os, json, yaml

def export_to_crewai(root_dir):
    with open(os.path.join(root_dir, "agent.yaml"), "r", encoding="utf-8") as f:
        agent_meta = yaml.safe_load(f)
    with open(os.path.join(root_dir, "SOUL.md"), "r", encoding="utf-8") as sf:
        soul = sf.read()
    cfg = {
        "agent": {
            "role": "GitDataQuality Specialist",
            "goal": "Autonomous Data Pipeline Drift, Null Rate Threshold & Distribution Anomaly Sentry Agent",
            "backstory": soul,
            "verbose": True,
            "allow_delegation": False,
            "tools": agent_meta.get("tools", [])
        }
    }
    cfg_file = os.path.join(root_dir, "exports", "crewai", "crewai_agent_config.json")
    with open(cfg_file, "w", encoding="utf-8") as out:
        json.dump(cfg, out, indent=2)
    py_file = os.path.join(root_dir, "exports", "crewai", "crewai_agent.py")
    with open(py_file, "w", encoding="utf-8") as out:
        out.write("""from crewai import Agent\ndef create_agent():\n    return Agent(role='GitDataQuality', goal='Autonomous Data Pipeline Drift, Null Rate Threshold & Distribution Anomaly Sentry Agent', backstory='Autonomous agent', verbose=True)\n""")
    return {"visa": "CrewAI Framework", "status": "PASSED", "output_files": [cfg_file, py_file]}
