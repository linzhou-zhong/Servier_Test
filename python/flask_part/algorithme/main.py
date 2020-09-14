import os
import sys
from SparseArrays import *
from flask import Flask, jsonify
from flasgger import swag_from, Swagger

app = Flask(__name__)
swagger = Swagger(app)


# Welcome Page :)
@app.route('/')
def welcome():
    return "Connected to Docker Container :)"


@app.route('/<queries>')
@swag_from('../config/swagger.yaml')
def main(queries):
    try:
        # If Environment Variable 'STRINGS_INPUT' doesn't exist
        if os.environ.get("STRINGS_INPUT") is None:
            raise KeyError

        # Split strings and queries by comma and remove space
        _strings = os.environ.get("STRINGS_INPUT").strip().split(',')
        _queries = queries.split(',')

    except Exception as e:
        # Cannot find correct Environment Variable
        if type(e) is KeyError:
            sys.stdout.write("Environment variable '{}' doesn't exist".format("STRINGS_INPUT"))
        else:
            sys.stdout.write(str(e))
        exit()  # Exit programme

    # Initial SpareArrays class, passing strings and queries as two parameters to it's constructor
    sa = SparseArrays(strings=_strings, queries=_queries)
    res = str(sa.count_frequency_brute_force())
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
