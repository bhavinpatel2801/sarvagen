# SarvaGen – The Unified Generative AI System

A lightweight, CPU-friendly multimodal generative AI platform for text, image, audio, and document understanding and generation, integrating Model Context Protocol (MCP) and dynamic agent reasoning.

---

## Project Highlights

* **Multimodal Input:** Text, image, audio, and PDF document handling.
* **Dynamic Agent Reasoning:** Automatic tool invocation based on user queries.
* **Model Context Protocol (MCP):** Persistent memory and coherent long-form interactions.
* **Modular Pipeline:** Local-first design with optional cloud deployment (Azure, AWS, Databricks).
* **Interactive UI:** Streamlit app for rapid exploration and testing.
* **Observability & Logging:** Built-in metrics, tracing, and error alerts.

---

## Repository Layout

```plaintext
.
├── app/                # Streamlit UI and dashboards
├── core/               # Inference engine, memory manager, agent orchestrator
├── models/             # Model loader configurations (LLM, vision, audio)
├── data/               # Sample inputs, outputs, and test files
├── utils/              # Helper functions and routing logic
├── tests/              # Unit and integration tests
├── .github/            # CI/CD workflows and issue/PR templates
├── LICENSE             # MIT License
├── README.md           # Project overview and instructions
└── requirements.txt    # Project dependencies
```

---

## Libraries Used

* **streamlit** – UI deployment
* **transformers** – LLM loading and tokenization
* **sentence-transformers** – Embedding generation
* **faiss** – Vector index for semantic retrieval
* **pymupdf** – PDF text and image extraction
* **torch** – Model inference and fine-tuning
* **langchain** – Tool orchestration and agent chains
* **azure-storage-blob** – Ingestion from Azure Blob Storage
* **mlflow** – (Optional) experiment tracking
* **loguru** – Structured logging

---

## Quick Start (local, CPU‑only)

```bash
git clone https://github.com/your-username/sarvagen.git
cd sarvagen
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

streamlit run app/main.py
```

> **Note:** Supports CPU-only execution. Cloud deployment scripts for Docker/Kubernetes are available under `.github/workflows`.

---

## Usage Examples

```python
from sarvagen.core import SarvaGen

agent = SarvaGen(mcp_endpoint="https://your-mcp-endpoint")
response = agent.generate_text("Explain transformer architecture.")
print(response)
```