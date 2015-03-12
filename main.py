import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


IS_PROD = os.environ.get('DYNO') != None

app = Flask('FluidLending',
            static_folder='assets',
            static_url_path='',
            template_folder='assets')

app.debug = os.environ.get('DYNO') is None
app.secret_key = 'some random key hahahah'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'] if IS_PROD else 'sqlite:///sqlite.db'

if IS_PROD:
    from flask_sslify import SSLify
    SSLify(app)   

db = SQLAlchemy(app)

#======================= IMPORT MODULES ======================
from models import *        
from front import * # @NoMove @UnusedWildImport

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        app.run()
    else:
        if sys.argv[1] == 'shell':
            import code
            code.interact("\n>>> %s %s shell. Try dir()" % ('PRODUCTION' if IS_PROD else 'localdev', app.name), local=locals())
        elif sys.argv[1] == 'db_init':
            db.create_all()
