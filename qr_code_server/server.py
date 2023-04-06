from flask import Flask,send_from_directory,redirect
from . import configuration
from .nju_qr_py import njuQrCode
from .nju_login import nju_login
import os

app = Flask("NJU QR server")
castgc=None

@app.route("/")
def err():
    return '<p>网址没粘完咩～</p>'

@app.route(configuration.path+'/qr')
def qr():
    global castgc
    app.logger.info("Calling qr()...")
    if not castgc:
        app.logger.info("Loggin in...")
        login_response=nju_login.login(configuration.username, configuration.password)
        app.logger.info(f"Login cookie: {login_response.cookies}")
        castgc=nju_login.login(configuration.username, configuration.password).cookies['CASTGC']

    app.logger.info("Getting qr content...")
    qr_content=njuQrCode.getQrContent(castgc)

    app.logger.info("Done getting qr content.")
    return qr_content

@app.route(configuration.path)
def index():
    return redirect('.'+configuration.path+'/index.html')

@app.route(configuration.path+'/<path:path>')
def static_files(path):
    current_file_path=os.path.dirname(__file__)
    return send_from_directory(os.path.join(current_file_path,'static'), path)


