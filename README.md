# LLM Switcher

A FastAPI-based service to route prompts to different Large Language Models (LLMs) such as Llama3 and Mistral, with logging and token counting.

---

## Features

- **Switch between Llama3 and Mistral models** via a single API endpoint.
- **Logs all prompts and responses** with latency and token counts.
- **Easily extensible** for more models.

---

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the project root with your Together API key:
     ```
     TOGETHER_AI_TOKEN=your_together_api_key_here
     ```
   - You can get a free API key from [Together API](https://www.together.xyz/).

---

## Run

Start the FastAPI server with Uvicorn:
```bash
uvicorn main:app --reload
```
- The API will be available at `http://127.0.0.1:8000`.

---

## Usage

Send a POST request to `/ask_prompt` with JSON:
```json
{
  "prompt": "your prompt here",
  "model": "llama3" // or "mistral"
}
```

- `model` must be either `"llama3"` or `"mistral"`.

**Example using `curl`:**
```bash
curl -X POST http://127.0.0.1:8000/ask_prompt \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is the capital of France?", "model": "llama3"}'
```

---

## Logs

- All prompt/response logs are saved in `logs/prompts.jsonl` as JSON lines.
- Each log entry includes: model, prompt, response, latency, token counts, and timestamp.

---

## Testing

Run the test code:
```bash
python -m tests.test_api
```
- Tests cover both Llama3 and Mistral endpoints, response structure, and error handling.

---

## Project Structure

```
main.py                # FastAPI app and endpoint
models/
  llama3_client.py     # Llama3 API client
  mistral_client.py    # Mistral API client
services/
  model_router.py      # Model routing logic
  utils.py             # Token counting utilities
  logger.py            # Logging utility
logs/
  prompts.jsonl        # Log file (auto-created)
tests/
  test_api.py          # API tests
requirements.txt       # Python dependencies
README.md              # This file
```

---

## Requirements

- Python 3.8+
- See `requirements.txt` for all dependencies.

---

## Notes

- Make sure your Together API key is valid and has sufficient quota.
- To add more models, implement a new client in `models/` and update the router logic. 