import flask

app = flask.Flask(__name__)

app.config["DEBUG"] = True

@app.route('/', methods=['Get'])
def home():
    return 'Hello'

app.run()


