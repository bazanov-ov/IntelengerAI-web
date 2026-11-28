import config
import os
import db_bowser
from main import app
from flask import Flask, render_template, redirect, json, jsonify, request
from flask_login import login_required, LoginManager


app.secret_key = os.environ['SECRET_KEY']  

login_manager = LoginManager()
login_manager.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  
login_manager.login_message = "Пожалуйста, войдите, чтобы открыть эту страницу." 




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 





@app.route("/")
def login():
    return render_template("login.html")


@app.route("/apps")
@login_required
def apps_dashbord():
    return render_template("apps.html")







# ------------------------------------------------------- Backend ------------------------------------------------------- #


@app.route("/api/create/account", methods=["GET", "POST"])  # <-- Добавлена запятая
def api_create_account():
    if request.method == "POST":  # <-- request.method в единственном числе + проверка на POST
        # Получаем данные (из JSON или из обычной HTML-формы)
        data = request.get_json(silent=True) or request.form
        
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Логин и пароль обязательны"}), 400

        # Проверяем, не занят ли логин
        if User.query.filter_by(username=username).first():
            return jsonify({"error": "Пользователь уже существует"}), 409

        # Создаём пользователя с хэшированным паролем
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        
        db_bowser.session.add(new_user)
        db_bowser.session.commit()

        return jsonify({"message": "Аккаунт успешно создан"}), 201

    # Если пришёл GET-запрос
    return jsonify({"message": "Отправьте POST-запрос с данными для регистрации"}), 200
