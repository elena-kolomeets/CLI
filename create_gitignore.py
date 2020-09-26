import argparse
import os
import sys

ignore_files = ['.DS_Store\n', '.idea\n', '.pytest_cache/\n', '__pycache__/\n', '*.spec\n', 'build/\n', 'dist/\n',
                'venv/\n']


def create(path, ignore=None):
    if os.path.exists(path):
        with open("{}\\.gitignore".format(path), mode="a+", encoding="utf-8") as file:
            for i in ignore_files:
                file.seek(0)
                if i not in file.read():
                    file.write(i)
            if ignore:
                print(ignore)
                for j in ignore:
                    file.seek(0)
                    if j+'\n' not in file.read():
                        file.write(j+'\n')
    else:
        print("Error: The specified path does not exist", file=sys.stdout)


def main():
    parser = argparse.ArgumentParser(prog=".gitignore creator",
                                         description="Creates a .gitignore file with basic content: .DS_Store, .idea, "
                                                     ".pytest_cache/, __pycache__/, *.spec, build/, dist/, venv/; "
                                                     "additional files can be added and the path can be specified.",
                                         usage="Run without arguments to create .gitignore file with basic contents "
                                               "in the current directory or provide the path name and additional "
                                               "content to create/update .gitignore",
                                         add_help=True
                                         )
    parser.add_argument('--path', '-p', type=str, help="To create .gitignore outside of the current directory provide "
                                                       "the path",
                            default=str(os.getcwd()))
    parser.add_argument('--add', '-a', type=str, nargs='*', help="To add one or multiple files/folders to .gitignore "
                                                                 "provide their names (separate with space)")
    args = parser.parse_args()
    create(args.path, args.add)


if __name__ == '__main__':
    main()
