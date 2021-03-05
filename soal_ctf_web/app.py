from flask import Flask
from flask import render_template, render_template_string
from flask import request

app = Flask(__name__)

@app.route('/')
def index(inp=None):
	req = request.args.get('inp')
	
	if req:
		try:
			payload = "{{%s}}"%req
			templ = "{% extends 'index.html' %}{% block main %}<p>Answer: "+payload+"</p>{% endblock %}"
			return render_template_string(templ)
		except:
			templ = "{% extends 'index.html' %}{% block main %}<p>An error occured</p>{% endblock %}"
			return render_template_string(templ)
	return render_template("index.html")
	
