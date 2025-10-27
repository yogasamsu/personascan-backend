from .resolver import resolve_identities
from .collector import collect_public_content
from .classifier import classify_content
from .risk_policy import determine_risk
from .summarizer import build_narrative

def run_pipeline(full_name: str, location: str | None):
    # 1. cari akun publik
    accounts = resolve_identities(full_name, location)

    # 2. ambil konten publik
    posts = collect_public_content(accounts)

    # 3. klasifikasikan konten
    scores = classify_content(posts)

    # 4. tentukan level risiko
    risk_level = determine_risk(scores)

    # 5. buat narasi formal
    narrative = build_narrative(full_name, scores)

    # 6. build final report-like structure
    return {
        "candidate_name": full_name,
        "risk_level": risk_level,
        "narrative": narrative,
        "scores": scores,
        "evidence_samples": scores["evidence_samples"]
    }
