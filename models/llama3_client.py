import os
import time
import httpx
from dotenv import load_dotenv
from services.utils import count_tokens

load_dotenv()
TOGETHER_AI_TOKEN = os.getenv("TOGETHER_AI_TOKEN")

async def call_llama3(prompt: str) -> dict:
    start = time.time()

    headers = {
        "Authorization": f"Bearer {TOGETHER_AI_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        "messages": [
            { "role": "user", "content": prompt }
        ],
        "max_tokens": 100,
        "temperature": 0.7
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            "https://api.together.xyz/inference",
            headers=headers,
            json=payload
        )
        result = response.json()        
        output = result.get("output", {}).get("choices", [{}])[0].get("text", "")

        return {
            "response": output,
            "latency_ms": int((time.time() - start) * 1000),
            "input_tokens": count_tokens(prompt, "llama3"),  # still valid
            "output_tokens": count_tokens(output, "llama3")
        }