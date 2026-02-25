from filemanagement import copy_static_files
from page_generator import generate_pages_recursive
import sys

def main():
    current_wd = "/".join(__file__.split("/")[:-2])
    args = sys.argv
    basepath = args[1] if len(args) > 1 else "/"
    target_dir = "docs"

    copy_static_files(current_wd, target_dir, log=False)
    generate_pages_recursive(
        dir_path_content=f"{current_wd}/content",
        template_path=f"{current_wd}/template.html",
        dest_dir_path=f"{current_wd}/{target_dir}",
        basepath=basepath,
        log=False,
    )

if __name__ == "__main__":
    main()
