# 🛡️ GhostDep

GhostDep is a lightweight **software supply chain security scanner** for Python (PyPI) and JavaScript (npm) ecosystems.

It helps detect:
- 🧠 Typosquatting packages
- ⚠️ Suspicious or malicious code patterns
- 📦 Dependency confusion risks
- 📉 Unusual or low-trust package metadata
- 🌐 Risks in GitHub repositories

---

## 🚀 Features

- 🔍 Scan local repositories
- 🌐 Scan GitHub repositories via URL
- 📦 Analyze individual packages (PyPI / npm)
- 🧬 Basic static code analysis for malicious patterns
- ⚖️ Risk scoring system (LOW / MEDIUM / HIGH)
- 🤖 GitHub Actions integration
- 📝 CLI-based tool for fast usage

---

## 📦 Supported ecosystems

- Python (PyPI)
- JavaScript (npm)

---

## 🧠 How it works

GhostDep analyzes packages using:

- Name similarity detection (typosquatting)
- Package registry metadata (PyPI / npm APIs)
- Static code inspection for suspicious patterns
- Basic heuristic-based risk scoring

---

## ⚙️ Installation

```bash
git clone https://github.com/DobreGabriel/Ghostdep-Scanner-Github.git
cd ghostdep

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pip install .
