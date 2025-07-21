from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import json
import os
from services.model_router import route_model_call
from services.logger import log_to_file

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    model: str

@app.post("/ask_prompt")
async def prompt_endpoint(req: PromptRequest):
    start = time.time()
    try:
        result = await route_model_call(req.model, req.prompt)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    latency = time.time() - start

    log_entry = {
        "model": req.model,
        "prompt": req.prompt,
        "response": result["response"],
        "latency": result["latency_ms"],
        "token_count": {
            "input_tokens": result["input_tokens"],
            "output_tokens": result["output_tokens"],
        },
    }
    log_to_file(log_entry)
    
    return log_entry