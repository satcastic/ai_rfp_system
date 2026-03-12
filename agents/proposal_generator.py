import ollama

def generate_proposal(requirements, scenarios, machines, costs):

    prompt = f"""
You are an industrial automation consultant preparing a professional engineering proposal.

Use the information below to generate a detailed automation system proposal.

SYSTEM REQUIREMENTS:
{requirements}

AUTOMATION SCENARIOS:
{scenarios}

SELECTED MACHINES:
{machines}

PROJECT COST ESTIMATES:
{costs}

The proposal should contain the following sections:

1. Project Overview
Explain the purpose of the automation project and the operational challenges it solves.

2. System Requirements Summary
Summarize the throughput requirements, carton specifications, pallet types, robot types, control systems, and integration requirements.

3. Proposed Automation Solutions
Describe the Basic, Standard, and Advanced automation scenarios in detail.

4. Selected Equipment
Explain why the selected robots, conveyors, and PLC systems are appropriate.

5. Cost Estimates for Each Option
Explain the estimated cost breakdown and how it relates to system complexity.

6. Recommended Solution
Recommend the best automation scenario and justify the choice.

7. Implementation Considerations
Describe deployment planning, integration with WMS/ERP, workforce training, and maintenance considerations.

Write the report in a professional engineering style.
"""

    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}],
        options={
            "temperature": 0.2,
            "num_predict": 1500
        }
    )

    return response["message"]["content"]