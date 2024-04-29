from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''<h1>PLAY DEEP ROCK GALACTIC</h1>
              <p>ROCK AND STONE!</p>'''
@app.route('/why/<because>')
def why(because):
    nameWithCap = because.title()
    return '''<h1>its fun</h1>
              <p>bottom text, {0}</p>'''.format(nameWithCap)
@app.route('/other/')
def other():
    return '''<h1>UNDERTALE</h1>
              <p>also deltarune</h1>'''