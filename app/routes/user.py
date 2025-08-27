from flask import Blueprint,request,render_template
from ..models import User
from app.config import config


user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@user_bp.route('/ceshi')
def ceshi():
    return render_template('ceshi.html')
@user_bp.route('/ceshi1',methods=['POST'])
def ceshi1():
    username = request.form.get('username')
    password = request.form.get('password')
    print(User.adduser(username,password))
    return "ok"