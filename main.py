import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            static_folder='assets',
            static_url_path='',
            template_folder='assets')

app.debug = os.environ.get('DYNO') is None
app.secret_key = 'some random key hahahah'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

db = SQLAlchemy(app)

from front import * # load code @UnusedWildImport


if __name__ == '__main__':
    app.run()
