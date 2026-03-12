import streamlit as st
import pandas as pd
import PyPDF2
import json
import re

from orchestrator.workflow import EngineeringWorkflow


st.set_page_config(page_title="AI Automation Proposal Generator", layout="wide")

st.title("AI Warehouse Automation Proposal Generator")

st.write(
    "Upload RFP / specification documents and generate an automation proposal."
)

# -------------------------------
# JSON Cleaning Utility
# -------------------------------

def clean_json(text):

    if not isinstance(text, str):
        return text

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return text.strip()


def display_json_safe(data):

    try:
        cleaned = clean_json(data)
        parsed = json.loads(cleaned)
        st.json(parsed)

    except:
        st.write(data)


# -------------------------------
# File Upload
# -------------------------------

uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["pdf", "txt", "csv", "xlsx"],
    accept_multiple_files=True
)

rfp_text = ""

if uploaded_files:

    st.subheader("Uploaded Documents")

    for uploaded_file in uploaded_files:

        st.write("•", uploaded_file.name)

        file_type = uploaded_file.name.split(".")[-1].lower()

        if file_type == "pdf":

            pdf_reader = PyPDF2.PdfReader(uploaded_file)

            for page in pdf_reader.pages:
                rfp_text += page.extract_text()

        elif file_type == "txt":

            rfp_text += uploaded_file.read().decode("utf-8")

        elif file_type == "csv":

            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
            rfp_text += df.to_string()

        elif file_type == "xlsx":

            df = pd.read_excel(uploaded_file)
            st.dataframe(df)
            rfp_text += df.to_string()

        rfp_text += "\n\n"


# Manual input
manual_text = st.text_area("Or paste requirements manually")

if manual_text:
    rfp_text += manual_text


# -------------------------------
# Run Workflow
# -------------------------------

if st.button("Generate Proposal"):

    if not rfp_text.strip():

        st.warning("Please upload documents or paste requirements.")

    else:

        with st.spinner("Running AI Engineering Workflow..."):

            workflow = EngineeringWorkflow(rfp_text)

            results = workflow.run()

        st.success("Workflow Complete")

        # -------------------------------
        # Step 1
        # -------------------------------

        st.header("Step 1: Extracted Requirements")

        display_json_safe(results["requirements"])

        # -------------------------------
        # Step 2
        # -------------------------------

        st.header("Step 2: Automation Scenarios")

        st.write(results["scenarios"])

        # -------------------------------
        # Step 3
        # -------------------------------

        st.header("Step 3: Machine Selection")

        display_json_safe(results["machines"])

        # -------------------------------
        # Step 4
        # -------------------------------

        st.header("Step 4: Cost Estimation")

        display_json_safe(results["costs"])

        # -------------------------------
        # Step 5
        # -------------------------------

        st.header("Step 5: Generated Proposal")

        st.write(results["proposal"])

        # -------------------------------
        # PDF Download
        # -------------------------------

        try:

            with open("automation_proposal.pdf", "rb") as file:

                st.download_button(
                    label="Download Proposal PDF",
                    data=file,
                    file_name="automation_proposal.pdf",
                    mime="application/pdf"
                )

        except:
            st.warning("PDF not generated yet.")