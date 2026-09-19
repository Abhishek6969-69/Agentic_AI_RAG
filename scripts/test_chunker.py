from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_documents



documents = load_pdf("data/Ebook-Agentic-AI.pdf")

chunks = chunk_documents(documents)

print("Number of pages:", len(documents))
print("Number of chunks:", len(chunks))

print("\nFirst chunk:")
print(chunks[0].page_content)

print("\nMetadata:")
print(chunks[0].metadata)