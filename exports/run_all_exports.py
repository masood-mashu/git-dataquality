"""
run_all_exports.py - Master exporter and Foundation Visa verification harness for git-dataquality.
"""
import os, sys, json, importlib.util
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    exp = os.path.join(root, "exports")
    results = []
    
    # 1. OpenAI
    m1 = load_mod("m1", os.path.join(exp, "openai", "export_openai.py"))
    results.append(m1.export_to_openai(root))
    
    # 2. CrewAI
    m2 = load_mod("m2", os.path.join(exp, "crewai", "export_crewai.py"))
    results.append(m2.export_to_crewai(root))
    
    # 3. Claude Code
    m3 = load_mod("m3", os.path.join(exp, "claude_code", "export_claude_code.py"))
    results.append(m3.export_to_claude_code(root))
    
    # 4. Lyzr
    m4 = load_mod("m4", os.path.join(exp, "lyzr", "export_lyzr.py"))
    results.append(m4.export_to_lyzr(root))
    
    print(f"PASSPORT STATUS (git-dataquality): {len(results)}/4 VISAS ISSUED | +{len(results)*100} POINTS")
    with open(os.path.join(exp, "visa_manifest.json"), "w", encoding="utf-8") as rf:
        json.dump({"agent": "git-dataquality", "visas_earned": len(results), "visas": results}, rf, indent=2)

if __name__ == "__main__":
    main()
