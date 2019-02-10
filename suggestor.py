from flask import Flask, render_template, request, jsonify
import comp as cp

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('web_page.html')

@app.route('/suggestor', methods=['POST'])

def suggestor():
	song_name = request.form['name']
	images_names = cp.process_data(song_name)
	return jsonify({'name' : images_names})

if __name__ == '__main__':
	app.run(debug=True)