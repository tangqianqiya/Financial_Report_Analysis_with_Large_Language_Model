from sentence_transformers import SentenceTransformer
from langchain_community.llms import Ollama
from financial_rag.config import EMBED_MODEL_NAME, LLM_MODEL
import torch

class EmbeddingModel:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")  # 打印当前设备

        # 直接加载模型到 CUDA
        self.model = SentenceTransformer(EMBED_MODEL_NAME, device=self.device)

    def encode(self, texts):
        return self.model.encode(texts)

class LLMModel:
    def __init__(self):
        self.model = Ollama(model=LLM_MODEL)

    def generate(self, prompt):
        response = ""
        for token in self.model.stream(prompt):
            response += token
        return response
