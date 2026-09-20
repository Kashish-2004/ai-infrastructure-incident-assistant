# AI Infrastructure Incident Assistant

An AI-powered system that monitors infrastructure health, retrieves relevant troubleshooting knowledge, and generates evidence-backed incident recommendations through a FastAPI backend.

## Features

- Real-time monitoring of CPU, memory, and disk usage
- REST API built with FastAPI
- Pydantic-based request and response validation
- RAG-based retrieval from infrastructure troubleshooting runbooks
- Semantic similarity search using sentence embeddings
- LLM-powered incident analysis and recommendations
- Rule-based tool routing for system diagnostics
- Application logging for incident workflow tracing
- Human approval required before destructive remediation
- GitHub Actions CI for automated Python validation
- Dockerfile for containerized deployment

## Architecture

The incident analysis workflow follows this pipeline:

```text
User Incident
      ↓
FastAPI `/incident` endpoint
      ↓
Agentic Decision Layer
      ↓
System Monitoring Tool ──────┐
      ↓                      │
RAG Retrieval                │
      ↓                      │
Relevant Knowledge           │
      ↓                      │
LLM Analysis ←───────────────┘
      ↓
Incident Recommendation
      ↓
Human Approval Required
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application and automation logic |
| FastAPI | REST API framework |
| Pydantic | Request and response validation |
| psutil | System resource monitoring |
| Sentence Transformers | Generating text embeddings |
| NumPy | Vector operations and cosine similarity |
| Groq | LLM inference |
| python-dotenv | Loading environment variables |
| Docker | Containerization configuration |
| Git & GitHub | Version control and source hosting |
| GitHub Actions | Continuous Integration (CI) |

## Getting Started

### Prerequisites

- Python 3.13
- Git
- A Groq API key

### Installation

Clone the repository:

```bash
git clone https://github.com/Kashish-2004/ai-infrastructure-incident-assistant.git
cd ai-infrastructure-incident-assistant

```
## API Endpoints

### `GET /`

Returns a basic message confirming that the application is running.

### `GET /system-status`

Collects the current CPU, memory, and disk usage of the system and returns a health status with detected issues.

Example response:

```json
{
  "status": "critical",
  "metrics": {
    "cpu_usage": 6.5,
    "memory_usage": 46.3,
    "disk_usage": 90.1
  },
  "issues": [
    "Disk usage is critically high!"
  ]
}

```
### `POST /incident`

Accepts an infrastructure incident description, retrieves relevant troubleshooting knowledge, optionally checks current system health, and generates an LLM-based recommendation.

Example request:

```json
{
  "incident": "My server has 95% disk usage because of huge logs. What should I investigate?"
}
```
{
  "incident": "My server has 95% disk usage because of huge logs. What should I investigate?",
  "retrieved_knowledge": "Possible Causes\n- Large log files\n- Temporary files\n- Old application files\n- Database or backup files consuming too much",
  "recommendation": "Investigation steps and recommended actions...",
  "requires_human_approval": true
}

## RAG and Incident Workflow

The `/incident` endpoint combines rule-based tool routing, retrieval-augmented generation (RAG), and LLM analysis.

The workflow is:

```text
Incident
   ↓
Rule-based decision
   ↓
System monitoring tool (when relevant)
   ↓
Semantic similarity search
   ↓
Relevant troubleshooting knowledge
   ↓
LLM analysis
   ↓
Incident recommendation
```
## Safety and Human Approval

The system separates incident investigation from remediation.

- The LLM is instructed not to execute or assume approval for remediation actions.
- Destructive remediation actions require human approval.
- The API explicitly returns `requires_human_approval: true`.
- The application does not provide the LLM with direct shell or command-execution access.

This design follows a human-in-the-loop approach where AI provides recommendations while potentially destructive actions remain under human control.

## CI/CD

The project uses GitHub Actions for continuous integration.

On every push to the `main` branch and on pull requests, the workflow:

1. Checks out the repository.
2. Sets up Python 3.13.
3. Installs project dependencies from `requirements.txt`.
4. Runs Python syntax validation using `compileall`.

A successful workflow confirms that the project dependencies can be installed and the Python source files pass the configured syntax check.


## Project Structure

```text
ai-infrastructure-incident-assistant/
│
├── main.py
├── system_monitor.py
├── chunking.py
├── vector_store.py
├── llm_test.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
│
├── knowledge_base/
│   └── disk_troubleshooting.md
│
└── .github/
    └── workflows/
        └── ci.yml
```

## Limitations and Future Improvements

The current version focuses on the core incident-analysis workflow. Possible future improvements include:

- Expanding the knowledge base with CPU, memory, networking, database, and deployment runbooks.
- Retrieving multiple relevant knowledge chunks instead of a single chunk.
- Replacing the in-memory vector store with a persistent vector database.
- Adding richer observability with metrics and distributed tracing.
- Integrating controlled infrastructure automation with explicit human approval.
- Adding authentication and authorization for production API usage.
- Deploying the application to a cloud environment.
- Adding automated unit and integration tests.