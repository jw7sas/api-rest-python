# -+- coding: utf-8 -*-
# imports
import json
from flask import render_template, request, jsonify, redirect, url_for, flash
from flask.views import View
from app.database import User

class WelcomeView(View):
    def dispatch_request(self):
        navData = [
            {"name": "001. Autenticarse Token", "id": "doc_000"},
            {"name": "002. Categorias", "id": "doc_001"},
            {"name": "003. Productos", "id": "doc_002"},
            {"name": "004. Clientes", "id": "doc_003"},
            {"name": "005. Tipos de pagos", "id": "doc_004"},
            {"name": "006. Facturas", "id": "doc_005"},
            {"name": "007. Detalle de facturas", "id": "doc_006"},
            {"name": "008. Usuarios", "id": "doc_007"}
        ]
        data = []
        with open('documentation.json', encoding='utf-8') as file:
            data = json.load(file)
        
        context = {
            'nav_data': navData,
            'data': data
        }
        return render_template("index.html", **context)

class LoginView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            if (not request.form.get("username")) or (not request.form.get("password")): 
                flash("Campos vacios por favor completelos")
            else:
                user = User.query.filter_by(username=request.form.get("username")).first()
                if user and user.check_password(request.form.get("password")):
                    return redirect(url_for('home_api'))
                else:
                    flash("El Usuario NO existe en el sistema")
        
        # Peticiones GET
        return render_template("pages/login.html")

class HomeView(View):
    def dispatch_request(self):
        return render_template("pages/home.html")
