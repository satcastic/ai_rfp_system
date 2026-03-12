# AI_RFPS_SYSTEM
# Multi-Agent AI System
A modular AI system where multiple specialized agents collaborate to analyze documents and generate solutions for complex problem statements.

## 🎯 Features

* **Multi-Agent Architecture**: The system simulates multiple AI agents (e.g., Sales Agent, Solution Agent, Analysis Agent) that collaborate to process information and generate structured outputs.

* **Document Processing**: Supports reading and analyzing uploaded documents such as PDFs and text files to extract useful insights.

* **Local LLM Integration**: Uses **Ollama** to run large language models locally, enabling AI-powered reasoning without relying on external APIs.

* **Interactive Interface**: A simple **Streamlit web interface** allows users to interact with the agents and test the workflow.

* **Modular Design**: Each agent operates as a separate module, making the system easy to extend with additional agents or capabilities.

* **Logic**: The system follows a sequential multi-agent workflow where the **Sales Agent interprets requirements, the Solution Agent proposes solutions, and the Analysis Agent processes documents and refines the output**.

---

## 💻 Technologies Used

* **Language**: Python

* **Libraries / Frameworks**
  * Streamlit
  * Ollama
  * LlamaIndex
  * ChromaDB
  * Pandas
  * NumPy
  * Sentence Transformers
  * PDF parsing libraries (pypdf / pdfplumber)

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

* Python **3.10 or higher**
* **Ollama** installed and running locally  
  https://ollama.com

You may also need to pull a model such as:

```bash
ollama run llama3
git clone https://github.com/satcastic/AI_RFPS_SYSTEM.git
cd ai_rfp_system
pip install -r requirements.txt

#run using streamlit
streamlit run app.py
# after running open browser at 
#http://localhost:8501 
```
AI_RFP_SYSTEM/
│
├── agents/          # AI agents responsible for different tasks
├── ingestion/       # Document parsing
├── retrieval/       # RAG index creation and querying
├── orchestrator/    # Multi-agent workflow controller
├── utils/           # Helper utilities (PDF generation etc.)
├── data/            # Machine catalog and cost data
├── test_documents/  # Sample RFP documents
│
├── app.py           # Streamlit UI
├── requirements.txt
└── README.md
