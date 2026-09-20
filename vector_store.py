from chunking import load_and_chunk_document
from sentence_transformers import SentenceTransformer
import numpy as np


vector_store=[]
model=SentenceTransformer("all-MiniLM-L6-v2")

chunks = load_and_chunk_document()

for chunk in chunks:
    embedding =model.encode(chunk)
    vector_store.append(
        {
            "chunk": chunk,
            "embedding": embedding
        }
    )

def retrieve_relevant_chunk(query):
    query_embedding= model.encode(query)
    best_score=-1
    best_chunk=None

    for item in vector_store:
        stored_embedding =item["embedding"]
        dot_product=np.dot(query_embedding,stored_embedding)
        query_norm=np.linalg.norm(query_embedding)
        stored_norm =np.linalg.norm(stored_embedding)
        similarity= dot_product/(query_norm*stored_norm)

        if(similarity>best_score):
            best_score=similarity
            best_chunk=item["chunk"]

    return best_chunk, best_score

retrieved_chunk,similarity_score= retrieve_relevant_chunk("My server is running out of storage because of huge logs.")


'''print(retrieved_chunk)
print(similarity_score)'''