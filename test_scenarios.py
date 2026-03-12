from retrieval.load_index import load_or_build_index
from retrieval.query_engine import create_query_engine
from utils.pdf_generator import generate_pdf
from orchestrator.workflow import EngineeringWorkflow


folder = "test_documents"

index = load_or_build_index(folder)

query_engine = create_query_engine(index)

workflow = EngineeringWorkflow(query_engine)

results = workflow.run()