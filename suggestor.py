from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('web_page.html')

@app.route('/suggestor', methods=['POST'])
def suggestor():

	email = request.form['email']
	name = request.form['name']

	if name and email:
		newName = name[::-1]

		return jsonify({'name' : newName})

	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)