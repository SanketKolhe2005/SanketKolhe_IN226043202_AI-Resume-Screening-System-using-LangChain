from langchain_core.runnables import RunnableLambda

def explain_fn(inputs):
    return {
        "score": inputs["score"],
        "matched_skills": inputs["matched"],
        "missing_skills": inputs["missing"],
        "reason": f"Candidate matches {len(inputs['matched'])} skills and misses {len(inputs['missing'])}."
    }

explain_chain = RunnableLambda(explain_fn)