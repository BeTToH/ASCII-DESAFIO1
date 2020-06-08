import os

from flask import Flask, render_template, redirect
from webbrowser import open_new_tab

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    home_pic = 'static/home.jpg'
    return render_template("home.html", image=home_pic)


@app.route('/quem-sou')
def quem_sou():
    quem_sou_pic = 'static/quem-sou2.png'
    return render_template("quem-sou.html", image=quem_sou_pic)


@app.route('/habilidades')
def habilidades():
    c_img = 'static/c_img.png'
    cs6_img = 'static/cs6.jpg'
    python_img = 'static/python_img.jpg'
    return render_template("habilidades.html", image1=python_img, image2=cs6_img, image3=c_img)


@app.route('/contato')
def contato():
    insta = 'static/insta.png'
    e_mail = 'static/e-mail.png'
    linkedin = 'static/linkedin.png'
    github = 'static/git-hub.png'
    twitter = 'static/twt.png'
    return render_template("contato.html", image1=insta, image2=e_mail, image3=linkedin, image4=github, image5=twitter)

if __name__ == '__main__':
    app.run(debug=True)
