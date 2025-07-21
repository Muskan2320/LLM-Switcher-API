from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

llama3_prompts = [
    "What is the capital of France?",
    "Explain the theory of relativity in simple terms.",
    "Write a haiku about the ocean."
]

mistral_prompts = [
    "Who wrote the play Hamlet?",
    "Summarize the plot of Inception.",
    "Give three facts about black holes."
]

def validate_response_structure(data):
    assert "response" in data
    assert "latency" in data
    assert "token_count" in data
    assert "input_tokens" in data["token_count"]
    assert "output_tokens" in data["token_count"]

def test_llama3_examples():
    for prompt in llama3_prompts:
        resp = client.post("/ask_prompt", json={"prompt": prompt, "model": "llama3"})
        assert resp.status_code == 200
        data = resp.json()
        validate_response_structure(data)
        print("LLAMA3 Test passed:", data)

def test_mistral_examples():
    for prompt in mistral_prompts:
        resp = client.post("/ask_prompt", json={"prompt": prompt, "model": "mistral"})
        assert resp.status_code == 200
        data = resp.json()
        validate_response_structure(data)
        print("Mistral Test passed:", data)

def test_invalid_model():
    resp = client.post("/ask_prompt", json={"prompt": "hello world", "model": "unknown"})
    assert resp.status_code == 400
    print("Invalid model test passed with status:", resp.status_code)

# Run all tests
if __name__ == "__main__":
    test_llama3_examples()
    test_mistral_examples()
    test_invalid_model()
