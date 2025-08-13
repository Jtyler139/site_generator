import os
import shutil
from copystatic import copy_content_to_dir
from markdown_blocks import generate_page, generate_pages_recursive

def main():

    if os.path.exists("public"):
        shutil.rmtree("public")
    os.makedirs("public")

    copy_content_to_dir("static", "public")

    #generate_page("content/index.md", "template.html", "public/index.html")

    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()