import os
os.environ["OPENAI_API_KEY"] = 'YOUR_OPENAI_API_KEY'

from llama_index import GPTSimpleVectorIndex, LLMPredictor
from langchain import OpenAI

query_text ="ailia SDKでVulkanを使用するにはどうすれば良いですか。日本語で回答してください。"

llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, max_tokens=350))
index = GPTSimpleVectorIndex.load_from_disk('index.json')
response = index.query(query_text, llm_predictor=llm_predictor)

print("Q:", query_text)
print("A:", str(response))
