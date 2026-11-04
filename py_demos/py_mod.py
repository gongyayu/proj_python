import glob
import os
import re
import streamlit as st
import importlib
#
# for py99_files
#
import pathlib
from pathlib import Path
from datetime import datetime, timezone,timedelta
import time


options = False
debug = False
non_topic_list = ['py_data', '__pycache__', 'data','__init__']
_st = True
outlines = codelines = ''
py_proj_path = '/Users/gongya/Programming/mac_python/proj_python/py_demos/'

datadir = (Path(__file__).parent.parent.parent / 'data/in/').resolve()
outputdir = (Path(__file__).parent.parent.parent / 'data/out/').resolve()
dbdir = (Path(__file__).parent.parent.parent / 'data/db/').resolve()

# AI
llm_model = 'gpt-oss:latest'
ollama_model = 'llama3.1:8b'
ollama_URL = "http://localhost:11434/api/chat"

#
# files stats
#
startfrom = {
    #'AI':['/Volumes/192.168.1.57/AI/','/Users/gongya/obsidian/gyu-obsidian/6. References/Indexes/AI_Indexes.md'],
    'AI':['/Volumes/My Passport/AI/','/Users/gongya/obsidian/gyu-obsidian/6. References/Indexes/AI_Indexes.md'],
    'proj_python':['/Users/gongya/Programming/mac_python/proj_python/','/Users/gongya/obsidian/gyu-obsidian/6. References/Indexes/Python_Indexes.md'],
    'uv_python':['/Users/gongya/Programming/uv_python/','/Users/gongya/obsidian/gyu-obsidian/6. References/Indexes/Pythonuv_Indexes.md'],
    'proj_ai':['/Users/gongya/Programming/mac_python/proj_ai/','/Users/gongya/obsidian/gyu-obsidian/6. References/Indexes/PythonAI_Indexes.md'],
    'gyu_obsidian':['/Users/gongya/obsidian/gyu-obsidian/','/Users/gongya/obsidian/gyu-obsidian/6. References/Indexes/Obsidian_Indexes.md'],
    'music':['/Volumes/192.168.1.57/music/','/Users/gongya/obsidian/gyu-obsidian/6. References/Indexes/Music_Indexes.md']
}

bk_prefix = {
    '/Users/gongya/Programming/mac_python/proj_python/':'/Volumes/192.168.1.57/MAC_M5/latest/mac_python/proj_python/',
    '/Users/gongya/Programming/mac_python/proj_ai/':'/Volumes/192.168.1.57/MAC_M5/latest/mac_python/proj_ai/',
    '/Users/gongya/obsidian/gyu-obsidian/':'/Volumes/192.168.1.57/MAC_M5/latest/obsidian/gyu-obsidian/',
    '/Users/gongya/Programming/mac_python/':'/Volumes/192.168.1.57/MAC_M5/latest/mac_python/',
    '/Users/gongya/Programming/uv_python/':'/Volumes/192.168.1.57/MAC_M5/latest/uv_python/',
    '/Users/gongya/obsidian/':'/Volumes/192.168.1.57/MAC_M5/latest/obsidian/'
}

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

excludedirs = ['__pycache__','pycache']
days = 100

topdirlist = startfrom.keys()

# demo variables
def topic_list():
    topics = sorted([topic for topic in glob.glob(
        '*') if os.path.isdir(topic) and topic not in non_topic_list])
    topics.append('py99_files')
    return topics


def subtopic_list(topic):
    return [subtopic.split('/')[1] for subtopic in glob.glob(topic + '/*.py') if not os.path.isdir(subtopic) and re.search(r'^py(\d+)_', subtopic)]


def parsing_input() -> str:
    inFile = 'data/in/Parsing-input.txt'
    with open(inFile, 'r') as FH:
        return FH.read()


def get_func_info(mod_file):
    startoffunc = 0
    funcstart = 0
    funclist = []
    code_content = {}
    code_lines = ''
    code_def = 0

    with open(mod_file, 'r') as FH:
        for line in FH:
            # if (re.search(r'^\s*$',line)): continue
            if re.search(r'^###(\s)StartofFunc###', line):
                # funclist.append('null')
                startoffunc = 1
                continue
            if startoffunc == 1:
                if re.match(r'^def\s', line):
                    if code_lines == '':
                        code_lines = line
                        code_def = 1
                    # ln = re.sub(r'^def\s',"",line.strip(':')).split(':')[0]
                    # remove all trailing whilespaces
                    line = line.rstrip()
                    # remove the end :
                    ln = re.sub(r'^def\s', "", line.strip(':'))
                    funclist.append(ln)
                    funcstart = 1
                if re.match(r'###(\s)EndofCodeSection###', line):
                    code_content[ln] = code_lines
                    funcstart = 0
                    code_lines = ''
                    continue
                if funcstart == 1:
                    if code_def == 1:
                        code_def = 0
                        continue
                    code_lines += line
    return funclist, code_content


def func_details(mod_file, func_item, func_content):
    try:
        st.code(func_content[func_item], width="content")
    except Exception as e:
        print(f"Error: {str(e)}")
    if debug:
        st.write(mod_file, func_item)
    if re.search(r'^py_', func_item):
        f = re.sub(r'[\(|\):]', '', func_item)
        f = re.sub(r'\s+', '', f)

        mdir = mod_file.split('/')[-2]
        m = mod_file.split('/')[-1]
        m = re.sub(r'\.py', '', m)
        if st.button("run"):
            st.write(execute_func(mdir, m, f))


def execute_func(mod_dir, mod_name, func):
    # if mod_name in get_modlist(py_var.packages_dir):
    module = importlib.import_module(mod_dir + '.' + mod_name)
    func = getattr(module, func)
    func()

#
# py99_files
#
def get_all_directories(start_folder):
    """Return all directories recursively from a starting folder."""
    directories = [start_folder]
    for root, dirs, files in os.walk(start_folder):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for d in dirs:
            if d in excludedirs: continue
            directories.append(os.path.join(root, d))
    return directories

def listfiles(key, days, bkcheck, kword):
    dirs = get_all_directories(startfrom[key][0])
    if key != 'AI':
        bk_dirs = get_bk_dirs(bk_prefix[startfrom[key][0]])
    
    #keyword = 'RAG'
    keyword = None
    curfnlist = []

    with open(startfrom[key][1],'w') as fh:
        for d in dirs:           
            dir_path = pathlib.Path(d)
            filelist = []

            bkfilelists = bk_listfiles(d)
            for entry in dir_path.iterdir(): 
                if entry.is_file() and not re.search(r'^\.',entry.name):
                    mdate = datetime.fromtimestamp(entry.stat().st_mtime).date()
                    if int(days) > 0 :
                        if entry.stat().st_mtime < (int(time.time()) - (int(days) * 86400)): continue

                    if kword == None:
                        filelist.append([entry.name,str(mdate)])
                    else:
                        if re.search(r'{}'.format(kword), entry.name):
                            filelist.append([entry.name,str(mdate)])
            if len(filelist) > 0:
                curfnlist = []
                fh.write(f"#### {d}\n")
                st_print(f"##### {d}")
                for idx,fn in enumerate(sorted(filelist), start=1):
                    curfnlist.append(fn[0])
                    if fn[0] in bkfilelists:
                        if fn[1] > bkfilelists[fn[0]]:
                            fh.write(f"{idx}. {fn[0]},{fn[1]}  # updated: bk mtime - {bkfilelists[fn[0]]} ")
                            code_print(f"{idx}. {fn[0]},{fn[1]}  # updated: bk mtime - {bkfilelists[fn[0]]} ")
                        elif fn[1] == bkfilelists[fn[0]]:
                            if not bkcheck:
                                fh.write(f"{idx}. {fn[0]},{fn[1]}  # the same: bk mtime - {bkfilelists[fn[0]]} ")
                                code_print(f"{idx}. {fn[0]},{fn[1]}  # the same: bk mtime - {bkfilelists[fn[0]]} ")
                        else:
                            fh.write(f"{idx}. {fn[0]},{fn[1]}  # older: bk mtime - {bkfilelists[fn[0]]} ")
                            code_print(f"{idx}. {fn[0]},{fn[1]}  # older: bk mtime - {bkfilelists[fn[0]]} ")
                    else:
                        fh.write(f"{idx}. {fn[0]},{fn[1]}\n") 
                        code_print(f"{idx}. {fn[0]},{fn[1]}") 
                st_code(code_print(f""))

                if days == '0' and key != 'AI':
                    # trace the from backup files
                    idx = 1
                    bk_title = 0
                    
                    for bfile in bkfilelists.keys():
                        if curfnlist:
                            if bfile in curfnlist: continue
                            if bk_title == 0:
                                code_print(f"backup files only")
                                bk_title = 1
                            code_print(f"{idx}. {bfile}")
                            idx += 1
                    if idx > 1:
                        st_code(f"{code_print(f'')}")

                    st_markline()
                    final_print = 0
                    for bdir in bk_dirs:
                        if re.search(r'^/Volumes/192.168.1.57/MAC_M5/latest/mac_python/',bdir):
                            macdir = re.sub(r'^/Volumes/192.168.1.57/MAC_M5/latest/mac_python/','/Users/gongya/Programming/mac_python/', bdir)
                        elif re.search(r'^/Volumes/192.168.1.57/MAC_M5/latest/uv_python/',bdir):
                            macdir = re.sub(r'^/Volumes/192.168.1.57/MAC_M5/latest/uv_python/','/Users/gongya/Programming/uv_python/', bdir)
                        elif re.search(r'^/Volumes/192.168.1.57/MAC_M5/latest/obsidian/',bdir):
                            macdir = re.sub(r'^/Volumes/192.168.1.57/MAC_M5/latest/obsidian/','/Users/gongya/obsidian/', bdir)
                        if macdir not in dirs:
                            final_print = 1
                            code_print(f"{bdir}")
                    if final_print == 1:
                        st_code(f"{code_print(f'')}")               

def bk_listfiles(dir_path):
    bk_listfiles = {}
    if re.search(r"^/Users/gongya/Programming/mac_python", dir_path):
        bk_dir_path = re.sub(r'^/Users/gongya/Programming/mac_python','/Volumes/192.168.1.57/MAC_M5/latest/mac_python', dir_path)
    elif re.search(r"^/Users/gongya/Programming/uv_python", dir_path):
        bk_dir_path = re.sub(r'^/Users/gongya/Programming/uv_python','/Volumes/192.168.1.57/MAC_M5/latest/uv_python', dir_path)
    elif re.search(r"^/Users/gongya/obsidian/", dir_path):
        bk_dir_path = re.sub(r'^/Users/gongya/obsidian/','/Volumes/192.168.1.57/MAC_M5/latest/obsidian/', dir_path)
    else:
        return bk_listfiles

    if not os.path.exists(bk_dir_path):
        st.write(f'Error: {bk_dir_path} does not exist!')
        return bk_listfiles

    dir_path = pathlib.Path(bk_dir_path)
    for entry in dir_path.iterdir():
        if entry.is_file() and not re.search(r'^\.',entry.name):
            mdate = datetime.fromtimestamp(entry.stat().st_mtime).date()
            bk_listfiles[entry.name] = str(mdate)
    return bk_listfiles

def get_bk_dirs(bk_startfrom):
    bk_dirs = get_all_directories(bk_startfrom)
    return bk_dirs
    
### end of py99_files

def line_print(out: str) -> str:
    global outlines
    outlines += out + '<br>'
    return outlines


def code_print(out: str) -> str:
    global codelines
    if out:
        codelines += out + '\n'
    return codelines


def st_print(out: str):
    global outlines
    if _st:
        st.write(f'{out}', unsafe_allow_html=True)
        outlines = ''
    else:
        print(f'{out}')


def st_code(str):
    global codelines
    st.code(str, width='content', wrap_lines=True)
    codelines = ''


def st_markline():
    st.markdown("---")
