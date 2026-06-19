import json
import os
from . import config
from qdrant_client.models import PointStruct
from src.utils.utils import embed, get_client


_ingested = False


def ingest():
    global _ingested
    if _ingested:
        return
    _ingested = True

    with open(os.path.join(config.DATA_DIR, "faq.json"), "r", encoding="utf-8") as f:
        faqs = json.load(f)

    client = get_client()

    for faq in faqs:
        chunk = faq["question"] + " " + faq["answer"]
        vector = embed(chunk)
        client.upsert(
            collection_name="knowledge",
            points=[
                PointStruct(
                    id=faq["id"],
                    vector=vector,
                    payload={
                        "category": faq.get("category", "General"),
                        "question": faq["question"],
                        "text": chunk,
                    },
                )
            ],
        )

    print("Uploaded", client.count(collection_name="knowledge").count, "chunks")


if __name__ == "__main__":
    ingest()