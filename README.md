# ProntoPlus
Toy project for an app that maintains a registry of medics/patients and their medical records, with the following features:
* Agnostic database compatibility 
* Rich text editor
* License control
* Cross-platform via PyQt
* Extendable through the MVC architecture
* External configuration via config.ini file

# Running in your machine

First, clone this repository with 
```shell
git clone https://github.com/akelopes/ProntoPlus
```

Then, install the requirements with:
```shell
pip install -r requirements.txt
```

After that, just run the app with the following commands:
```shell
cd ProntoPlus
python app.py
```

In order to compile this into an app, use [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/).
