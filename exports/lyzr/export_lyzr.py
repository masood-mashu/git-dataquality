"""
export_lyzr.py - Export GitDataQuality to Lyzr ecosystem agent specification.
"""
import os, json, yaml

def export_to_lyzr(root_dir):
    with open(os.path.join(root_dir, "agent.yaml"), "r", encoding="utf-8") as f:
        agent_meta = yaml.safe_load(f)
    with open(os.path.join(root_dir, "SOUL.md"), "r", encoding="utf-8") as sf:
        soul = sf.read()
    lyzr_cfg = {
        "agent_name": agent_meta.get("name"),
        "agent_role": "GitDataQuality",
        "agent_description": agent_meta.get("description"),
        "persona": soul,
        "instructions": "Execute policy evaluation and compliance verification.",
        "tools": agent_meta.get("tools", []),
        "framework": "lyzr-agent-api",
        "version": "1.0.0",
        "parameters": {"temperature": 0.0, "max_tokens": 2048, "deterministic_execution": True},
        "metadata": {"standard": "GitAgent-OpenGAP", "visa_category": "Lyzr-Native"}
    }
    cfg_file = os.path.join(root_dir, "exports", "lyzr", "lyzr_agent_config.json")
    with open(cfg_file, "w", encoding="utf-8") as out:
        json.dump(lyzr_cfg, out, indent=2)
    return {"visa": "Lyzr Ecosystem", "status": "PASSED", "output_file": cfg_file}
