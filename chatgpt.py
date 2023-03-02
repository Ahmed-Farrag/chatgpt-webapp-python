from flask import Flask, send_from_directory
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.session import *
from pywebio.pin import *
import openai
import argparse
import pywebio



def App():
    put_html("<center><h2>Welcome To ChatGPT EG</h2></center>").style("color:black;")
    put_html(
        "<center><p>مرحبا بك يمكنك الان كتابة ما يدور في  ذهنك </p></center>").style("color:gray;")
    put_html("<center><p>Created By <a href='https://www.ahmedfarrag.online'>Ahmed Farrag<a/></p></center>").style("color:black;")
    openai.api_key = ""
    while True:
        def is_valid(ask):
            if ask == " " or ask == "":
                return 'enter valide string!'
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
        put_text('Addy Tells You : ', text).style(
            "background:#212529; color:white; border-radius:5px")


app = Flask(__name__)

# app.run()


app.add_url_rule('/', 'webio_view', webio_view(App),
                 methods=['GET', 'POST', 'OPTIONS'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    pywebio.start_server(App, port=args.port)
    # start_server(App, port=8080)
