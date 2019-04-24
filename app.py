#!/usr/bin/python3

from flask import Flask, render_template
import markdown, codecs
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def show_cv():
    # Load file
    input_file = codecs.open("cv_text.md", mode="r", encoding="utf-8")
    text = input_file.read()
    
    # text markdown to html
    md = markdown.Markdown(extensions = ['extra'])
    html = md.convert(text)

    # Extract points (divs) of the html text
    soup = BeautifulSoup(html, 'html.parser')
    per_brd = soup.find(id="personal_brand")
    per_dta = soup.find(id="personal_data")
    pre = soup.find(id="presentation")
    cmp = soup.find(id="competences")
    exp = soup.find(id="expirience")
    formt = soup.find(id="formation")
    others = soup.find(id="others")

    return render_template('index.html', personal_brand = per_brd, personal_data = per_dta, presentation = pre, competences = cmp, expirience = exp, formation = formt, others = others)