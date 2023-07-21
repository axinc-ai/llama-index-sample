import requests
import os

from llama_index import VectorStoreIndex
from llama_index import download_loader

CJKPDFReader = download_loader("CJKPDFReader")
loader = CJKPDFReader()

path = "AR02ALA_UM01_21J.pdf"

documents = []
document = loader.load_data(path)
doc = document[0]
doc.text = doc.text.replace("、", "、 ")
doc.text = doc.text.replace("。", "。 ")
documents.append(doc)

index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir="./storage")

