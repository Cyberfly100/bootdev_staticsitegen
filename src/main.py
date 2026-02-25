from filemanagement import copy_static_files
from page_generator import generate_pages_recursive
def main():
    current_wd = "/".join(__file__.split("/")[:-2])

    copy_static_files(current_wd, log=False)
    generate_pages_recursive(
        dir_path_content=f"{current_wd}/content",
        template_path=f"{current_wd}/template.html",
        dest_dir_path=f"{current_wd}/public"
    )

if __name__ == "__main__":
    main()
