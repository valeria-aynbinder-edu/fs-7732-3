from flask import Flask, jsonify, request

app = Flask("example_app")

@app.route('/', methods=['GET', 'POST'])
def greet():
    print(request)
    if request.method == 'GET':
        return 'Get Hello Guest!'
    else:
        return 'POST Hello Guest!'

@app.route('/htmltest')
def greet_html():
    return """
        <h1>HELLO HELLO</h1>
    """

@app.route('/api/tests/json')
def test_json():
    data = {
        'version': 3,
        'name': 'flask_app'
    }
    return jsonify(data)


# path params
@app.route('/api/users/<string:name>/addresses/<int:address_id>')
def greet_name(name, address_id):
    return jsonify({'your name': name,
                    'address_id': address_id})


@app.route('/api/users')
def greet_name_query():
    print(request.args)
    return jsonify({'your name': request.args['name'],
                    'address_id': request.args['address']})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


# api/names/<name>
# api/names?name=herut&






