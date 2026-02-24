from filemanagement import copy_static_files
from page_generator import generate_page
def main():
    current_wd = "/".join(__file__.split("/")[:-2])

    copy_static_files(current_wd, log=False)
    generate_page(
        from_path=f"{current_wd}/content/index.md",
        template_path=f"{current_wd}/template.html",
        dest_path=f"{current_wd}/public/index.html"
    )

if __name__ == "__main__":
    main()
