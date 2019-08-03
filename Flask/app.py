from flask import Flask, request, json
from flask_cors import CORS
import final 
import revfinal
app = Flask(__name__)
CORS(app)

@app.route('/abc', methods=['POST', 'GET'])
def ok():
	source = request.form['source']
	destination = request.form['destination']
	json1 = final.func(source, destination)
	print("A.", json1)
	json2 = revfinal.func(source, destination)
	print("B. ", json2)
	return str(json1+json2)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)