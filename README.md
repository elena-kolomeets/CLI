# CLI tools

Python command line interface tools

## create_gitignore
creates a .gitignore file with basic content: 

.DS_Store, .idea, .pytest_cache/, pycache/, *.spec, build/, dist/, venv/

You can just run the .exe file to create a .gitignore file in the same directory as the app 

or you can run it in terminal with or without optional arguments:
```
--path/-p : provide the path to create the .gitignore file outside of current directory
--add/-a : provide one file or directory name you wish to add to .gitignore file
```
