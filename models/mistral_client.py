import os
import time
import httpx
from dotenv import load_dotenv
from services.utils import count_tokens

load_dotenv()
TOGETHER_AI_TOKEN = os.getenv("TOGETHER_AI_TOKEN")

async def call_mistral(prompt: str) -> dict:
    start = time.time()

    headers = {
        "Authorization": f"Bearer {TOGETHER_AI_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.7
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.together.xyz/inference",
            headers=headers,
            json=payload
        )

        result = response.json()
        
        output = result.get("output", "")
        if isinstance(output, dict) and "choices" in output:
            output = output["choices"][0]["text"]  # fallback if needed
        elif not isinstance(output, str):
            output = str(output)

        output = output.lstrip()
        if output.startswith("A:"):
            output = output[2:].lstrip()
            output = output[2:].strip()
        elif output.startswith("Answer:"):
            output = output[6:].lstrip()
            output = output[6:].strip()

        return {
            "response": output,
            "latency_ms": int((time.time() - start) * 1000),
            "input_tokens": count_tokens(prompt, "mistral"),
            "output_tokens": count_tokens(output, "mistral")
        }