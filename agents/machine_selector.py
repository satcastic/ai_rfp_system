import json
import re
from ollama import Client

client = Client()


def extract_json(text):

    # remove markdown blocks
    text = text.replace("```json", "").replace("```", "")

    # remove trailing commas
    text = re.sub(r",\s*}", "}", text)
    text = re.sub(r",\s*]", "]", text)

    # extract first JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        return match.group(0)

    return text


def select_machines(scenarios):

    prompt = f"""
Select machines for these automation scenarios.

Return ONLY JSON.

FORMAT:

{{
 "basic": {{
   "robots": [],
   "conveyors": [],
   "plc": []
 }},
 "standard": {{
   "robots": [],
   "conveyors": [],
   "plc": []
 }},
 "advanced": {{
   "robots": [],
   "conveyors": [],
   "plc": []
 }}
}}

Automation Scenarios:
{scenarios}
"""

    response = client.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}],
        options={
            "temperature": 0,
            "num_predict": 300
        }
    )

    text = response["message"]["content"]

    json_text = extract_json(text)

    machines = json.loads(json_text)

    return machines