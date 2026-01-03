import os
import shutil

def copy_static(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    copy_files_recursive(source, dest)

def copy_files_recursive(source, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_files_recursive(s, d)
        else:
            shutil.copy(s, d)
