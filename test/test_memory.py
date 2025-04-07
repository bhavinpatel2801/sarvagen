from core.memory import MemoryStore

print("== MemoryStore Test ==")
mem = MemoryStore()
mem.add_memory("Van Gogh was a Dutch painter.", modality="text")
print(mem.query("Who is Van Gogh?"))