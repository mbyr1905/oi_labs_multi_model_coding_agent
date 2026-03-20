import re
import json

def extract_json(text):
    try:
        # Step 1: Remove markdown
        text = re.sub(r"```json|```", "", text).strip()

        # Step 2: Find JSON block
        start = text.find("{")
        end = text.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON object found")

        json_str = text[start:end+1]

        # Step 3: Fix common issues
        json_str = json_str.replace("\r", "")
        
        # Escape unescaped newlines inside strings
        json_str = re.sub(
            r'(?<!\\)\n',
            '\\n',
            json_str
        )

        # Step 4: Fix trailing commas
        json_str = re.sub(r",\s*}", "}", json_str)
        json_str = re.sub(r",\s*]", "]", json_str)

        return json.loads(json_str)

    except Exception as e:
        raise ValueError(f"JSON parsing failed.\nRaw output:\n{text}\nError:\n{e}")