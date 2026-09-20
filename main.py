from fastapi import FastAPI
from system_monitor import get_system_status
from pydantic import BaseModel
from vector_store import retrieve_relevant_chunk
from openai import OpenAI
from dotenv import load_dotenv
import os
from system_monitor import get_system_status
import logging



logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

class SystemMetrics(BaseModel):
        cpu_usage: float
        memory_usage:float
        disk_usage:float

class SystemStatus(BaseModel):
     status: str
     metrics:SystemMetrics
     issues:list[str]

class IncidentRequest(BaseModel):
     incident:str

class IncidentResponse(BaseModel):
    incident:str
    retrieved_knowledge:str
    recommendation: str
    requires_human_approval: bool


load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

client=OpenAI(
     api_key=api_key,
     base_url="https://api.groq.com/openai/v1"
)

def system_status_tool():
     return get_system_status()

app=FastAPI()

def should_check_system(incident_text):
    keywords = ["cpu", "memory", "ram", "disk", "storage", "server", "slow", "performance"]

    return any(keyword in incident_text.lower() for keyword in keywords)
     

@app.get("/")
def root():
    return"AI Infrastructure Incident Assistant is running!"

@app.get("/system-status",response_model=SystemStatus)
def system_status():
    status=get_system_status()
    issues=[]

    if status["disk_usage"]>90:
        health_status="critical"
        issues.append("Disk usage is critically high!")
    else:
        health_status="healthy"

    if status["cpu_usage"]>90:
        health_status="critical"
        issues.append("Cpu usage is critically high!!")
    if status["memory_usage"]>90:
        health_status="critical"
        issues.append("High Memory Usage!!")
    
         

    return {
        "status":health_status,
        "metrics":status,
        "issues":issues 
    }

@app.post("/incident",response_model=IncidentResponse)

def incident(request:IncidentRequest):
    incident_text=request.incident
    logger.info("Incident received: %s", incident_text)
    retrieved_chunk, similarity_score = retrieve_relevant_chunk(incident_text)
    logger.info("RAG retrieval completed with similarity score: %.3f", similarity_score)
    system_status = None

    if should_check_system(incident_text):
     system_status = system_status_tool()
     logger.info("System status tool executed")

    prompt = f"Incident: {incident_text}\nCurrent system status: {system_status}\nRelevant knowledge:\n{retrieved_chunk}\nDo not execute or assume approval for any remediation action. Clearly distinguish investigation steps from remediation actions that require human approval."
    response = client.responses.create(
    model="openai/gpt-oss-20b",
    input=prompt
)
    recommendation = response.output_text
    logger.info("LLM recommendation generated")
    return {
    "incident": incident_text,
    "retrieved_knowledge": retrieved_chunk,
    "recommendation": recommendation,
    "requires_human_approval":True
}


