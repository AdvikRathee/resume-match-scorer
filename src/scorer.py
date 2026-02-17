from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_match_analysis(resume_text, jd_text):
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    tfidf_score = similarity * 100

    # 🔥 Skill-based scoring
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())

    matched_keywords = list(resume_words.intersection(jd_words))
    missing_keywords = list(jd_words - resume_words)

    if len(jd_words) > 0:
        skill_score = (len(matched_keywords) / len(jd_words)) * 100
    else:
        skill_score = 0

    # 🔥 Hybrid weighted score (better logic)
    final_score = round((0.6 * skill_score) + (0.4 * tfidf_score), 2)

    if final_score >= 80:
        explanation = "Excellent alignment. Resume strongly matches required skills."
    elif final_score >= 65:
        explanation = "Good match. Most required technical skills are present."
    elif final_score >= 50:
        explanation = "Moderate match. Core skills align but some important gaps exist."
    else:
        explanation = "Low match. Significant required skills are missing."

    return final_score, explanation, matched_keywords[:15], missing_keywords[:15]
