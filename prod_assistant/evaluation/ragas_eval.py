import asyncio
from utils.model_loader import ModelLoader
from ragas import SingleTurnSample
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.metrics import LLMContextPrecisionWithoutReference, ResponseRelevancy
import grpc.experimental.aio as grpc_aio
grpc_aio.init_grpc_aio()
model_loader=ModelLoader()


def evaluate_context_precision():
    """
    Evaluate the context precision of the LLM.
    """
    pass


def evaluate_response_relevancy():
    """
    Evaluate the response relevancy of the LLM.
    """
    pass