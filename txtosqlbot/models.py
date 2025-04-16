from langchain_core.language_models.chat_models import BaseChatModel
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
import os

from txtosqlbot.config import Config, ModelConfig, ModelProvider


def create_llm(model_config: ModelConfig) -> BaseChatModel:
    if model_config.provider == ModelProvider.OLLAMA:
        return ChatOllama(
            model=model_config.name,
            temperature=model_config.temperature,
            num_ctx=Config.OLLAMA_CONTEXT_WINDOW,
            verbose=False,
            keep_alive=-1,
        )
    elif model_config.provider == ModelProvider.GROQ:
        # Explicitly get and use the API key
        api_key = os.environ.get("GROQ_API_KEY")
        
        # Add this line to explicitly pass the API key
        return ChatGroq(
            model=model_config.name, 
            temperature=model_config.temperature,
            api_key=api_key
        )