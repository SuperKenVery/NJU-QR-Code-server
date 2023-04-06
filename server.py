from flask import Flask
import configuration
from nju_qr_py import njuQrCode
from nju_login import nju_login

app = Flask("NJU QR server")
castgc=None

@app.route("/")
def index():
    return '<p>网址没粘完咩～</p>'

@app.route(configuration.path+'/qr')
def qr():
    if not castgc:
        castgc=nju_login.login(configuration.username, configuration.password)

    qr_content=njuQrCode.get_qr_content(castgc)
