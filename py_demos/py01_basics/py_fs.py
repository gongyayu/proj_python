from mcp import os
import streamlit as st
from pprint import pformat
import json

from shared_mod.shared_mod import line_print, st_print, st_code, code_print, st_markline

### StartofFunc###

def py_directories():
    from pathlib import Path
    import os

    def dir_pathlib():  
        code_print(f"Path(__file__): {Path(__file__)}")                                                                        # seems no difference with resolve or without resolve
        code_print(f"Path(__file__).parent / '__pycache__').resolve(): {(Path(__file__).parent / '__pycache__').resolve()}")
        code_print(f"Path(os.path.dirname(__file__)): {Path(os.path.dirname(__file__))}")                                      # vs. os.path.dirname(__file__)
        st_code(f"{code_print(f'')}")
    dir_pathlib()
    
    st_markline()
    def dir_os(): 
        code_print(f"os.path: {os.path} \ndir(os.path): {dir(os.path)}")
        # the directory where the current script runs. vs. getcwd() which returns the current working directory of the main script
        code_print(f"os.path.dirname(__file__): {os.path.dirname(__file__)}")              
        code_print(f"os.path.abspath('.'): {os.path.abspath('.')}")
        code_print(f"os.path.exists('./data'): {os.path.exists('./data')}")
        
        code_print(f"os.getcwd(): {os.getcwd()}")  
        st_code(f"{code_print(f'')}")
    dir_os()

    st_markline()
    def dir_recursive():  
        code_print(f"os.listdir('.'): {os.listdir('.')}")   
        code_print(f" ") 
        code_print(f"Path('.').iterdir(): {list(Path('.').iterdir())}")
        code_print(f" ") 
        entrylist = []
        for entry in Path('.').iterdir():
            entrylist.append(entry)
        code_print(f"entry: {entry}, type: {type(entry)} \n\ndir(entry): {dir(entry)}")

        code_print(f" ")
        code_print(f"os.walk:")
        for root, dirs, files in os.walk('./data'):
            code_print(f"root: {root}, dirs: {dirs}, files: {files}")     
        
        
        st_code(f"{code_print(f'')}")
    dir_recursive()

    def dir_ops():
        code_print(f"os.makedirs('./data/out/test_folder', exist_ok=True): {os.makedirs('./data/out/test_folder', exist_ok=True)}")

### EndofCodeSection###

def py_files():
    from pathlib import Path

    def file_access():
        import os
        import glob
        from pathlib import Path

        contents = glob.glob('*.py')
        files = [file for file in contents if not os.path.isdir(file)]
        code_print(f'files: {files}, path: {Path(files[0])}, file: {files[0]}')
        
        code_print(f" ")
        cachedir = (Path(__file__).parent).resolve()
        files = list(cachedir.glob("py_*.py"))                                        # convert glob to a list as glob returns an iterator which will be consumed once. See Obsidian from gpt

        code_print(f"files[:3]: {files[:3]}")
        code_print(f"(files[0].read_text.splitlines())[:2]: {(files[0].read_text().splitlines())[:2]}")

        code_print(f" ")
        file_names = [str(path.relative_to(cachedir)) for path in files]            # return all the files
        code_print(f"file_names: {file_names}")
        st_code(f"{code_print(f'')}")

        code_print(f" ")
        kbdir = (Path(__file__).parent.parent.parent / 'data/in').resolve()   
        code_print(f"kbdir: {type(kbdir)}, {str(kbdir)}") 
        try: 
            with open(str(kbdir) + '/sample-simple.json','r',encoding='utf-8') as fh:   # str function converts postfix to a string for concate
                code_print(f"successful open the file.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
        st_code(f"{code_print(f'')}")
    file_access()
   
    def pyrename():
        # Path(file).rename(Path(new_file))
        pass  

    def pyremovefile():
        file_path = './data/out/test_folder/test_file.txt'
        if os.path.exists(file_path):
            os.remove(file_path) 
### EndofCodeSection###

def pysearchforfiles():
    import re
    foundlist = []
    cnt = 0
    searchfor = input("Search for: ")
    for fname in os.listdir('/Volumes/192.168.1.57/music'):
        if re.search(r'{}'.format(searchfor).lower(), fname.lower()):
            foundlist.append(fname)
            cnt += 1
    if len(foundlist) > 0:
        for each in foundlist:
            print(each)
        print(f"Total: {cnt}")
    else:
        print(f"Nothing found.")
### EndofCodeSection###

def pylistallfiles():
    import os
    import re
    import pathlib

    def listfiles():
        dirs = get_all_directories('/Volumes/192.168.1.57/Topics/AI/')
        index_file = '/Users/gongya/obsidian/gyu-obsidian/6. References/Indexes.md'
        keyword = 'RAG'

        with open(index_file,'w') as fh:
            for d in dirs:           
                dir_path = pathlib.Path(d)
                idx = 1
                filelist = []
                for entry in dir_path.iterdir(): 
                    if entry.is_file():
                        if keyword == None:
                            filelist.append(entry.name)
                        else:
                            if re.search(r'{}'.format(keyword), entry.name):
                                filelist.append(entry.name)
                if len(filelist) > 0:
                    fh.write(f"#### {d}\n")
                    for idx,fn in enumerate(sorted(filelist), start=1):
                        fh.write(f"{idx}. {fn}\n")  
                        

        def get_all_directories(start_folder):
            """Return all directories recursively from a starting folder."""
            directories = []
            for root, dirs, files in os.walk(start_folder):
                dirs[:] = [d for d in dirs if not d.startswith('.')]   # exclude dir starting with dot
                for d in dirs:
                    directories.append(os.path.join(root, d))
            return directories
### EndofCodeSection###

def py_filesize():
    import os

    def get_folder_size(folder):
        total_bytes = 0
        # through the folder
        for root, dirs, files in os.walk(folder):
            #print(root, dirs, files)
            for filename in files:
                file_path = os.path.join(root, filename)
                # whether a file or not
                if os.path.isfile(file_path):
                    total_bytes = os.path.getsize(file_path)
                    # to MB
                    total_mb = total_bytes / 1024 / 1024
                    code_print(f"the size of the file {(file_path)}: {total_bytes} bytes, {total_mb: .2f} MB")
        st_code(f"{code_print(f'')}")
        return total_mb

    target_dir = "./data"
    if os.path.exists(target_dir):
        get_folder_size(target_dir)
    else:
        st_code(f"{target_dir} does not exists !")
### EndofCodeSection###

def pyarrangefiles():
    import os
    import shutil

    def arrange_files_by_extension(source_folder, destination_folder):
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        for filename in os.listdir(source_folder):
            file_path = os.path.join(source_folder, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1][1:]  # Get the extension without the dot
                if file_extension:  # Only proceed if there is an extension
                    ext_folder = os.path.join(destination_folder, file_extension)
                    if not os.path.exists(ext_folder):
                        os.makedirs(ext_folder)
                    shutil.move(file_path, os.path.join(ext_folder, filename))
                    code_print(f"Moved {filename} to {ext_folder}")

    source_dir = "./data"
    dest_dir = "./data/organized"
    arrange_files_by_extension(source_dir, dest_dir)
    st_code(f"{code_print(f'')}")

    file_type_map = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
        'Documents': ['pdf', 'doc', 'docx', 'txt', 'xls', 'xlsx', 'ppt', 'pptx'],
        'Audio': ['mp3', 'wav', 'aac', 'flac'],
        'Video': ['mp4', 'avi', 'mkv', 'mov'],
        # Add more categories and extensions as needed
    }

    def get_file_category(extension):
        for category, extensions in file_type_map.items():
            if extension.lower() in extensions:
                return category
        return 'Others'
### EndofCodeSection###
