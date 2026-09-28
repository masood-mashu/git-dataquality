"""
export_claude_code.py - Export GitDataQuality to Claude Code / MCP configuration.
"""
import os, json, yaml

def export_to_claude_code(root_dir):
    with open(os.path.join(root_dir, "agent.yaml"), "r", encoding="utf-8") as f:
        agent_meta = yaml.safe_load(f)
    with open(os.path.join(root_dir, "SOUL.md"), "r", encoding="utf-8") as sf:
        soul = sf.read()
    claude_md = f"# GitDataQuality Claude Code Instructions\n\n{soul}\n"
    cmd_file = os.path.join(root_dir, "exports", "claude_code", "CLAUDE.md")
    with open(cmd_file, "w", encoding="utf-8") as out:
        out.write(claude_md)
    mcp_cfg = {
        "mcpServers": {
            agent_meta.get("name"): {
                "command": "python",
                "args": ["-m", "tools"],
                "env": {"STANDARD": "OpenGAP-v0.1.0"}
            }
        }
    }
    mcp_file = os.path.join(root_dir, "exports", "claude_code", "claude_desktop_config.json")
    with open(mcp_file, "w", encoding="utf-8") as out:
        json.dump(mcp_cfg, out, indent=2)
    return {"visa": "Claude Code / MCP", "status": "PASSED", "output_files": [cmd_file, mcp_file]}
