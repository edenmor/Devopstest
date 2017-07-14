from flask import Flask

app = Flask(__name__)
@app.route('/hello')
def print_hello():
	return 'hello'
app.run(host='0.0.0.0', port = 5555)
