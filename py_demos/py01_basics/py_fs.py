import streamlit as st
import os
import pathlib
from py_mod import line_print, st_print, st_code, code_print, st_markline
from pprint import pformat

### StartofFunc###
def py_fspkg():
    import os
    import pathlib

    code_print(f"os.getcwd: {os.getcwd()}")  
    code_print(f"os.listdir('.'): {os.listdir('.')}")

    for root, dirs, files in os.walk('./data'):
        code_print(f"root: {root}, dirs: {dirs}, files: {files}")     
    code_print(f"os.makedirs('./data/out/test_folder', exist_ok=True): {os.makedirs('./data/out/test_folder', exist_ok=True)}")
    
    code_print(f"{'-' * 30 }")
    code_print(f"os.path: {os.path} \ndir(os.path): {dir(os.path)}")
    # the directory where the current script runs. vs. getcwd() which returns the current working directory of the main script
    code_print(f"os.path.dirname(__file__): {os.path.dirname(__file__)}")              
    code_print(f"os.path.abspath('.'): {os.path.abspath('.')}")
    code_print(f"os.path.exists('./data'): {os.path.exists('./data')}")
    
    code_print(f"{'-' * 30 }")
    code_print(f"pathlib.Path(os.path.dirname(__file__)): {pathlib.Path(os.path.dirname(__file__))}")
    # return a list of names of the entries in the directory given by the path
    code_print(f"pathlib.Path('.').iterdir(): {list(pathlib.Path('.').iterdir())}")
    entrylist = []
    for entry in pathlib.Path('.').iterdir():
        entrylist.append(entry)
    code_print(f"\npathlib.path('.').iterdir(): {entrylist} \n\nentry: {entry}, type: {type(entry)} \n\ndir(entry): {dir(entry)}")
    
    st_code(f"{code_print(f'')}")
### EndofCodeSection###

    
def py_files():
    def pyglob():
        import glob
        from pathlib import Path
        contents = glob.glob('*.png')
        files = [file for file in contents if not os.path.isdir(file)]
        st_code(f'files: {files}, path: {Path(files[0])}, file: {files[0]}')

    def pyrename():
        # Path(file).rename(Path(new_file))
        pass
    pyglob()
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
