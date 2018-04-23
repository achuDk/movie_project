# coding:utf8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# 会员数据模型
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)     # 编号
    name = db.Column(db.String(100),unique=True)    # 昵称
    pwd = db.Column(db.String(100))                 # 密码
    email = db.Column(db.String(100),unique=True)   # 邮箱
    phone = db.Column(db.String(11),unique=True)    # 电话
    info = db.Column(db.Text)                       # 个性签名
    face = db.Column(db.String(255),unique=True)    # 头像
    addtime = db.Column(db.DateTime,unique=True,default=datetime.utcnow)    # 注册时间
    uuid = db.Column(db.String(255),unique=True)    # 唯一标识符

