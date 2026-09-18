from app.ingestion.loader import load_pdf


documents = load_pdf("data/Ebook-Agentic-AI.pdf")

print("Number of pages:", len(documents))

for document in documents[:2]:
    print("\nPAGE:", document.metadata["page"])
    print(document.page_content[:500])