
from flask import Flask, render_template, request, redirect, session, jsonify
from authentication import Authentication
from utils import remove_file,generate_qr_code

authenticate = Authentication().authenticate




app = Flask(__name__)
app.secret_key = "!241$gariqr"

file_path = "output/qr_code.png"
remove_file(file_path)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(username, password):
            session["username"] = username
            return redirect('/home')
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")


@app.route('/', methods=['GET', 'POST'])
def home():
    show = False


    if request.method == 'POST':
        show=True
        website_url = request.form['url']
        output_file = "static/output/qr_code.png"
        generate_qr_code(website_url, output_file)

        
        return render_template("index.html",message="Done!", show=show)
    else:
        return render_template("index.html", error="Please input a valid URL", show=show)
    

if __name__ == '__main__':
    app.run(debug=True)