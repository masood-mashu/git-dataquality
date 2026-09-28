"""
export_openai.py - Export GitDataQuality to OpenAI Assistants API format.
"""
import os, json, yaml

def export_to_openai(root_dir):
    with open(os.path.join(root_dir, "agent.yaml"), "r", encoding="utf-8") as f:
        agent_meta = yaml.safe_load(f)
    tools = []
    for t_name in agent_meta.get("tools", []):
        t_path = os.path.join(root_dir, "tools", f"{t_name}.yaml")
        if os.path.exists(t_path):
            with open(t_path, "r", encoding="utf-8") as tf:
                spec = yaml.safe_load(tf)
                tools.append({
                    "type": "function",
                    "function": {
                        "name": spec.get("name", t_name).replace("-", "_"),
                        "description": spec.get("description"),
                        "parameters": spec.get("input_schema", {"type": "object", "properties": {}})
                    }
                })
    with open(os.path.join(root_dir, "SOUL.md"), "r", encoding="utf-8") as sf:
        soul = sf.read()
    spec = {
        "name": agent_meta.get("name"),
        "description": agent_meta.get("description"),
        "model": "gpt-4o",
        "instructions": soul,
        "tools": tools,
        "metadata": {"standard": "OpenGAP-v0.1.0", "category": agent_meta.get("category")}
    }
    out_file = os.path.join(root_dir, "exports", "openai", "openai_assistant_spec.json")
    with open(out_file, "w", encoding="utf-8") as out:
        json.dump(spec, out, indent=2)
    return {"visa": "OpenAI SDK", "status": "PASSED", "output_file": out_file}
