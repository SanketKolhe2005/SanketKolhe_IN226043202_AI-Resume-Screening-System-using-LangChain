from langchain_core.runnables import RunnableLambda

def match_fn(inputs):
    skills = inputs["skills"]
    jd_text = inputs["job_description"].lower()

    jd_skills = [
        "python", "machine learning", "deep learning", "nlp",
        "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy"
    ]

    # extract JD skills properly
    jd_present = []
    for skill in jd_skills:
        if skill in jd_text:
            jd_present.append(skill)

    matched = []
    for s in skills:
        if s in jd_present:
            matched.append(s)

    missing = []
    for s in jd_present:
        if s not in skills:
            missing.append(s)

    return {
        "matched": matched,
        "missing": missing
    }

match_chain = RunnableLambda(match_fn)