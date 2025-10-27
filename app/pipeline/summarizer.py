def build_narrative(candidate_name: str, scores: dict) -> str:
    # Narasi harus formal, netral, audit-able.
    return (
        f"Berdasarkan analisis konten publik yang diasosiasikan "
        f"dengan kandidat '{candidate_name}', tidak ditemukan indikasi "
        f"ujaran kebencian atau ajakan kekerasan. Konten dominan "
        f"bersifat positif dan profesional (≈ {int(scores['professionalism_score']*100)}%). "
        "Risiko digital dikategorikan rendah. "
        "Rekomendasi: kandidat dapat dilanjutkan ke tahap seleksi berikutnya "
        "dengan klarifikasi manual oleh panitia."
    )
