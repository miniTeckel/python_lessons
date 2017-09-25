import os


def get_all_files(dir_path):
    return [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.splitext(f)[1] == ".sql"]


def print_files(files):
    for path in files:
        print(path)


def check_file(path, string):
    with open(path, "rt") as file:
        return (string in file.read())


def filter_files(files, string):
    return [p for p in files if check_file(p, string)]


if __name__ == "__main__":
    files = get_all_files(os.getcwd())
    print_files(files)
    while files:
        string = input("search string: ")
        files = filter_files(files, string)
        print_files(files)
    else:
        print("no such files")