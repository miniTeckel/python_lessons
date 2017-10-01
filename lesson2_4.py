import os
import glob

def get_all_files(dir_path):
    return glob.glob(dir_path)

def print_files(files):
    print('\n'.join(files))
    print("Всего: %d"%len(files))


def check_file(path, string):
    with open(path, "rt") as file:
        return string in file.read()


def filter_files(files, string):
    return [p for p in files if check_file(p, string)]


if __name__ == "__main__":
    migrations = 'Migrations'
    files = get_all_files(os.path.join(migrations, "*.sql"))

    print_files(files)
    while files:
        string = input("search string: ")
        files = filter_files(files, string)
        print_files(files)
    else:
        print("no such files")

