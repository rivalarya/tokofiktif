# TokoFiktif

Live demo of a RAG-powered customer service chatbot for a fictional Indonesian e-commerce company.

Built as the production implementation of findings from [faq-rag-benchmark](https://github.com/rivalarya/faq-rag-benchmark) — where 8B + RAG matched 70B accuracy at 88% lower cost.

**Live:** https://tokofiktif.rival.my.id  
**Case study:** https://rival.my.id/case-study/why-you-dont-need-a-bigger-model

## Stack

| Layer | Tech |
|---|---|
| Backend | FastAPI, Python |
| Frontend | Next.js, TypeScript |
| Vector DB | Qdrant |
| Embeddings | `BAAI/bge-m3` via sentence-transformers |
| Inference | `llama-3.1-8b-instant` via Groq API |
| Infra | Docker Compose |

## Structure

```
tokofiktif/
├── backend/      # FastAPI — RAG pipeline, Qdrant client, Groq inference
├── frontend/     # Next.js — chat UI
├── data/         # 100 FAQ items (TokoFiktif dataset)
└── docker-compose.yml
```

## Running Locally

```bash
cd backend
cp .env.example .env
# Fill in GROQ_API_KEY
docker compose up
```