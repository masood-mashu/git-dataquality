# GitDataQuality (git-dataquality) 🛡️

[![OpenGAP Standard](https://img.shields.io/badge/OpenGAP-v0.1.0-blue.svg)](https://github.com/open-gitagent/opengap)
[![Category](https://img.shields.io/badge/Category-Data%20%26%20analytics-success.svg)](https://hidevs.com)
[![Visas](https://img.shields.io/badge/Visas-4%2F4%20Earned-brightgreen.svg)](#framework-visas)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

**GitDataQuality** is an OpenGAP-compliant, autonomous autonomous data pipeline drift, null rate threshold & distribution anomaly sentry agent.

---

## 🏛️ Architecture & OpenGAP Compliance
- `agent.yaml`: Canonical OpenGAP specification manifest.
- `SOUL.md`: Identity, operational boundaries, and audit trail requirements.
- `DUTIES.md`: Explicit separation of duties (Maker vs. Checker).
- `RULES.md`: Zero-tolerance compliance rules and constraints.
- `AGENTS.md`: Multi-agent team workflow and orchestration instructions.
- `EXPLAINABILITY.md`: Detailed auditability, decision logic, and boundary documentation.
- `tools/`: Deterministic execution tools with strict schemas.
- `skills/`: Standardized procedural workflows.
- `exports/`: Multi-framework portability adapters across OpenAI, CrewAI, Claude Code, and Lyzr.

---

## 🎯 Framework Visas
Certified portable across System Prompt, Claude Code, OpenAI SDK, CrewAI, and Lyzr ecosystems.

---

## 🧪 Testing & Verification
```bash
python tests/eval_predictability.py
python exports/run_all_exports.py
npx @open-gitagent/opengap validate
python demo.py
```

---

## 📄 License
Apache License 2.0. See [LICENSE](LICENSE) for details.
