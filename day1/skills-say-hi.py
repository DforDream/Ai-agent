from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

skill_path = Path(__file__).parent / ".codex" / "skills" / "hello-skill" / "SKILL.md"
skill_prompt = skill_path.read_text(encoding="utf-8")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)

response = client.responses.create(
    model="gpt-5.5",
    instructions=skill_prompt,
    input="请打招呼",
    max_output_tokens=200,
)

print(response.output_text)

# uv run --with openai --with python-dotenv --with Path python skills-say-hi.py
