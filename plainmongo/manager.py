from config import app
from flask_mongoengine import MongoEngine
from config import Roles
from config import Users

app.config['MONGODB_SETTINGS'] = {
    'db': 'sample1',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)
