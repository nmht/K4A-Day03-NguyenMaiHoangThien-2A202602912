"""
🚀 FASTAPI DEMO SERVER FOR REACT AGENT & MCP DASHBOARD
Khởi chạy Web UI tại http://localhost:8000
"""

import json
import os
import sys
import webbrowser
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn

# Inject parent directory into sys.path to import src modules
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "src"))

from src.mcp_server import MCPAcademicServer
from src.providers import get_llm_provider
from src.app import run_react_agent, save_waterfall_trace

app = FastAPI(title="Supply Chain ReAct Agent MCP Demo Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Shared Instance
provider = get_llm_provider()
mcp_server = MCPAcademicServer()

class QueryRequest(BaseModel):
    query: str

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "provider": provider.__class__.__name__,
        "mcp_server": mcp_server.server_name
    }

@app.post("/api/run-agent")
def api_run_agent(req: QueryRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query string cannot be empty")
    
    try:
        trace_logs = run_react_agent(req.query.strip(), provider, mcp_server)
        save_waterfall_trace(trace_logs)
        return {
            "status": "success",
            "query": req.query,
            "trace_logs": trace_logs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/waterfall-trace")
def get_waterfall_trace():
    trace_path = os.path.join(BASE_DIR, "docs", "trace_waterfall.json")
    if not os.path.exists(trace_path):
        return []
    try:
        with open(trace_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read trace file: {str(e)}")

@app.get("/api/test-cases")
def get_test_cases():
    config_path = os.path.join(BASE_DIR, "config", "test_cases.json")
    if not os.path.exists(config_path):
        return []
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Serve static demo UI files
DEMO_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get("/")
def serve_index():
    return FileResponse(os.path.join(DEMO_DIR, "index.html"))

app.mount("/", StaticFiles(directory=DEMO_DIR, html=True), name="static")

if __name__ == "__main__":
    print("==================================================================")
    print("🚀 SUPPLY CHAIN REACT AGENT - INTERACTIVE DEMO SERVER IS RUNNING")
    print("🌐 Access Dashboard Web UI at: http://localhost:8000")
    print("==================================================================")
    
    # Try to open browser automatically
    try:
        webbrowser.open("http://localhost:8000")
    except Exception:
        pass

    uvicorn.run(app, host="0.0.0.0", port=8000)
