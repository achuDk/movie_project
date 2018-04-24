# coding:utf8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# 会员数据表结构
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
    userlogs = db.relationship("Userlog",backref="user") # 会员日志外键关系关联

    def __repr__(self):
        return "User %r" %self.name

# 登录日志数据表结构
class Userlog(db.Model):
    id = db.Column(db.Integer,primary_key=True)             # 编号
    user = db.Column(db.Integer,db.ForeignKey('user.id'))   # 所属会员
    ip = db.Column(db.String(100))                          # 登录IP地址
    addtime = db.Column(db.DataTime,unique=True,default=datatime.utcnow)    #登录时间

    def __repr__(self):
        return "Userlog %r" %self.id