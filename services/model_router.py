from models.llama3_client import call_llama3
from models.mistral_client import call_mistral

async def route_model_call(model: str, prompt: str):
    if model == "llama3":
        return await call_llama3(prompt)
    elif model == "mistral":
        return await call_mistral(prompt)
    else:
        raise ValueError("Model not supported") 