
from py_mod import line_print,st_print,code_print,st_code,st_markline, datadir

### StartofFunc###

def py_load_txt(): 
    def load_textA():
        from langchain_community.document_loaders import TextLoader

        loader = TextLoader(f"{str(datadir) + '/rag_kb.txt'}", encoding="utf8")
        documents = loader.load()
        #code_print(f"documents: {documents}")
        #st_code(f'{code_print(f'')}')
        return documents

    def load_textB():
        with open(str(datadir) + '/' + 'rag_kb.txt','r') as fh:
            return fh.read()
    return load_textA, load_textB
### EndofCodeSection###

def py_call_innerfuncs():
    load_text = py_load_txt()
    docsA = load_text[0]()
    docsB = load_text[1]()
    st_code(f"docsA: {docsA}")
    st_code(f"docsB: {docsB}")
    
### EndofCodeSection###