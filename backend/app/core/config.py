import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o-mini"
#used in comparator
SEMANTIC_WEIGHT = 0.3
SKILLS_WEIGHT = 0.5
EXPERIENCE_WEIGHT = 0.2