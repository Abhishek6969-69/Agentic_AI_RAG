import pymupdf
from langchain_core.documents import Document


def load_pdf(file_path: str) -> list[Document]:
    pdf = pymupdf.open(file_path)

    documents = []

    for page_number, page in enumerate(pdf):
        text = page.get_text()

        if text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "page": page_number + 1,
                        "source": file_path
                    }
                )
            )

    pdf.close()

    return documents

