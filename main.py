from flask import Flask, render_template, request, redirect
from SQLite_alloc import db, Student

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "mzhdsb"
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

# 登入
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    # 获取用户名和密码
    name = request.form.get("name")
    password = request.form.get("password")

    # 做用户名和密码的判断   
    if name == "root" and password == "123456":
        return redirect("/data")  # 成功跳转

    error = '用户名或密码错误'

    return render_template("login.html", error=error)  # 失败报错

# 查看学生信息列表
@app.route("/data", methods=["GET", "POST"])
def show():
    students = Student.query.all()
    return render_template("data.html", students=students)

# 改
@app.route("/edit/<int:nid>", methods=["POST", "GET"])
def edit(nid):
    #选定学生id为nid的学生信息进行操作
    s=Student.query.filter(Student.id == nid).first()
    if request.method == "GET":
        return render_template("edit.html")
    
    # 先删后增，实现修改
    db.session.delete(s)
    db.session.commit()
    FirstName = request.form['FirstName']
    LastName = request.form['LastName']
    Email = request.form['Email']
    new_s = Student(FirstName=FirstName, LastName=LastName, Email=Email)
    db.session.add(new_s)
    db.session.commit()
    return redirect("/data")

 # 删       
@app.route("/delete/<int:nid>")
def delete(nid):
    s=Student.query.filter(Student.id == nid).first()
    db.session.delete(s)
    db.session.commit()
    return redirect("/data")

# 增
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")
    
    FirstName = request.form['FirstName']
    LastName = request.form['LastName']
    Email = request.form['Email']
    new_s = Student(FirstName=FirstName, LastName=LastName, Email=Email)
    db.session.add(new_s)
    db.session.commit()
    return redirect("/data")



if __name__ == "__main__":
    app.run()
