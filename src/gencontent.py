import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[1:].strip()
    raise ValueError("no title found")

def generate_page(from_path, template_path, dest_path):
    print(f"generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    title = extract_title(markdown)
    node = markdown_to_html_node(markdown)
    html = node.to_html()

    with open(template_path, "r") as f:
        template = f.read()

    page_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dirpath = os.path.dirname(dest_path)
    if dirpath != "":
        os.makedirs(dirpath, exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(page_content)