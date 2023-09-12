from dotenv import load_dotenv
load_dotenv()

from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer

# Load HTML
loader = AsyncChromiumLoader(["https://phptravels.com"])
html = loader.load()

#Transform
bs_transformer = BeautifulSoupTransformer()
docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["span"])

#Result
print(docs_transformed[0].page_content[0:500])