def classify_content(posts: list[str]):
    # TODO: ganti dengan model beneran.
    # Sekarang: simple heuristic demo.
    toxicity_score = 0.12
    hate_speech_score = 0.03
    violence_incitement_score = 0.00
    professionalism_score = 0.78

    return {
        "toxicity_score": toxicity_score,
        "hate_speech_score": hate_speech_score,
        "violence_incitement_score": violence_incitement_score,
        "professionalism_score": professionalism_score,
        "evidence_samples": posts[:2]  # ambil 2 contoh kalimat
    }
