from filemanagement import copy_static_files

def main():
    current_wd = "/".join(__file__.split("/")[:-2])

    copy_static_files(current_wd, log=False)

if __name__ == "__main__":
    main()
