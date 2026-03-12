from ollama import Client

client = Client()

def generate_scenarios(requirements):

    prompt = f"""
You are a warehouse automation engineer.

Create THREE automation scenarios using the requirements below.

Requirements:
{requirements}

Return ONLY these THREE sections:

BASIC
STANDARD
ADVANCED

For EACH include:

System Architecture
Machines Used
Expected Throughput

Do NOT generate proposals.
Do NOT generate additional instructions.
Do NOT repeat the requirements.
"""

    response = client.chat(
    model="phi3",
    messages=[{"role": "user", "content": prompt}],
    options={
        "temperature": 0,
        "num_predict": 800
    }
)

    return response["message"]["content"]