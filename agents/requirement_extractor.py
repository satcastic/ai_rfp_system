from ollama import Client

client = Client()


def extract_requirements(query_engine):

    query = """
Extract the warehouse automation system requirements from the RFP.

Return JSON with:

throughput
carton_weight
pallet_type
robot_type
gripper_type
conveyor_speed
control_system
integration
power_requirement
"""

    nodes = query_engine.retrieve(query)

    context = "\n".join([node.text for node in nodes])

    prompt = f"""
Use the following document context to extract system requirements.

Context:
{context}

{query}
"""

    response = client.chat(
    model="phi3",
    messages=[{"role": "user", "content": prompt}],
    options={"temperature": 0}
)

    return response["message"]["content"]