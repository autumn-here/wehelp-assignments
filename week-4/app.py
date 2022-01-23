from flask import Flask
from flask import request
from flask import redirect 
from flask import url_for
from flask import render_template
from flask import session
import os
app = Flask(__name__)
app.secret_key = os.urandom(20)

#建立網站首頁的回應方式
#login page
# @app.route("/", methods=["POST","GET"])
# def login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return redirect(url_for("user",usr=user))
#     else:
#         return render_template("home.html")
#user page
# @app.route("/<usr>")
# def user(user):
#     return render_template("success.html",user=user)
# if __name__ =="__main__":
#     app.run(debug=True)


@app.route("/", methods=["POST","GET"])
def login():
  global user, password
  if request.method == "POST":
    user = request.form["username"]
    password = request.form["password"]
    return redirect(url_for("verify"))
  else:
    return render_template('home.html')

@app.route("/signin/")
def verify():
  if user == "test" and password == "test":
    session["user"] = user
    return redirect(url_for("member"))
  elif user == "" or password == "":
    global message
    message = "請輸入帳號、密碼"
    return redirect(url_for('error', message=message))
  elif user != "test" or password != "test":
    message = "帳號或密碼輸入錯誤"
    return redirect(url_for('error', message=message))


@app.route("/member/")
def member():
  if  "user" in session:
    return render_template("success.html")
  else:
    return render_template('home.html')


@app.route("/error/")
def error():
  message = request.args.get('message')
  return render_template("fail.html", message=message)

@app.route("/signout")
def signout():
  session.pop("user", None)
  return redirect(url_for('login'))

#啟動網站伺服器
app.run(port=3000)