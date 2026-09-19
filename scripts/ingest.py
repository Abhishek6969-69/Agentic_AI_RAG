from app.ingestion.loader import load_pdf
from app.ingestion.chunker import chunk_documents
from app.vectorstore.pinecone_store import index


PDF_PATH = "data/Ebook-Agentic-AI.pdf"
NAMESPACE = "agentic-ai"
BATCH_SIZE = 50


def ingest_documents():
    print("Loading PDF...")

    documents = load_pdf(PDF_PATH)

    print(f"Loaded {len(documents)} pages")

    print("Creating chunks...")

    chunks = chunk_documents(documents)

    print(f"Created {len(chunks)} chunks")

    records = []

    for i, chunk in enumerate(chunks):
        records.append(
            {
                "_id": f"chunk-{i}",
                "text": chunk.page_content,
                "page": chunk.metadata["page"],
                "source": chunk.metadata["source"],
            }
        )

    print(f"Prepared {len(records)} records")

    for start in range(0, len(records), BATCH_SIZE):
        end = start + BATCH_SIZE
        batch = records[start:end]

        print(
            f"Uploading records {start + 1}-{min(end, len(records))}..."
        )

        index.upsert_records(
            namespace=NAMESPACE,
            records=batch,
        )

    print("Upload completed successfully")


if __name__ == "__main__":
    ingest_documents()