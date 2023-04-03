"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgdtdng2qv2bbhllef70-a.oregon-postgres.render.com",
        database="todo_app_ajbk",
        user="todo_app_ajbk_user",
        password="SiTVSnmNV8GfeX0tePROPPwI1aReUwcP")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
