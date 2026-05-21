# assistant

General app that automate certain actions, by following instructions through voice or text input. Follow the init menu to check current capabilities.

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have the modern Poetry package manager installed globally on your machine:

```bash
curl -sSL [https://install.python-poetry.org](https://install.python-poetry.org) | python3 -
```

### 2. Useful commands

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

Audit/Scan for vulnerabilities

Install audit plugin (if required)

```bash
poetry self add poetry-audit-plugin
```

Vulnerability check

```bash
poetry audit
```

Typosquatting, lock file integrity check

```bash
poetry check
```

### 3. Set up

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

### 4. Advanced use cases

If multiple python versions are found in the operative system, then

- use pyenv to handle the versions
- if needed set the local python for this project, like

```bash
pyenv local 3.14.3
```

- you can confirm all good by checking

```bash
pyenv which python
```

- set the specific python version like

```bash
poetry env use $USER_HOME/.pyenv/versions/3.14.3/bin/python
```

- then install using commands like the ones in the previous section

### 5. Requirements file

For generate requirements.txt file please execute:

```bash
pip3 freeze > requirements.txt
```

### 6. Launch

```bash
python3 src/main.py
```

## List of cool technologies in use here

- [Google Gen AI](https://ai.google.dev/gemini-api/docs)
- [Pyttsx3](https://github.com/nateshmbhat/pyttsx3)
- [Selenium](https://www.selenium.dev/)
- [Speech Recognition](https://github.com/Uberi/speech_recognition#readme)
- [YFinance](https://github.com/ranaroussi/yfinance)

## License

[MIT licensed](LICENSE).

## Stay in touch

- Author - [gal16v8d](https://github.com/gal16v8d)