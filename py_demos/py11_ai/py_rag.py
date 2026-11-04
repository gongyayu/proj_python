import numpy as np
from py_mod import line_print, st_print, code_print, st_code, st_markline, datadir, outputdir, dbdir, DOCUMENTS, debug
import streamlit as st
from pprint import pformat

from dotenv import load_dotenv
load_dotenv()

embed_model_name = "all-MiniLM-L6-v2"         # sentence-transformers/all-MiniLM-L6-v2
gen_model_name = "google/flan-t5-base"

debug = False
loading_debug = False
chunking_debug = False
embedding_debug = False
retrieving_debug = False


### StartofFunc###

######################
# loading KB 
######################
def py_01_load_json():
    from pathlib import Path
    import os
    import json
    from pprint import pformat

    rag_kb = 'rag_kb.jsonl'
    
    try:
        with open(str(datadir) + '/' + rag_kb,'r',encoding='utf-8') as fh:
            raw_kb = [json.loads(line) for line in fh]
    except Exception as e:
        st.error(f"Error: {str(e)}")
    if loading_debug:
        st.code(pformat(raw_kb))
        st_code(f"facts: {raw_kb}")  

        kbA = [line['fact'] for line in raw_kb]
        st_code(f"{kbA}")
        kbB = [(line['category'] + ':' +  line['fact']) for line in raw_kb]
        st_code(f"{kbB}")
    return raw_kb, kbA, kbB
### EndofCodeSection###    

def py_01_load_txt(): 
    def load_docs():
        from langchain_community.document_loaders import TextLoader

        try:
            loader = TextLoader(f"{str(datadir) + '/rag_kb.txt'}", encoding="utf8")
            documents = loader.load()
            if loading_debug:
                st_code(f"documents:\n{documents}")
        except Exception as e:
            st.code(f"Error: {str(e)}")
            return None
        return documents
    
    def load_text():
        try:
            with open(str(datadir) + '/' + 'rag_kb.txt','r') as fh:
                if loading_debug:
                    st_code(f"texts:\n{fh.read()}")
                return fh.read()
        except Exception as e:
            st.error(f"Error: {str(e)}")
    if loading_debug:
        load_docs()
        load_text()
    return load_docs, load_text
### EndofCodeSection###

##################
# chunking
##################
def py_02_chunking():  

    load_docs, load_text = py_01_load_txt()
    kb_docs = load_docs()                             # returned documents
    kb_text = load_text()  
    
    chunk_size = 100                           # returned texts

    def manual_chunking(text, chunk_size=100):
        """
        Splits the input text into chunks of specified size.
        Args:
            text (str): The input text to be chunked.
            chunk_size (int): The maximum size of each chunk.
        Returns:
            list: A list of text chunks.
        """
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    def rag_chunking(methods):
        from langchain_text_splitters import RecursiveCharacterTextSplitter

        if methods == 'langchain':
            text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=50, chunk_overlap=0)
            splitsDoc = text_splitter.split_documents(kb_docs)  
            splitsTxt = text_splitter.split_text(kb_text)
            if chunking_debug:
                code_print(f"spitsDoc:\n{rag_chunking()[0]}")
                code_print(f"{'-' * 50}")
                code_print(f"splitsTxt:\n{rag_chunking()[1]}")
                st_code(f"{code_print(f'')}")
            return splitsDoc,splitsTxt
        else:
            if chunking_debug:
                st_code(f"texts:\n{manual_chunking(kb_text)}")
            return [kb_text[i:i + chunk_size] for i in range(0, len(kb_text), chunk_size)]
    return rag_chunking
### EndofCodeSection###

def py_03_memEmbedding():
    from dotenv import load_dotenv
    load_dotenv()
       
    rag_chunking = py_02_chunking()
    chunks = rag_chunking('langchain')[1]

    # convert_to_numpy - whether the output should be a list  of numpy vector
    # normalize_embeddings - whether to normalize returned vectors to have length 1
    def LC_embedding():
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_community.embeddings import HuggingFaceEmbeddings
       
        embed_model = HuggingFaceEmbeddings(model_name = embed_model_name)
        LC_embeddings = embed_model.embed_documents(chunks)
        if embedding_debug:
            code_print(f"HuggingFaceEmbeddings")
            code_print(f"type of LC_embeddings: {type(LC_embeddings)}")
            code_print(f"LC_embeddings.shape: {np.array(LC_embeddings).shape}")
            st_code(f"{code_print(f'')}")
        return LC_embeddings,chunks

    def TF_embedding():
        from sentence_transformers import SentenceTransformer
        embed_model = SentenceTransformer(embed_model_name)
        TF_embeddings = embed_model.encode(chunks,convert_to_numpy=True, normalize_embeddings=True)
        if embedding_debug:
            code_print(f"SentenceTransformer")
            code_print(f"type of TF_ebeddings: {type(TF_embeddings)}")
            code_print(f"TF_embeddings.shape: {TF_embeddings.shape}")
            # code_print(f"{embeddings[:2]}")
            st_code(f"{code_print(f'')}")
        return TF_embeddings,chunks
        
    if embedding_debug:
        LC_embedding()
        TF_embedding()
        
    return LC_embedding, TF_embedding
### EndofCodeSection###

def py_03_dbEmbedding():
    from langchain_chroma import Chroma

    rag_chunking = py_02_chunking()

    def langchain_HF():
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_community.embeddings import HuggingFaceEmbeddings

        db = f"{str(dbdir) + '/rag_chromaHF_LC'}"
        chunks = rag_chunking('langchain')[0]                                               # list[Document]
        embedder = HuggingFaceEmbeddings(model_name = embed_model_name)
    
        HFvectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embedder,
            persist_directory=db,
        )
        if embedding_debug:
            resp = HFvectorstore.similarity_search("who created python?", k=3)
            st_code(f"resp: {resp[0].page_content}")
            st_code(f"embeddings: {HFvectorstore.embeddings}")
        return HFvectorstore

    def transformer_HF():
        from sentence_transformers import SentenceTransformer
        import chromadb

        db = f"{str(dbdir) + '/rag_chromaHF_TF'}"
        #
        # Step 1: embedding 
        #
        chunks = rag_chunking('langchain')[1]                                              
        embedder = SentenceTransformer(embed_model_name)   
        embeddings = embedder.encode(
            chunks,                                                                     # list[str]
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        if embedding_debug:
            st_code(f"embedding: \n{embeddings}")
        #
        # step 2: store embeddings to db
        #
        client = chromadb.PersistentClient(path=db)
        if embedding_debug:
            code_print(f"collections: {client.list_collections()}")
            for c in client.list_collections():
                code_print(f"collection: {c.name}")
        #client.delete_collection("db_collection")
        
        collection = client.get_or_create_collection("rag_collection")                  # get or create a table
        collection.add(                                                                 # add 
            ids = [str(i) for i in range(len(chunks))], 
            documents=chunks,
            embeddings=embeddings.tolist(),
        )
        if embedding_debug:
            result = collection.get(include=['embeddings', 'documents', 'metadatas'])
            code_print(f"result: {result}")
            st_code(f"{code_print(f'')}")   
        return collection   
    if embedding_debug:        
        langchain_HF()
        st_markline()
        transformer_HF()
    return langchain_HF, transformer_HF
### EndofCodeSection###

def py_04_dbRetrieving():
    debug = False
    vectorStore = py_03_dbEmbedding()

    if retrieving_debug:
        st.write(f"langchain HF receiving:")

    def HF_Retrieving():
        vectorHF = vectorStore[0]()
        user_prompt = "What is the company's vacation policy?"
        received = vectorHF.similarity_search(user_prompt, k=3)
        if retrieving_debug:
            st_code(f"received: {received}")
        return received

    def TF_retrieving():
        from sentence_transformers import SentenceTransformer

        st.write(f"HF Transformer receiving:")

        embedder = SentenceTransformer(embed_model_name)
        query_embedding = embedder.encode(
            ["What is the company's vacation policy?","who created python?"],
            normalize_embeddings=True
        )[1]

        collection = vectorStore[1]()
        if retrieving_debug:
            ret = collection.get(include=['embeddings', 'documents', 'metadatas'])
            st_code(f"collection.get(): {ret}")
        received = collection.query(
             query_embeddings = [query_embedding.tolist()],
             n_results=3,
             include=['documents',],
        )
        if retrieving_debug:
            st_code(f"received: {received}")
        return received
    if retrieving_debug:
        HF_Retrieving()
        TF_retrieving()
### EndofCodeSection###

def py_04_memRetrieving():
    top_k=3
    docs_embedder = py_03_memEmbedding()
    def LC_Retrieving():
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_community.embeddings import HuggingFaceEmbeddings

        docs_embeddings = docs_embedder[0]()[0]
        chunks = docs_embedder[0]()[1]

        embedder = HuggingFaceEmbeddings(model_name = embed_model_name)
        query_embeddings = embedder.embed_query("When and where did gongya get retired?")               # compare this with TF encode

        if retrieving_debug:
            st_code(f"docs_embeddings: {docs_embeddings}")
            st_code(f"query_embeddings: {query_embeddings}")

        return np.array(docs_embeddings),np.array(query_embeddings), chunks
           
    def TF_Retrieving():
        from sentence_transformers import SentenceTransformer

        docs_embeddings = docs_embedder[1]()[0]
        chunks = docs_embedder[1]()[1]

        if retrieving_debug:
            st_code(f"TF_embeddings: {docs_embeddings}")

        embedder = SentenceTransformer(embed_model_name)
        # This code generates a normalized, 1D NumPy embedding vector for a single search query using the sentence-transformers library.
        # Here is a quick breakdown:
        # [query]: Wraps the query string in a list (models expect a batch).
        # convert_to_numpy=True: Returns a NumPy array instead of a PyTorch tensor.
        # normalize_embeddings=True: Scales the vector to length 1 (L2 normalization), which makes calculating cosine similarity much faster (via dot product).
        # [0]: Unwraps the list to give you just the single vector.
        # re you looking to use this for vector search, or do you have a question about it?
        query_embeddings = embedder.encode(
                ["What is the company's vacation policy?","what is python?"], convert_to_numpy=True, normalize_embeddings=True
            )[0]
        if retrieving_debug:
            st_code(f"query_embeddings: {query_embeddings}")
        return docs_embeddings, query_embeddings, chunks

    def get_topK(langchain: bool):
        results = []
        d_embeddings, q_embeddings, chunks = LC_Retrieving()
        scores = d_embeddings @ q_embeddings
        top_indices = np.argsort(scores)[::-1][:top_k]
        results = [ chunk for index, chunk in enumerate(chunks) if index in top_indices ]
        if retrieving_debug:
            st_code(f"scores: {scores}")
            st_code(f"top_indices: {top_indices}")
            for i in top_indices:
                code_print(f"{chunks[i]} {float(scores[i])}")
            st_code(code_print(f''))
        return results
        
    if retrieving_debug:
        #LC_Retrieving()
        get_topK(True)
    return get_topK   
### EndofCodeSection###

def py_generation():
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline, AutoModelForCausalLM

    #get_topK = py_04_dbRetrieving()
    get_topK = py_04_memRetrieving()
    context = get_topK(True)
    query = 'When and where did gongya get retired?'

    prompt = (
            "Answer the question using only the context below.\n"
            f"Context:\n{context}\n\n"
            f"Question: {query}\n"
            "Answer:"
        )

    def load_generator():
        print(f"\n[3/3] Loading generator {gen_model_name} ...")
        tokenizer = AutoTokenizer.from_pretrained(gen_model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(gen_model_name)
        # model = AutoModelForCausalLM.from_pretrained(gen_model_name, tie_word_embeddings=False)              
        def generate(prompt, max_new_tokens=128):
            inputs = tokenizer(prompt, return_tensors="pt")
            output = model.generate(**inputs, max_new_tokens=max_new_tokens)
            return tokenizer.decode(output[0], skip_special_tokens=True).strip() 
        return generate

    generator = load_generator()
    text = generator(prompt)    
    st_code(f"query: {query}\nfinal answer: {text}")
### EndofCodeSection###

def pygeneration_bk():
    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from transformers import pipeline
    import transformers

    #print(transformers.__version__)

    documents = DOCUMENTS
    top_k=2
    query = ["who created python"]
    
    embed_model_name="all-MiniLM-L6-v2"
    gen_model_name="google/flan-t5-base"
    
    embedder = SentenceTransformer(embed_model_name)
    doc_embeddings = embedder.encode(
        documents, convert_to_numpy=True, normalize_embeddings=True
    )

    # return emdedding for Queries
    query_emb = embedder.encode(
        query, convert_to_numpy=True, normalize_embeddings=True
    )[0]

    #
    # if remove [0], will get the following
    # ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc 
    # signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 384)
    
    scores = doc_embeddings @ query_emb
    top_indices = np.argsort(scores)[::-1][:top_k]
    retrieved = [(documents[i], float(scores[i])) for i in top_indices]
    ## retrieved = [('Python is a high-level programming language created by Guido van Rossum in 1991.', 0.746315062046051), 
    ## ('RAG stands for Retrieval-Augmented Generation, combining a retriever with a language model.', 0.1926918625831604)]
    ### -------------------------------------------------------------------------------------

    context = "\n".join(f"- {doc}" for doc, _ in retrieved)
    #print(f"\n\n {'-' * 50}")
    code_print(f"context---: \n{context}")
    #
    # initialize the generator
    # generator = pipeline(
    #         "text2text-generation",
    #         model=gen_model_name,
    #         device=-1,
    # )   
    def load_generator():
        print(f"\n[3/3] Loading generator {gen_model_name} ...")
        tokenizer = AutoTokenizer.from_pretrained(gen_model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(gen_model_name)
        def generate(prompt, max_new_tokens=128):
            inputs = tokenizer(prompt, return_tensors="pt")
            output = model.generate(**inputs, max_new_tokens=max_new_tokens)
            return tokenizer.decode(output[0], skip_special_tokens=True).strip() 
        return generate

    prompt = (
        "Answer the question using only the context below.\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n"
        "Answer:"
    )

    code_print(f"Model: {gen_model_name}")
    code_print(f"Query: {repr(query)}")
    
    print(f"\n\nprompt---: \n{prompt}")
    # result = generator(
    #     prompt,
    #     max_new_tokens=256,
    #     do_sample=False,
    #     return_full_text=False,
    # )
    # print(f"\n\nresult---: {result}")
    # answer = result[0]["generated_text"].strip()
    # print(f"\n\nanswer---: {answer}") 

    generator = load_generator()
    text = generator(prompt)
    
    code_print(f"final answer: \n{text}")
    st_code(f"{code_print(f'')}")
    
### EndofCodeSection###







