from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/<string:wall>')
def channel(wall):
	return render_template('wall.html', channel=wall)
