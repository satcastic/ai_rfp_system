from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


def generate_pdf(proposal_text, filename="automation_proposal.pdf"):

    styles = getSampleStyleSheet()

    elements = []

    # Split text into paragraphs
    paragraphs = proposal_text.split("\n")

    for para in paragraphs:
        if para.strip() == "":
            elements.append(Spacer(1, 12))
        else:
            elements.append(Paragraph(para, styles["Normal"]))
            elements.append(Spacer(1, 12))

    pdf = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    pdf.build(elements)

    print(f"PDF generated: {filename}")