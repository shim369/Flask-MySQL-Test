class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flask_todolist'
    SQLALCHEMY_TRACK_MODIFICATIONS = False