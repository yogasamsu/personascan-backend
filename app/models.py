from pydantic import BaseModel
from typing import List, Optional, Dict

class CandidateInput(BaseModel):
    full_name: str
    location: Optional[str] = None
    email_hint: Optional[str] = None

class RiskScores(BaseModel):
    toxicity_score: float
    hate_speech_score: float
    violence_incitement_score: float
    professionalism_score: float

class PersonaReport(BaseModel):
    candidate_name: str
    risk_level: str
    narrative: str
    scores: RiskScores
    evidence_samples: List[str]
