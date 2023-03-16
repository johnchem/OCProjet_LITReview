# Download of the files
- Go to the repertory where the application will be store
- In the repertory, copy the repertory from github
`git clone https://github.com/johnchem/OCProjet_LITReview.git`
# Instalation on Window
## Creation of the virtual environment
- Move into the project folder
`cd OCProjet_LITReview`
- Install the virtual environment
`python -m venv venv`
## Start the virtual environment
- `venv\Script\activate`
## Installation of the dependancies
- `python -m pip install -r requirement.txt.`
## launch the application
- start the virtual environment
`python -m venv venv`
- Start the server with the command
`python -m manage.py runserver`
- go to the application page with a webbrowser
`http://127.0.0.1:8000/`

# Instalation on Linux
## Creation of the virtual environment
- Move into the project folder
`cd OCProjet_LITReview`
- Install the virtual environment
`python3 -m venv venv`
## Start the virtual environment
- `source venv\bin\activate`
## Installation of the dependancies
- `python3 -m pip install -r requirement.py`
## launch the application
- start the virtual environment
`venv\Script\activate`
- Start the server with the command
`python litreview/manage.py runserver`