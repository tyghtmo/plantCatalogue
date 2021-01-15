# plantCatalogue
A site using the trefle.io plants API.

Made using Django & Python

## Development Setup:
Ensure Python3, pip and virtualenv are installed

Clone repo to local machine

cd into repo

## Environmental Variables
Add 'TREFLETOKEN' Env variable for API key
Add 'SECRET_KEY=xxx' Env variable for Django security
Add 'DEBUG=True' for local use or false for production

## Start Server
In PowerShell or terminal run:

`virtualenv ENV`

`ENV\Scripts\activate`

`pip install -r requirements.txt`

`python ./manage.py migrate`

`python ./manage.py runserver`
