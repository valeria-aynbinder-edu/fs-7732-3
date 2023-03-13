from flask import Flask, request, jsonify

app = Flask("sample_web_app")

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/apple")
def get_apple():
    return "Apple.com"

@app.route("/valeria")
def valeria():
    print(request)
    return f"The name is: {request.args.get('name')}"


@app.route("/beauty")
def beauty():
    return "<div><p style='color: red'>HELLO</p>" \
           "</div>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5554, debug=True)
    # app.run(debug=True, port=5001)