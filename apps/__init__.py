from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from jinja2 import Environment

import config

# 创建SQLAlchemy实例
db = SQLAlchemy()

# 创建用户管理
login_manager = LoginManager()
login_manager.session_protection = 'strong'
# 登录视图对应蓝图auth的login
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    # 初始化数据库
    db.init_app(app)
    # 初始化用户管理
    login_manager.init_app(app)
    # 蓝本注册
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    from .operation import operation as op_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(main_blueprint, url_prefix='')
    app.register_blueprint(op_blueprint, url_prefix='/operation')
    return app