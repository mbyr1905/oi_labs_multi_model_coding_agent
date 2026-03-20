BASE_JSON_RULES = """
Rules:
- No explanation
- No markdown
- Output STRICTLY valid JSON
- Ensure json.loads() can parse it

CRITICAL JSON RULES:
- Escape ALL double quotes inside code using \"
- Escape ALL newlines as \\n
- Do NOT include raw newlines inside strings
- Do NOT break JSON format
"""

CODE_GEN_RULES = """
Requirements:
- Use best practices
- Follow modular architecture
- Ensure all files are connected properly
- Use clean folder structure
"""

DEBUG_RULES = """
Fix issues:
- Syntax errors
- Import issues
- API mismatches
- Missing dependencies

IMPORTANT:
- Do NOT rewrite entire project
- Only fix broken parts
- Keep changes minimal
"""

FILES_OUTPUT_FORMAT = """
Return ONLY valid JSON:

{
  "files": [
    {
      "path": "",
      "content": ""
    }
  ]
}
"""

EVALUATION_RULES = """
Evaluate based on:
- Code correctness
- API consistency
- Integration correctness
- Structure quality

Return JSON:

{
  "score": 0-100,
  "issues": [],
  "decision": "good" or "bad"
}
"""

def build_prompt(role, context, task, extra_rules=""):
    return f"""
You are a {role}.

{context}

TASK:
{task}

{extra_rules}

{BASE_JSON_RULES}
"""