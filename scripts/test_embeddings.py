from app.ingestion.embedder import create_embeddings


texts = [
    "Agentic AI systems can autonomously perform tasks.",
    "Traditional software follows predefined instructions."
]

embeddings = create_embeddings(texts)

print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))
print("First 10 values:")
print(embeddings[0][:10])