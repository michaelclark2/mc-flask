from flask import Flask, g
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_cors import CORS
from flask_github import GitHub

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)
github = GitHub(app)

@github.access_token_getter
def token_getter():
    return app.config['GITHUB_TOKEN']


from app import routes, models