from langchain_core.runnables import RunnableLambda

def score_fn(inputs):
    matched = inputs["matched"]
    missing = inputs["missing"]

    total = len(matched) + len(missing)
    score = int((len(matched) / total) * 100) if total else 0

    return {
        "score": score,
        "matched": matched,   # ✅ keep
        "missing": missing    # ✅ keep
    }

score_chain = RunnableLambda(score_fn)