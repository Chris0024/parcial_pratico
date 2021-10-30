from flask import Flask , render_template , request ,session
import random


app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/create/",methods=["POST"])
def create():
	return render_template("create.html")

@app.route("/register/", methods=["POST"])
def register():
	return render_template("register.html")

@app.route("/cv", methods=["POST"])
def cv():
	ad = request.form.get("ad")
	name = request.form.get("name")
	edad = request.form.get("edad")
	dess = request.form.get("dess")
	gen = request.form.get("gen")
	estudios = request.form.get("estudios")
	exp = request.form.get("Exp")
	hab = request.form.get("Hab")
	return render_template("cv.html",ad=ad,name=name,edad=edad,dess=dess,gen=gen,estudios=estudios,exp=exp,hab=hab)


