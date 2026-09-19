import os

from dotenv import load_dotenv
from pinecone import Pinecone


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")


if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is not set")

if not INDEX_NAME:
    raise ValueError("PINECONE_INDEX_NAME is not set")


pc = Pinecone(api_key=PINECONE_API_KEY)

index = pc.Index(INDEX_NAME)