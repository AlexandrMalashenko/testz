from app import app
from flask import request, jsonify


@app.route('/')
def hello_world():
    return 'Oh, hi Mark!'


@app.route('/revert', methods=['POST'])
def revert():
    try:
        json = request.get_json()
        result = json['text'][::-1]
        response = jsonify({'response': result})
        response.status_code = 201
        app.logger.info("{} was reverted on {}".format(json, result))
        return response
    except Exception as err:
        app.logger.error("An error occurred {}".format(err))
        return jsonify({'error': err}), 400
