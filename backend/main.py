"""
Adversarial AI Defense System - FastAPI Backend
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

from routers import health, query, attacks, metrics
from bert_classifier import BERTClassifier
from cosine_drift_monitor import CosineDriftMonitor
from retrieval_engine import RetrievalEngine
from integrity_scorer import IntegrityScorer
from pipeline import RAGPipeline


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: initialize ML components
    classifier = BERTClassifier()
    drift_monitor = CosineDriftMonitor()
    retrieval_engine = RetrievalEngine()
    integrity_scorer = IntegrityScorer()
    pipeline = RAGPipeline()

    app.state.classifier = classifier
    app.state.drift_monitor = drift_monitor
    app.state.retrieval_engine = retrieval_engine
    app.state.integrity_scorer = integrity_scorer
    app.state.pipeline = pipeline

    print("✅ Adversarial AI backend started")
    yield
    print("🛑 Shutting down")


app = FastAPI(
    title="Adversarial AI RAG Security API",
    description="Detects prompt injection, adversarial attacks, and monitors RAG pipeline integrity",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# ── CORS ──────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # lock down to Vercel URL after testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ───────────────────────────────────────────────────────
app.include_router(health.router,  prefix="/api/v1", tags=["Health"])
app.include_router(query.router,   prefix="/api/v1", tags=["Query"])
app.include_router(attacks.router, prefix="/api/v1", tags=["Attacks"])
app.include_router(metrics.router, prefix="/api/v1", tags=["Metrics"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)