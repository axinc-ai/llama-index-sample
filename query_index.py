import sys
import time

from llama_index import VectorStoreIndex
from llama_index import StorageContext, load_index_from_storage

# for debug
import langchain
langchain.verbose = True

# open index
start = int(round(time.time() * 1000))
storage_context = StorageContext.from_defaults(persist_dir='./storage')
loaded_index = load_index_from_storage(storage_context)
end = int(round(time.time() * 1000))
print(f'\tfrom_defaults processing time {end - start} ms')

args = sys.argv
if len(args) >= 2:
	question = args[1]
else:
	question = "ailia SDKが対応しているOSを教えてください。"

start = int(round(time.time() * 1000))
query_engine = loaded_index.as_query_engine(
    similarity_top_k=1
)
end = int(round(time.time() * 1000))
print(f'\tquery_engine processing time {end - start} ms')

start = int(round(time.time() * 1000))
output = query_engine.query(question)
print("Q: "+ question)
print("A: ", end="")
print(output)
end = int(round(time.time() * 1000))
print(f'\tquery processing time {end - start} ms')
