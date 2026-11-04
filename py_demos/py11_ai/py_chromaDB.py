import chromadb 
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer

from shared_mod.shared_mod import datadir
from shared_mod.shared_ai import get_kb, DB_PATHS

from dotenv import load_dotenv

_ = load_dotenv()


EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

### StartofFunc###

def create_chromaDB(db_name: str):
    try:
        chromaDB = chromadb.PersistentClient(path=DB_PATHS[db_name])
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
### EndofCodeSection###

def get_chromaDB(db_name):
    try:
        return chromadb.PersistentClient(path=DB_PATHS[db_name])
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
### EndofCodeSection###

def get_LC_vectorStore(chromaDB,collection_name: str):
    # Connect LangChain to the existing DB and collection
    
    if chromaDB:
        embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
        vectorstore = Chroma(
            collection_name=collection_name,
            client=chromaDB,
            embedding_function=embedder,
        )
    return vectorstore
### EndofCodeSection###

def get_collections(chromaDB):
    if chromaDB:
        collections = chromaDB.list_collections()
        # [Collection(name=rag_HF_collection), Collection(name=rag_TF_collection), Collection(name=rag_HF_collection2), Collection(name=rag_TF_collection2)]
        collection_names = [collection.name for collection in collections]
        return collections, collection_names
    else:
        return None
### EndofCodeSection###

def add_collection(chromaDB, collection_name: str, langchain: bool):

    if chromaDB:
        if collection_name in get_collections(chromaDB)[1]:
            print(f"The collection ({collection_name}) already exists")
            return None
        else:
            if langchain:
                # embedder = HuggingFaceEmbeddings(model_name = EMBED_MODEL)
                # vectorstore = Chroma(
                #     embedding_function=embedder,
                #     client=chromaDB,
                #     collection_name=collection_name,
                # )
                get_LC_vectorStore(chromaDB,collection_name)
            else:
                chromaDB.get_or_create_collection(collection_name)
    else:
        print(f"Error: chroma DB {chromaDB} does not exist.")

    #
    # collection attr
    #
    # collection.count()       # total records
    # collection.update()
    # collection.delete()
    #
### EndofCodeSection###

def del_collection(chromaDB, collection_name: str):
    if chromaDB:
        if collection_name in get_collections(chromaDB)[1]:
            chromaDB.delete_collection(collection_name)
        else:
            print(f"Error: the collection ({collection_name}) does not exist.")
    else:
        print(f"Error: the chromaDB does not exist.")
### EndofCodeSection###

def update_kb_prep(chromaDB, collection_name: str):
    if chromaDB is None:
        print(f"Error4: chromaDB does not exist.")
        return False
    
    collections, collection_names = get_collections(chromaDB)
    
    if collection_name not in collection_names:
        print("Error: the collection ({collection_name}) does not exist.")
        return False
    return collections
### EndofCodeSection###
    
def add_kb(chromaDB, collection_name: str, langchain: bool, kb_fname: str):
    import uuid

    if not update_kb_prep(chromaDB,collection_name):
        return
    
    kb_docs, kb_texts = get_kb(kb_fname)
    print(kb_docs)
    print(kb_texts)

    # Generate unique IDs for this batch of KB records
    ids = [str(uuid.uuid4()) for _ in kb_texts]

    if langchain:
        # Connect LangChain to the existing DB and collection
        vectorstore = get_LC_vectorStore(chromaDB,collection_name)
    
        vectorstore.add_documents(
            documents=kb_docs,
            ids=ids
        )
    else:                                                                                 # for Transformer
        collections, collection_names = get_collections(chromaDB)
        collection = next(
            (c for c in collections if c.name == collection_name),
            None,
        )
        embedder = SentenceTransformer(EMBED_MODEL)   
        kb_embeddings = embedder.encode(
            kb_texts,                                                                     # list[str]
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        collection.add(
            #ids = [str(i) for i in range(len(kb_texts))
            ids = ids,
            documents=kb_texts,
            embeddings=kb_embeddings.tolist(),
        )
### EndofCodeSection###

def del_kb(chromaDB, collection_name: str, langchain: bool, kb_fname: str):
    collections = update_kb_prep(chromaDB,collection_name)

    if not collections:
        return

    collection = next(
        (c for c in collections if c.name == collection_name),
        None,
        )

    if kb_fname == None:
        all_records, all_ids, all_docs = select_all(chromaDB, collection_name)
        if len(all_ids) > 0:
            collection.delete(ids = all_ids)
            print(f"All the records from this collection has been deleted.")
            return True
        else:
            print("This collection is empty.")
            return False
    else:
        kb_docs, kb_texts = get_kb(kb_fname)
        print(kb_texts)
        for each in kb_texts:
            records = collection.get(where_document={"$contains": each})
            print ('===',records)
            if len(records['ids']) > 0:
                collection.delete(ids=records['ids'])
                print(f"the record '{each}' has been deleted from the collection.")
            else:
                print(f"the record '{each}' does not exist.")

### EndofCodeSection###

##############################
# query
##############################
def select_topK(chromaDB, collection_name: str, user_query: str, langchain: bool):

    if langchain:
        vectorStore = get_LC_vectorStore(chromaDB, collection_name)
        resp = vectorStore.similarity_search("When did gongya get retired?", k=3)
        return resp
    else:
        embedder = SentenceTransformer(EMBED_MODEL)
        query_embeddings = embedder.encode(
                [user_query,],
                normalize_embeddings=True
        )[0]
        collections, collection_names = get_collections(chromaDB)
        collection = next(
                    (c for c in collections if c.name == collection_name),
                    None,
                )
        resp = collection.query(
            query_embeddings=query_embeddings,
            n_results=3,
            include=['documents',]
        )
    return resp
### EndofCodeSection###

def select_all(chromaDB, collection_name: str):

    collections, collection_names = get_collections(chromaDB)
        
    if collection_name not in collection_names:
        print("Error: the collection ({collection_name}) does not exist.")
        return
    
    collection = next(
        (c for c in collections if c.name == collection_name),
        None,
    )

    all_records = collection.get()
    all_ids = all_records['ids']
    all_docs = all_records['documents']
    # all_embeddings = all_records['embeddings']
    # metadatas = [metadata['source'] for metadata in resp['metadatas']]
    return all_records, all_ids, all_docs
### EndofCodeSection###


################################################################################
# AI chroma DB Demo version
################################################################################
def rag_chromadb():
    kb_docs, kb_texts = get_kb()
  
    def rag_LC_chromadb():
        embedder = HuggingFaceEmbeddings(model_name = EMBED_MODEL)
        vectorstore = Chroma.from_documents(
            documents=kb_docs,
            embedding=embedder,
            persist_directory=datadir + "/db/LC_chroma_db",
            collection_name='HF_rag_collection',
        )
        collection = vectorstore._collection_name
        return vectorstore, collection
    #LC_chromadb()

    def rag_TF_chromaDB():
        embedder = SentenceTransformer(EMBED_MODEL)   
        kb_embeddings = embedder.encode(
            kb_texts,                                                                     # list[str]
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        chromaDB = chromadb.PersistentClient(path=f"{datadir}/db/TF_chroma_db")
        collection = chromaDB.get_or_create_collection("TF_rag_collection")
        collection.add(
            ids = [str(i) for i in range(len(kb_texts))],
            documents=kb_texts,
            embeddings=kb_embeddings,
        )
        return collection
    return rag_LC_chromadb, rag_TF_chromaDB
### EndofCodeSection###

def get_topK():
    HF_vectors, TF_collection = rag_chromadb()
    
    def HF_vectors_query():
        resp = HF_vectors()[0].similarity_search("When did gongya get retired?", k=3)
        return resp

    def TF_collection_query():
        embedder = SentenceTransformer(EMBED_MODEL)
        query_embeddings = embedder.encode(
                ["When did gongya get retired?","who created python?"],
                normalize_embeddings=True
        )[0]
        resp = TF_collection().query(
            query_embeddings=query_embeddings,
            n_results=3,
            include=['documents',]
        )
        return resp
    return HF_vectors_query, TF_collection_query
### EndofCodeSection###

#############################################################################################
# End of AI chroma
#############################################################################################

def test():
    #################################
    # chromaDB 
    #################################
    # create_chromaDB('legal')
    chromaDB = get_chromaDB('rag')
    #################################
    # collection
    #################################
    print(get_collections(chromaDB)[1])
    # add_collection(chromaDB,'rag_TF_collection',True)
    #
    # del_collection(chromaDB,'rag_HF_collection')
    # print(get_collections(chromaDB)[1])
    #################################
    # Add records
    #################################
    # add_kb(chromaDB,'rag_TF_collection',True, 'rag_kb_add.txt')
    # del_kb(chromaDB,'rag_HF_collection',True, None)
    # del_kb(chromaDB,'rag_HF_collection',True, 'rag_kb_add.txt')

    #################################
    # select
    #################################
    # user_query = 'how often does gongya to back China?'
    # resp = select_topK(chromaDB,'rag_HF_collection',user_query, True)
    # ids = [doc.id for doc in resp]
    # metadatas = [doc.metadata['source'] for doc in resp]
    # page_contents = [doc.page_content for doc in resp]
    # print(ids)
    # print(metadatas)
    # print(page_contents)

    all_recodrs, all_ids, all_docs = select_all(chromaDB,'rag_TF_collection')
    print('----- All records -----')
    print(all_recodrs)
    print()
    print(all_ids)
    print()
    print(all_docs)
    
### EndofCodeSection###
   
if __name__ == "__main__":
    test()
    
    


        