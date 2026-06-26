from app.extensions import db
from app.utils import utc_now
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__="users"

    id = db.Column