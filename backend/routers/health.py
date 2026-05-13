from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
        "components": {
            "bert_classifier": "operational",
            "drift_monitor": "operational",
            "retrieval_engine": "operational",
            "integrity_scorer": "operational",
            "rag_pipeline": "operational",
        },
    }


@router.get("/ping")
async def ping():
    return {"pong": True, "timestamp": datetime.utcnow().isoformat()}