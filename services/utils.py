import tiktoken

from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest

ENCODER = tiktoken.encoding_for_model("gpt-3.5-turbo")
MISTRAL_TOKENIZER = MistralTokenizer.v1()

def count_tokens(text: str, model: str) -> int:
    if model == "llama3":
        return len(ENCODER.encode(text))
    elif model == "mistral":
        request = ChatCompletionRequest(messages=[UserMessage(content=text)])
        return len(MISTRAL_TOKENIZER.encode_chat_completion(request).tokens)
    else:
        raise ValueError("Unsupported model for token counting")
