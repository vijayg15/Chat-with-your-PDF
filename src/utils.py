import os, json
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


def load_pdfs(path, extract_images = False):
    loader = PyPDFDirectoryLoader(path,
                                  glob = '**/[!.]*.pdf',
                                  extract_images = extract_images
                                  )
    documents = loader.load()
    return documents


def text_split(extracted_data, c_size=800, c_overlap=80):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=c_size, chunk_overlap=c_overlap)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


def download_embeddings(embd_model_name="text-embedding-3-small"):
    embeddings = OpenAIEmbeddings(
        model = embd_model_name,
        #dimensions=687
    )
    return embeddings


def initialize_llm(model_name, temp=0.6):
    llm = ChatOpenAI(
        model = model_name,
        temperature = temp,
    )
    return llm


def update_json(data, file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            loaded = json.load(file)
            loaded.append(data)
    else:
        loaded = [data]
            
    with open(file_name,"w") as f:
        json.dump(loaded, f, indent=2)
        f.close()   