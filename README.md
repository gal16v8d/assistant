# assistant

General app that automate certain actions, by following instructions through voice or text input. Follow the init menu to check current capabilities.

# Get started

## Unix

Install poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Init repo:

```bash
poetry new assistant
```

Create the virtual env folder:

```bash
mkdir .venv
```

Install all the dependencies in the project (clean-state):

```bash
poetry install
```

Install any dependency you need:

```bash
poetry add lib_here
```

Remove a dependency you don't need:

```bash
poetry remove lib_here
```

# Set up

# env

Activate using the command:

```bash
source .venv/bin/activate
```

or poetry 2.0 or above syntax

```bash
eval $(poetry env activate)
```

Exit virtual env:

```bash
exit
```

or

```bash
deactivate
```

# Advanced use cases

If multiple python versions are found in the operative system, then

- use pyenv to handle the versions
- if needed set the local python for this project, like

```bash
pyenv local 3.13.3
```

- you can confirm all good by checking

```bash
pyenv which python
```

- set the specific python version like

```bash
poetry env use $USER_HOME/.pyenv/versions/3.13.3/bin/python
```

- then install using commands like the ones in the previous section

## Windows

Update pip:

```bash
py -m pip install --upgrade pip
```

Install python3-venv:

```bash
py -m pip install virtualenv
```

Then create the folder for allocate the virtual environment:

```bash
py -m virtualenv env
```

Optional (run if UnauthorizedAccess in powershell console):

```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```

Then activate the virtual env:

```bash
.\venv\Scripts\activate.ps1
```

Now you can install python libs as you need it

# set up

Configure all your dependencies in Pipfile.
See: [Pypi](https://pypi.org/)

# dependencies

For generate requirements.txt file please execute:

```bash
pip3 freeze > requirements.txt
```

# launch

## Unix

```bash
python src/app.py
```

## Windows

```bash
py src/app.py
```

## List of cool technologies in use here

- [Pyttsx3](https://github.com/nateshmbhat/pyttsx3)
- [Selenium](https://www.selenium.dev/)
- [Speech Recognition](https://github.com/Uberi/speech_recognition#readme)
- [YFinance](https://github.com/ranaroussi/yfinance)

## License

[MIT licensed](LICENSE).

## Stay in touch

- Author - [gal16v8d](https://github.com/gal16v8d)