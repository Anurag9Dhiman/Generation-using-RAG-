from transformers import pipeline


class Generator:
    def __init__(self, model_name='distilgpt2'):
        self.generator = pipeline('text-generation', model=model_name)


    def generate(self, query, context, max_length=250):
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
        response = self.generator(prompt, max_length=max_length, do_sample=True, temperature=0.7)
        return response[0]['generated_text']