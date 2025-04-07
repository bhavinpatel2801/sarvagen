# core/memory.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import uuid
import os
import pickle

class MemoryStore:
    def __init__(self, dim=384, index_path=None):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = {}  # ID -> metadata
        self.counter = 0
        self.index_path = index_path
        if index_path:
            self._load(index_path)

    def add_memory(self, content, source="user", modality="text"):
        vector = self.model.encode([content])[0]
        self.index.add(np.array([vector]).astype('float32'))

        memory_id = str(uuid.uuid4())
        self.metadata[self.counter] = {
            "id": memory_id,
            "content": content,
            "source": source,
            "modality": modality
        }
        self.counter += 1

    def query(self, query_text, top_k=3):
        if self.counter == 0:
            return []

        query_vec = self.model.encode([query_text])[0].astype('float32')
        D, I = self.index.search(np.array([query_vec]), top_k)

        results = []
        for idx in I[0]:
            if idx in self.metadata:
                results.append(self.metadata[idx])
        return results

    def save(self, folder="data/faiss_store"):
        os.makedirs(folder, exist_ok=True)
        faiss.write_index(self.index, os.path.join(folder, "index.faiss"))
        with open(os.path.join(folder, "metadata.pkl"), "wb") as f:
            pickle.dump(self.metadata, f)

    def _load(self, folder):
        index_file = os.path.join(folder, "index.faiss")
        meta_file = os.path.join(folder, "metadata.pkl")
        if os.path.exists(index_file) and os.path.exists(meta_file):
            self.index = faiss.read_index(index_file)
            with open(meta_file, "rb") as f:
                self.metadata = pickle.load(f)
            self.counter = len(self.metadata)

# ✅ Singleton for use across the system
memory = MemoryStore()
