from flask import Flask

app = Flask(__name__)

# PostgreSQLを使用する場合には、コメントアウトを外してください。
# from sqlalchemy.orm import DeclarativeBase
# from flask_sqlalchemy import SQLAlchemy
# 
# class Base(DeclarativeBase):
#   pass
# 
# db = SQLAlchemy(model_class=Base)
# POSTGRES_USER = "postgres"
# POSTGRES_PASSWORD = "postgres"
# app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
# db.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"