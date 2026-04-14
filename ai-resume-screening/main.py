import os
import json

# LangSmith (required)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "LANGCHAIN_API_KEY"

from langchain_core.runnables import RunnableLambda, RunnableConfig

from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain

# ✅ LangSmith tags (BONUS)
config = RunnableConfig(tags=["resume-screening", "bonus"])

# Load job description
jd = open("data/job_description.txt").read()

resumes = [
    "data/resume_strong.txt",
    "data/resume_average.txt",
    "data/resume_weak.txt"
]

# 🔥 Build ONE pipeline
pipeline = (
    extract_chain
    | RunnableLambda(lambda x: {
        "skills": x["skills"],
        "job_description": jd
    })
    | match_chain
    | score_chain
    | explain_chain
)

# 🚀 Run pipeline
for file in resumes:
    print("\n=============================")
    print("Processing:", file)

    resume = open(file).read()

    result = pipeline.invoke(
        {"resume": resume},
        config=config   # ✅ IMPORTANT (for LangSmith tags)
    )

    # ✅ Pretty JSON output (BONUS)
    print(json.dumps(result, indent=2))