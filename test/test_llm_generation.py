from models.llm_generation import llm_generation
print("== LLM Generation Test ==")
prompt = "Write a haiku about the ocean"
response = llm_generation(prompt)
print("LLM Output:", response)
