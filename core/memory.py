# import necessary libraries
from sentence_transformers import SentenceTransformer                 # Import SentenceTransformer for generating embeddings
import faiss                                                          # Import FAISS for vector similarity search
import numpy as np                                                    # Import NumPy for numerical operations
import uuid                                                           # Import uuid for generating unique memory IDs
import os                                                             # For file and folder operations
import pickle                                                         # For saving and loading Python objects

# Define a class for managing vector-based memory storage and retrieval
class MemoryStore:
    def __init__(self, dim=384, index_path=None, autosave=True):
         # Load pre-trained sentence embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2") 
        self.index = faiss.IndexFlatL2(dim)                           # Initialize a FAISS index with L2 distance and specified embedding dimension
        self.metadata = {}                                            # Dictionary to hold metadata (ID → metadata dictionary)
        self.counter = 0                                              # Internal counter to track entries in FAISS index
        self.index_path = index_path                                  # Path to load/save FAISS index and metadata
        self.autosave = autosave                                      # If true, saves to disk on each add

        # Load previous index and metadata if a path is given
        if index_path:
            self._load(index_path)

    # Normalize input text (strip whitespace and convert to lowercase)
    def _normalize(self, text: str) -> str:
        return text.strip().lower()

    # Add a new memory to the store
    def add_memory(self, content, source="user", modality="text"):
        content = self._normalize(content)                            # Clean and standardize input text
        vector = self.model.encode([content])[0]                      # Encode into vector using SentenceTransformer
        self.index.add(np.array([vector]).astype('float32'))          # Add vector to FAISS index

        # Generate unique UUID for the memory
        memory_id = str(uuid.uuid4())
        # Store associated metadata
        self.metadata[self.counter] = {
            "id": memory_id,
            "content": content,
            "source": source,
            "modality": modality
        }
        self.counter += 1                                             # Increment the internal counter

        # Automatically save to disk if enabled
        if self.autosave and self.index_path:
            self.save(self.index_path)

    # Query top_k most similar memories from FAISS based on input text
    def query(self, query_text, top_k=3, modality_filter=None):
        if self.counter == 0:
            return []                                                # Return empty list if no memories exist                          

        # Normalize and vectorize the query
        query_vec = self.model.encode([self._normalize(query_text)])[0].astype('float32')
        D, I = self.index.search(np.array([query_vec]), top_k)       # Search FAISS index for top_k most similar vectors

        results = []
        # For each matched index, retrieve and filter metadata
        for idx in I[0]:
            if idx in self.metadata:
                entry = self.metadata[idx]
                if modality_filter is None or entry["modality"] == modality_filter:
                    results.append(entry)
        return results

    # Save FAISS index and metadata to disk
    def save(self, folder="data/faiss_store"):
        os.makedirs(folder, exist_ok=True)                           # Ensure directory exists
        faiss.write_index(self.index, os.path.join(folder, "index.faiss"))    # Save vector index
        with open(os.path.join(folder, "metadata.pkl"), "wb") as f:
            pickle.dump(self.metadata, f)                            # Save metadata dictionary

    # Load previously saved index and metadata
    def _load(self, folder):
        index_file = os.path.join(folder, "index.faiss")
        meta_file = os.path.join(folder, "metadata.pkl")
        if os.path.exists(index_file) and os.path.exists(meta_file):
            self.index = faiss.read_index(index_file)                # Load FAISS index
            with open(meta_file, "rb") as f:
                self.metadata = pickle.load(f)                       # Load metadata dictionary
            self.counter = len(self.metadata)                       # Set counter to number of entries

# ✅ Create a singleton instance of MemoryStore for reuse across the system
memory = MemoryStore(index_path="data/faiss_store")
