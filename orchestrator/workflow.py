from agents.requirement_extractor import extract_requirements
from agents.scenario_generator import generate_scenarios
from agents.machine_selector import select_machines
from agents.cost_estimator import estimate_cost
from agents.proposal_generator import generate_proposal
from utils.pdf_generator import generate_pdf

from llama_index.core import VectorStoreIndex, Document, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

# Use local embedding model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Use Ollama instead of OpenAI
Settings.llm = Ollama(model="phi3")

class EngineeringWorkflow:

    def __init__(self, input_data):

        if isinstance(input_data, str):

            documents = [Document(text=input_data)]

            index = VectorStoreIndex.from_documents(documents)

            self.query_engine = index.as_query_engine()

        else:
            self.query_engine = input_data


    def run(self):

        print("\nStep 1: Extracting requirements...\n")
        requirements = extract_requirements(self.query_engine)
        print(requirements)

        print("\nStep 2: Generating automation scenarios...\n")
        scenarios = generate_scenarios(requirements)
        print(scenarios)

        print("\nStep 3: Selecting machines...\n")
        machines = select_machines(scenarios)
        print(machines)

        print("\nStep 4: Estimating project cost...\n")
        costs = estimate_cost(machines)
        print(costs)

        print("\nStep 5: Generating proposal...\n")
        proposal = generate_proposal(requirements, scenarios, machines, costs)
        print(proposal)

        generate_pdf(proposal)

        return {
            "requirements": requirements,
            "scenarios": scenarios,
            "machines": machines,
            "costs": costs,
            "proposal": proposal
        }