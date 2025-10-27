from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import CandidateInput, PersonaReport, RiskScores
from .pipeline.run_pipeline import run_pipeline

app = FastAPI(title="PersonaScan.AI API", version="0.1")

# CORS supaya frontend React bisa fetch API lokal
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only, nanti restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/analyze_candidate", response_model=PersonaReport)
def analyze_candidate(payload: CandidateInput):
    result = run_pipeline(
        full_name=payload.full_name,
        location=payload.location
    )

    response = {
        "candidate_name": result["candidate_name"],
        "risk_level": result["risk_level"],
        "narrative": result["narrative"],
        "scores": {
            "toxicity_score": result["scores"]["toxicity_score"],
            "hate_speech_score": result["scores"]["hate_speech_score"],
            "violence_incitement_score": result["scores"]["violence_incitement_score"],
            "professionalism_score": result["scores"]["professionalism_score"],
        },
        "evidence_samples": result["evidence_samples"]
    }

    return response
