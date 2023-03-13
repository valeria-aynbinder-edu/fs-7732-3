from flask import Flask, request

app = Flask("sample_web_app")

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/valeria")
def valeria():
    return f"The name is: {request.args.get('name')}"

@app.route("/beauty")
def beauty():
    return "<div><p style='color: red'>HELLO</p>" \
           "<img src='static/funny_cat.jpg' >" \
           "</div>"


@app.route("/users/<string:username>", methods=['GET','POST'])
def get_user_data(username):
    return f"the username is: {username}"



# running from commandline or code
# debugging
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5555)
    app.run(debug=True, port=5001)
