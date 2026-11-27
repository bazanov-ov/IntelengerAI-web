import os
import re
import uuid
import hashlib
import secrets
from main import app, config, psycopg2, SQLAlchemy, Bcrypt, UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from datetime import datetime
from sqlalchemy.orm import deferred
from sqlalchemy import UUID, text

# --- Инициализация БД ---
DB_USER = os.environ.get('DB_USER', config.DB_USER)
DB_PASSWORD = os.environ.get('DB_PASSWORD', config.DB_PASSWORD)
DB_HOST = os.environ.get('DB_HOST', config.DB_HOST)
DB_PORT = os.environ.get('DB_PORT', str(config.DB_PORT))
DB_NAME = os.environ.get('DB_NAME', config.DB_NAME)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
}
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)




# ------------------------------------------------------------------- Accounts ------------------------------------------------------------------- #

class account(db.Model, UserMixin):
    id = db.Column(db.UUID, unique=True, primary_key=True, default=db.func.gen_random_uuid())
    login = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    name_account = db.Column(db.String(50), nullable=False)
    lastname_account = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    def get_id(self):
        return f"account-{self.id}"


















# ------------------------------------------------------------------- QR-Auth ------------------------------------------------------------------- #