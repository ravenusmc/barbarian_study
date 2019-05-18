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
        data_set_length = data.buildColorChart(yearOne, yearTwo)
        print(data_set_length)
        return jsonify(data_set_length)

@app.route('/graphOne', methods=['GET'])
def graphOne():
    data = Data()
    graphOneData = data.build_Chart_One()
    return jsonify(graphOneData)

if __name__ == '__main__':
    app.run()
