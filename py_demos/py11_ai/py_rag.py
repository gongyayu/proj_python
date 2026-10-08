import numpy as np
from py_mod import line_print, st_print, code_print, st_code, st_markline

DOCUMENTS = [
        "The Eiffel Tower is located in Paris, France. It was completed in 1889.",
        "Python is a high-level programming language created by Guido van Rossum in 1991.",
        "The Great Wall of China is over 13,000 miles long and was built over many centuries.",
        "Transformers are a neural network architecture introduced in the paper 'Attention Is All You Need' (2017).",
        "RAG stands for Retrieval-Augmented Generation, combining a retriever with a language model.",
        "The capital of Japan is Tokyo, which is one of the most populous cities in the world.",
        "Photosynthesis is the process by which plants convert sunlight into chemical energy.",
        "The human genome contains approximately 3 billion base pairs of DNA.",
]

### StartofFunc###

def py_chunking():
    def load_text():
        with open('./data/in/rag_kb.txt','r') as fh:
            return fh.read()
        
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

    def rag_chunking():
        sample_text = load_text()
        chunks = manual_chunking(sample_text, chunk_size=20)
        code_print(f"{chunks}")
        code_print(f"Text Chunks:")
        for i, chunk in enumerate(chunks):
            code_print(f"Chunk {i + 1}: {chunk}")
        st_code(code_print(f''))
    rag_chunking()

    def langchain_chunking():
        st_markline()
        from langchain_community.document_loaders import TextLoader
        from langchain_text_splitters import RecursiveCharacterTextSplitter

        loader = TextLoader("data/in/rag_kb.txt", encoding="utf8")
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=100, chunk_overlap=0)
        splits = text_splitter.split_documents(documents)
        code_print(f"{splits}")
        st_code(code_print(f''))
        return splits
    langchain_chunking()
### EndofCodeSection###

def py_embedding():
    from sentence_transformers import SentenceTransformer
    DOCUMENTS = [
        "The Eiffel Tower is located in Paris, France. It was completed in 1889.",
        "Python is a high-level programming language created by Guido van Rossum in 1991.",
        # "The Great Wall of China is over 13,000 miles long and was built over many centuries.",
        # "Transformers are a neural network architecture introduced in the paper 'Attention Is All You Need' (2017).",
        # "RAG stands for Retrieval-Augmented Generation, combining a retriever with a language model.",
        # "The capital of Japan is Tokyo, which is one of the most populous cities in the world.",
        # "Photosynthesis is the process by which plants convert sunlight into chemical energy.",
        # "The human genome contains approximately 3 billion base pairs of DNA.",
    ]

    embed_model_name="all-MiniLM-L6-v2"
    gen_model_name="google/flan-t5-base"

    def HF_embedding(chunks):
        from dotenv import load_dotenv
        load_dotenv()

        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        # convert_to_numpy - whether the output should be a list  of numpy vector
        # normalize_embeddings - whether to normalize returned vectors to have length 1
        embeddings = model.encode(chunks,convert_to_numpy=True, normalize_embeddings=True)
        code_print(f"embeddings.shape: {embeddings.shape}")
        code_print(f"{embeddings}")
        st_code(f"{code_print(f'')}")
    HF_embedding(DOCUMENTS)
### EndofCodeSection###

def py_retrieve():
    from sentence_transformers import SentenceTransformer

    documents = DOCUMENTS
    top_k=3

    embed_model_name="all-MiniLM-L6-v2"
    gen_model_name="google/flan-t5-base"

    embedder = SentenceTransformer(embed_model_name)
    doc_embeddings = embedder.encode(
            documents, convert_to_numpy=True, normalize_embeddings=True
        )

    """Return the top_k most similar documents."""
    #
    # This code generates a normalized, 1D NumPy embedding vector for a single search query using the sentence-transformers library.
    # Here is a quick breakdown:
    # [query]: Wraps the query string in a list (models expect a batch).
    # convert_to_numpy=True: Returns a NumPy array instead of a PyTorch tensor.
    # normalize_embeddings=True: Scales the vector to length 1 (L2 normalization), which makes calculating cosine similarity much faster (via dot product).
    # [0]: Unwraps the list to give you just the single vector.
    # re you looking to use this for vector search, or do you have a question about it?
    query_emb = embedder.encode(
        ["what is python?"], convert_to_numpy=True, normalize_embeddings=True
    )[0]
    # Cosine similarity (vectors are normalized, so it's just dot product)
    scores = doc_embeddings @ query_emb
    top_indices = np.argsort(scores)[::-1][:top_k]
    for i in top_indices:
        code_print(f"{documents[i]} {float(scores[i])}")
    st_code(code_print(f''))

    return [(documents[i], float(scores[i])) for i in top_indices]
### EndofCodeSection###

def py_generation():
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from transformers import pipeline

    documents = DOCUMENTS
    top_k=2
    query = ["what is python", "Where is Effiel Tower located?"]
    
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
    print(f"\n\n {'-' * 50}")
    print(f"context---: {context}")
    #
    # initialize the generator
    generator = pipeline(
            "text-generation",
            model=gen_model_name,
            device=-1,
    )   

    prompt = (
        "Answer the question using only the context below.\n"
        f"Context:\n{context}\n\n"
        f"Question: {query}\n"
        "Answer:"
    )
    print(f"prompt---: {prompt}")
    result = generator(
        prompt,
        max_new_tokens=256,
        do_sample=False,
    )
    print(f"result---: {result}")
    answer = result[0]["generated_text"].strip()
    print(f"answer---: {answer}") 



### EndofCodeSection###


