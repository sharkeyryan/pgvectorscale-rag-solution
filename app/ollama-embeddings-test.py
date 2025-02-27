import ollama 

print('Waiting for model to load... \n')

embeddings = ollama.embeddings(
  model='nomic-embed-text', 
  prompt='Yoda, the wise Jedi Master, navigated the mysterious Degoda system with caution.'
)

print(embeddings.embedding)