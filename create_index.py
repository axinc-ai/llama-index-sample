import os
os.environ["OPENAI_API_KEY"] = 'YOUR_OPENAI_API_KEY'

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from llama_index import download_loader

CJKPDFReader = download_loader("CJKPDFReader")
loader = CJKPDFReader()

documents = loader.load_data("ailia_sdk.pdf")
index = GPTSimpleVectorIndex(documents)
index.save_to_disk('index.json')