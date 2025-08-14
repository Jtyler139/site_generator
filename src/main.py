import os
import shutil
import sys
from copystatic import copy_content_to_dir
from markdown_blocks import generate_page, generate_pages_recursive

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'

    copy_content_to_dir("static", "docs")

    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()