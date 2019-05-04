from flask import Flask, jsonify, request
from flask_cors import CORS

#importing code that I wrote
from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# sanity check route
@app.route('/colorChart', methods=['GET', 'POST'])
def colorChart():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        yearOne = int(post_data['yearOne'])
        yearTwo = int(post_data['yearTwo'])
        data.buildColorChart(yearOne, yearTwo)
        return jsonify('pong!')

if __name__ == '__main__':
    app.run()
