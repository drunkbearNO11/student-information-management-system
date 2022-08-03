from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    return "hello"#render_template('login.html')

if __name__=="__main__":
    app.run()