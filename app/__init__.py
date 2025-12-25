from flask import Flask
from config import Config
from app.extenshions import db, login_manager, migrate
from app.models import User
import os
from flask_login import current_user

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('templates'))
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.context_processor
    def inject_user():
        return dict(current_user = current_user)
    
    from app.routes.auth import auth
    from app.routes.complaints import complaint_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(auth)
    app.register_blueprint(complaint_bp)
    app.register_blueprint(admin_bp)

    with app.app_context():
        db.create_all()
    return app
