from langchain_core.runnables import RunnableLambda

def extract_fn(inputs):
    resume = inputs["resume"].lower()

    # Few-shot examples (simple simulation)
    examples = [
        {"text": "Python, Machine Learning", "skills": ["python", "machine learning"]},
        {"text": "Deep Learning, NLP", "skills": ["deep learning", "nlp"]}
    ]

    skills_list = [
        "python", "machine learning", "deep learning", "nlp",
        "tensorflow", "pytorch", "scikit-learn", "pandas", "numpy"
    ]

    found_skills = [s for s in skills_list if s in resume]

    return {
        "skills": found_skills
    }

extract_chain = RunnableLambda(extract_fn)