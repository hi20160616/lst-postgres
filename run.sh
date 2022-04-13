. venv/bin/activate
sudo waitress-serve --port=80 --call 'flaskr:create_app'
