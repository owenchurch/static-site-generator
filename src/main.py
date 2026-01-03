import os
import shutil
from copystatic import copy_files_recursive
from gencontent import generate_page

static = "./static"
public = "./public"
content = "./content"
template = "./template.html"

def main():
    print("deleting public directory...")
    if os.path.exists(public):
        shutil.rmtree(public)

    print("copying static files to public directory...")
    copy_files_recursive(static, public)

    print("generating page...")
    for root, dirs, files in os.walk(content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                dest_path = os.path.join(public, os.path.relpath(root, content), file[:-3] + ".html")
                generate_page(from_path, template, dest_path)

if __name__ == "__main__":
    main()