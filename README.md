# README

## Notepadify

A work in progress web app which allows users to generate a link to a text document, similar to Pastebin. Anybody with a link to a notepad can collaboratively edit it in real-time

### Screenshots

![Demo][./demo.gif]


### Setup

1. Create a venv
    python -m venv venv
    venv\Scripts\activate
2. Install python requirements
    pip install -r requirements.txt
3. Install client requirements
    cd client
    npm i requirements
4. Run server (cd to server directory)
    python manage.py runserver
5. Run client
    npm run dev