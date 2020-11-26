## CLI create_gitignore
Python CLI made with argparse that creates a .gitignore file with basic content: 

* .DS_Store, .idea/, **pycache/, *.spec, build/, dist/, **bin/, *.sh, venv/

You can just run the .exe file to create a .gitignore file in the same directory as the app 

or you can run .exe or .py file in the terminal with or without optional arguments:
```
--path [path] /-p [path] : provide the path to create the .gitignore file outside of current directory
--add [file] /-a [file]  : provide one or multiple file or directory names you wish to add to .gitignore file
--help/-h                : shows help message
```
