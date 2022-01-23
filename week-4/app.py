from flask import Flask, request, redirect, url_for, render_template, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(20)

@app.route("/", methods=["POST","GET"])
def login():
  if request.method == "POST":
    return redirect(url_for("verify"))
  else:
    return render_template('home.html')

@app.route("/signin/", methods=["POST"])
def verify():
  user = request.form["username"]
  password = request.form["password"]
  if user == "test" and password == "test":
    session["user"] = user
    return redirect(url_for("member"))
  elif user == "" or password == "":
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