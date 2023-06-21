import qrcode
from flask import Flask, render_template, request, redirect, session, jsonify
import os

def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def generate_qr_code(url, output_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

app = Flask(__name__)
app.secret_key = "!241$gariqr"

file_path = "output/qr_code.png"
remove_file(file_path)


@app.route('/', methods=['GET', 'POST'])
def login():
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