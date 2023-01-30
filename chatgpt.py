from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import *
from pywebio.pin import *
import openai


def App():
    put_html("<center><h2>Welcome To ChatGPT EG</h2></center>").style("color:black;")
    put_html(
        "<center><p>مرحبا بك يمكنك الان كتابة ما يدور في  ذهنك </p></center>").style("color:gray;")
    put_html("<center><p>Created By <a href='https://www.ahmedfarrag.online'>Ahmed Farrag<a/></p></center>").style("color:black;")
    openai.api_key = ""
    while True:
        def is_valid(ask):
            if ask == " " or ask == "":
                return 'Age cannot be negative!'
        ask = input("Ask Addy: 🤔اسئلني؟", type="text", validate=is_valid)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature=0.9,
            max_tokens=1200,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
        text = response['choices'][0]['text']
        put_text('Addy Tell You : ', text).style(
            "background:#212529; color:white; border-radius:5px")


app = Flask(__name__)

app.add_url_rule('/', 'webio_view', webio_view(App),
                 methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods


app.run()
