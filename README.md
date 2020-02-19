# Remote Locker

A remote locker created with Python for Windows to lock your computer when you are away from it.


# Getting Started:

Start the server at `server/server.js` ( it is already ready to run on [Heroku](https://heroku.com) ) and configure the `config.json` file.
After that, just run `locker.py` to start listening to the server and check if the computer lock has been requested.


# Generating an executable:

To create a executable, use [PyInstaller](https://pypi.org/project/PyInstaller/) by executing the following commands:

```
pip install PyInstaller
pyInstaller --icon=icon.ico --noconsole --hidden-import=pkg_resources --hidden-import=infi.systray locker.py -F 
```

