import os
import shutil
from copystatic import copy_content_to_dir

def main():

    copy_content_to_dir("static", "public")

if __name__ == "__main__":
    main()