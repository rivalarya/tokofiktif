from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from sentence_transformers import SentenceTransformer

import atexit

_model = None
_client = None
_collection_name = "knowledge"


def _cleanup():
    global _client
    if _client is not None:
        _client.close()
        _client = None

atexit.register(_cleanup)


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("BAAI/bge-m3")
    return _model


def get_client():
    global _client
    if _client is None:
        _client = QdrantClient(path="./qdrant_db")
        embedding_dim = get_model().get_embedding_dimension()
        if not _client.collection_exists(_collection_name):
            _client.create_collection(
                collection_name=_collection_name,
                vectors_config=VectorParams(
                    size=embedding_dim,
                    distance=Distance.COSINE,
                ),
            )
    return _client


def embed(text: str) -> list[float]:
    return get_model().encode(text, normalize_embeddings=True).tolist()


def query(text: str) -> str:
    vector = embed(text)
    results = get_client().query_points(
        collection_name=_collection_name,
        query=vector,
        score_threshold=0.6,
        limit=1,
    )
    return "\n".join(
        point.payload.get("text", "") for point in results.points
    )