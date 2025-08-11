import os
import shutil

def copy_content_to_dir(source, destination):
        if not os.path.exists(source):
            raise Exception("the source directory does not exist")
        if os.path.exists(destination):
            shutil.rmtree(destination)
        os.mkdir(destination)

        source_items = os.listdir(source)
        for item in source_items:
            full_path = os.path.join(source, item)
            if os.path.isfile(full_path):
                shutil.copy(full_path, destination)
                print(f"Added file: {item}")
            else:
                os.mkdir(os.path.join(destination, item))
                print(f"Added directory: {item}")
                copy_content_to_dir(full_path, os.path.join(destination, item))