import argparse
import os

# os.getcwd() - current working directory
# os.path.abspath('.') - absolute path to cwd
# os.popen(filename, 'w'/'r') - open the file to write/read
# os.popen(filename)
# os.path.exists, os.path.isdir

ignore_files = ['.DS_Store\n', '.idea\n', '.pytest_cache/\n', '__pycache__/\n', '*.spec\n', 'build/\n', 'dist/\n',
                'venv/\n']


def create(path, ignore=None):
    with open("{}\\.gitignore".format(path), mode="a+", encoding="utf-8") as file:
        for i in ignore_files:
            file.seek(0)
            if i not in file.read():
                file.write(i)
        if ignore:
            if ignore not in file.read():
                file.write(ignore+'\n')


parser = argparse.ArgumentParser(prog=".gitignore creator",
                                 description="Creates a .gitignore file with basic content: .DS_Store, .idea, "
                                             ".pytest_cache/, __pycache__/, *.spec, build/, dist/, venv/",
                                 usage="Run without arguments to create .gitignore file with basic contents "
                                       "in the current directory or provide the path name and additional content to "
                                       "create/update .gitignore",
                                 add_help=True
                                 )
parser.add_argument('--path', '-p', type=str, help="To create .gitignore outside of current directory provide the path",
                    default=str(os.getcwd()))
parser.add_argument('--add', '-a', type=str, help="To add one file/folder to .gitignore provide its name")
args = parser.parse_args()
create(args.path, args.add)
