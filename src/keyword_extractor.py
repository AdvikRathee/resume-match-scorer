def extract_keywords(resume_text, jd_text):
    """
    Extract common keywords between resume and job description.
    """

    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())

    matching_words = resume_words.intersection(jd_words)

    return list(matching_words)[:15]
